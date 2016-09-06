#!/usr/bin/python
import os, re
import numpy as np
import healpy as hp
import astropy.units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz, get_sun
from astropy.time import Time
from astropy.io import fits
import ephem
from ephem import *
from params import Observatory_Locations

def Patch(fitsfile, verbose=False, prob_cover=0.99):
	(pixProb, header) = hp.read_map(fitsfile, field=0, nest=False, hdu=1, h=True, verbose=False, memmap=False)
	nside = hp.npix2nside(len(pixProb))
	theta, phi = hp.pix2ang(nside, np.arange(0, len(pixProb)), nest=False)
	total_prob = np.sum(pixProb)
	pixArea = hp.nside2pixarea(nside, degrees = 'True')

	nonzero = pixProb > 0.0
	nonzeroProb, nonzeroTheta, nonzeroPhi = pixProb[nonzero], theta[nonzero], phi[nonzero]
	order = np.argsort(-nonzeroProb)
	sortedProb, sortedTheta, sortedPhi = nonzeroProb[order], nonzeroTheta[order], nonzeroPhi[order]	

	# Now select top prob_cover %
	SigPix = np.cumsum(sortedProb) <= prob_cover
	if verbose:
		rejPix = np.cumsum(nonzeroProb) >= prob_cover
	fin_pixProb = sortedProb[SigPix]	
	fin_theta, fin_phi = sortedTheta[SigPix], sortedPhi[SigPix]	
	return fin_pixProb, fin_theta, fin_phi, nside, pixArea


def onSkyPatch(pixprob, fin_theta, fin_phi, total_prob, obsName, tim, twilight=18., verbose=False):
	RA, Dec = np.rad2deg(fin_phi), np.rad2deg(np.pi/2.0 - fin_theta)	# RA & Dec of pixels

	skycords = SkyCoord(RA*u.deg, Dec*u.deg)
	otime = tim.iso
	altaz = skycords.transform_to(AltAz(location=Observatory_Locations[obsName].location, obstime=otime))
	alt, az = altaz.alt.degree, altaz.az.degree

	aboveSky = alt > Observatory_Locations[obsName].horizon 
	above_alt, above_az, Prob = alt[aboveSky], az[aboveSky], pixprob[aboveSky] 
	abovSkyProb = np.sum(Prob) 
	
	sun_below = get_sun(tim).transform_to(AltAz(location=Observatory_Locations[obsName].location, obstime=otime)).alt.degree < -np.abs(twilight)
	
	if(abovSkyProb*sun_below != 0):
		obs_prob = pixprob[aboveSky]
		pixprob[aboveSky] = 0.0
	else:
		obs_prob = 0.0
	return [above_alt, above_az, Prob], [abovSkyProb, abovSkyProb*sun_below, total_prob - abovSkyProb*sun_below, sun_below], pixprob, obs_prob


def totalSkyPatch(fitsfile, pixprob, theta, phi, obsName, nsteps, h, twilight=18., verbose=False):
	(pixelProb, header) = hp.read_map(fitsfile, field=0, nest=False, hdu=1, h=True, verbose=False, memmap=False)
	total_prob = np.sum(pixelProb)
	f = fits.open(fitsfile)
	stim= f[1].header["DATE-OBS"]
	detectors = f[1].header["INSTRUME"]
	time = stim[:10]+" "+stim[11:]
	time = Time( time, format = 'iso', scale = 'utc')
	time = time.mjd
	probObserve = []
	thetaObserve = []
	phiObserve = []
	nObserve = 0.0
	for l in range(0, nsteps):
		tim = time + h*l*second
		tim = Time(tim, format = 'mjd')
		aboveSky, instt_vis, pixprob, obs_prob = onSkyPatch(pixprob, theta, phi, total_prob, obsName, tim)
		if(np.sum(obs_prob) > 0.0000001):
			obs_prob = [x for x in obs_prob if x != 0]
			obs_prob = np.array(obs_prob).tolist()
			probObserve	= probObserve + obs_prob
			nObserve = float(len(obs_prob)) + nObserve
	return probObserve, nObserve, [stim, detectors]


def Coverage(fitsfile, obsName, Texp, NsqDeg, h):
	# Texp is how many hours after the trigger one could possibly followup
	Texp2secs = Texp*3600
	nsteps = Texp2secs/h
	fin_pixProb, fin_theta, fin_phi, nside, pixArea = Patch(fitsfile)
	probObserve, nObserve, timdet = totalSkyPatch(fitsfile, fin_pixProb, fin_theta, fin_phi, obsName, nsteps, h)
	probObserve = sorted(probObserve, reverse=True)
	cumProb = np.cumsum(probObserve)
	nceil = [0.]*len(NsqDeg)
	n = [0.]*len(NsqDeg)
	n.append(timdet)
	for i in range (0, len(NsqDeg)):
		nceil[i] = np.ceil(NsqDeg[i]/pixArea) 

	for i in range(0, len(NsqDeg)):
		area = nceil[i]*pixArea
		if(nObserve != 0):
			if(nceil[i] < nObserve):
				n[i] = [ area, cumProb[nceil[i]] ]
			else:
				n[i] = [ area, cumProb[nObserve-1] ]
		else:
			n[i] = [area, 0.]
	return n
