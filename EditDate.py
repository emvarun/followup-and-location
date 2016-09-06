import numpy as np
from datetime import date
from astropy.io import fits
from astropy.time import Time
from params import *
import os, re

def PromptEditDate():
	boolval= raw_input('Do you wish to edit the dates of LIGO science run? The released dates are from August to October. \n')
	if( boolval == 'True' or boolval == 'Yes' or boolval == 'yes' or boolval == 'y'  or boolval == 'Y' or boolval == 1):
		boolval = True
	else:
		boolval = False
		print 'Dates not editted \n'
	return boolval

def StdDatetoMJD(input_list):
	'''		Converts the standard date YYYY-MM-DD to the MJD
	'''
	input_list = "".join(input_list.split())
	day, month, year = input_list.split(',')
	time = str(year) + '-' + str(month) + '-' + str(day) + 'T00:00:00'
	time = Time(time, format='isot', scale='utc')
	return time.mjd


def GetFitsfilesList(rootdir):
	''' Returns the list of all the fitsfiles whose dates will be editted
	'''
	fitsfiles = []
	for dirpath, dirname, files in os.walk(rootdir):
		for filename in files:
			path = os.path.join(dirpath, filename)
			name = filename.strip().split('.')
			if(name[-1] == 'gz' ):
				fitsfiles.append(path)
	return fitsfiles

def PromptStartEndDate():
	input_list= raw_input( 'Enter the start date of LIGO Operation: (Day, Month, Year)  ')
	start_LIGO = StdDatetoMJD(input_list)
	input_list = raw_input('Enter the stop date of LIGO Operation: (Day, Month, Year)   ')
	stop_LIGO = StdDatetoMJD(input_list)
	############################ NOTE THAT LIGO IS ASSUMED ON IN THE PERIOD OF VIRGO ON ############################
	input_list= raw_input( 'Enter the start date of VIRGO Operation: (Day, Month, Year)  ')
	start_VIRGO = StdDatetoMJD(input_list)
	input_list = raw_input('Enter the stop date of VIRGO Operation: (Day, Month, Year)   ')
	stop_VIRGO = StdDatetoMJD(input_list)
	return start_LIGO, stop_LIGO, start_VIRGO, stop_VIRGO

def getOverlap(start_LIGO, stop_LIGO, start_VIRGO, stop_VIRGO):
	overlap = False
	if(start_LIGO < start_VIRGO and stop_LIGO > start_VIRGO):
		overlap = True
	if(start_LIGO < stop_VIRGO and stop_LIGO > stop_VIRGO):
		overlap = True
	return overlap, [ min(start_LIGO, start_VIRGO), max(stop_LIGO, stop_VIRGO) ]

def TransformDates(Inj_time, delta, longDeg = '45d'):
	time = Time( Inj_time, format = 'iso', scale = 'utc', location = (longDeg, '45d') )
	time = time.mjd
	#23h56m4.090530833s mjd to transform by one sidereal day 0.9972695663290856
	time = time + 0.99726957*int(delta)
	time = Time( time, format = 'mjd', scale = 'utc', location = (longDeg, '45d') )
	time = time.iso
	time = Time( time, format = 'iso', scale = 'utc', location = (longDeg, '45d') )
	time = time.isot
	return time


def EditDates(fitsfile, start_LIGO, stop_LIGO, start_VIRGO, stop_VIRGO, suffixtitle):
	data, header = fits.getdata(fitsfile, header=True)
	f = fits.open(fitsfile)
	stim= f[1].header["DATE-OBS"]
	dets = f[1].header["INSTRUME"]
	Inj_time = stim[:10]+" "+stim[11:]
	OldDate = Time( Inj_time, format = 'iso', scale = 'utc')
	Inj_time = OldDate.mjd
	isoverlap, period = getOverlap(start_LIGO, stop_LIGO, start_VIRGO, stop_VIRGO)
	if(dets.find('H1') != -1 and dets.find('L1') != -1 and dets.find('V1') == -1): 										# HL Patches
		if(isoverlap == False):
			NewDate = [ np.random.uniform(start_LIGO, stop_LIGO), np.random.uniform(start_VIRGO, stop_VIRGO) ]
			NewDate = np.random.choice(NewDate)	
		else:		
			NewDate = np.random.uniform(period[0], period[1])

	if(dets.find('H1') != -1 and dets.find('L1') != -1 and dets.find('V1') != -1):										# Three Detector Patches
		NewDate = np.random.uniform(start_VIRGO, stop_VIRGO) 

	if(dets.find('H1') != -1 or dets.find('L1') != -1 and dets.find('V1') != -1 and len(dets) < 6):		# HV or LV patches
		NewDate = np.random.uniform(start_VIRGO, stop_VIRGO) 

	NewDate = Time( NewDate, format = 'mjd', scale = 'utc')
	delta = (NewDate.value - Inj_time)
	InvSideRealTime =	TransformDates(OldDate, delta)
	header['DATE-OBS'] = InvSideRealTime
	outputfile = fitsfile.replace('.fits.gz', '-' + suffixtitle + '.fits.gz')
	fits.writeto(outputfile, data, header, clobber=True)
	


boolval = PromptEditDate()
if boolval:
	fitsfiles = GetFitsfilesList(rootdir)
	start_LIGO, stop_LIGO, start_VIRGO, stop_VIRGO = PromptStartEndDate()
	print '\n THE FILES WITH MODIFIED DATES WILL BE OUTPUTED IN THE SAME FOLDER WITH "'+ str(suffix2ModDateFits) + '" APPENDED TO ITS NAME \n'
	for fitsfile in fitsfiles:
		EditDates(fitsfile, start_LIGO, stop_LIGO, start_VIRGO, stop_VIRGO, suffix2ModDateFits)
