import os, re
import numpy as np
from astropy.time import Time
from astropy.io import fits
import random
from datetime import date
from random import randint
from optparse import OptionParser

def GetSpDay(SpDay):
	if (SpDay == 'Vernal'):
		mon = 3
		day = 20
		year = 2010
		d1 = date(year, mon, day)
	if (SpDay == 'Summer'):
		mon = 6
		day = 21
		year = 2010
		d1 = date(year, mon, day)
	if (SpDay == 'Autumn'):
		mon = 9
		day = 23
		year = 2010
		d1 = date(year, mon, day)
	if (SpDay == 'Winter'):
		mon = 12
		day = 21
		year = 2010
		d1 = date(year, mon, day)
	return d1

def SetPeriodO1(oldDate):
	nos = [ 1, 2, 3, 4 ]
	noss = random.choice(nos)	
	if( noss == 1):
		months = [ 9, 1]
		mon = random.choice(months)	
	else:
		months = [ 10, 11, 12]
		mon = random.choice(months)	
	if(mon == 10 or mon == 12):
		days = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
	if(mon == 11):
		days = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
	if(mon == 9):
		days = [ 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
	if(mon == 1):
		days = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
	day = random.choice(days)
	d1 = date(oldDate[0], mon, day)	
	return d1

def SetPeriodO2(oldDate, nDet, dets):
	if (nDet == 2):
		if( dets.find('H1') != -1 and dets.find('L1') != -1):
			nos = [ 1, 2, 3, 4, 5, 6, 7 ]
			#KEEPING THE DISTRIBUTION UNIFORM
			noss = random.choice(nos)	
			if( noss == 1):
				months = [ 3, 12]
				mon = random.choice(months)	
			else:
				months = [ 4, 5, 6, 10, 11]
				mon = random.choice(months)	
			if(mon == 10 or  mon == 5 ):
				days = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
			if( mon == 11 or mon == 4 or mon == 6) :
				days = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
			if(mon == 3):
				days = [ 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
			if(mon == 12):
				days = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10]
			day = random.choice(days)
			d1 = date(oldDate[0], mon, day)	
		else:
			nos = [ 1, 2, 3, 4, 5, 6, 7 ]
			#KEEPING THE DISTRIBUTION UNIFORM
			noss = random.choice(nos)	
			if( noss == 1):
				mon = 3
			else:
				months = [ 4, 5, 6]
				mon = random.choice(months)	
			if(mon == 5 ):
				days = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
			if( mon == 4 or mon == 6) :
				days = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
			if(mon == 3):
				days = [ 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
			day = random.choice(days)
			d1 = date(oldDate[0], mon, day)	
	if (nDet == 3):
		nos = [ 1, 2, 3, 4, 5, 6, 7 ]
		noss = random.choice(nos)	
		#KEEPING THE DISTRIBUTION UNIFORM
		if( noss == 1):
			mon = 3
		else:
			months = [ 4, 5, 6]
			mon = random.choice(months)	
		if(mon == 5 ):
			days = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
		if( mon == 4 or mon == 6) :
			days = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
		if(mon == 3):
			days = [ 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
		day = random.choice(days)
		d1 = date(oldDate[0], mon, day)	
	return d1


def tformNdays(time, N, longDeg = '45d'):
	time = Time( time, format = 'iso', scale = 'utc', location = (longDeg, '45d') )
	#23h56m4.090530833s mjd to transform by one sidereal day 0.9972695663290856
	time = time.mjd
	time = time + 0.99726957*N
	time = Time( time, format = 'mjd', scale = 'utc', location = (longDeg, '45d') )
	time = time.iso
	time = Time( time, format = 'iso', scale = 'utc', location = (longDeg, '45d') )
	time = time.isot
	return time

def editDate(fitsfile, titlesuffix = 'Mod-Date', EquiSol = False, SpDay = None):
	data, header = fits.getdata(fitsfile, header=True)
	f = fits.open(fitsfile)
	stim= f[1].header["DATE-OBS"]
	timeI = stim[:10]+" "+stim[11:]
	temp = timeI.strip().split(' ')
	temp = temp[0].strip().split('-')
	temp = [int(i) for i in temp]
	d0 = date(temp[0], temp[1], temp[2] )
#########################################################################################
	if(EquiSol == False):
		modD = SetPeriodO1(temp)
	else:
		modD = GetSpDay(SpDay)
	delta = modD - d0
	N = delta.days
	Ntime = tformNdays( timeI, N )
	header['DATE-OBS'] = Ntime
#########################################################################################
	outputfile = fitsfile.replace('.fits.gz', '-' + titlesuffix +'.fits.gz')
	fits.writeto(outputfile, data, header, clobber=True)

def Loopfits(rootdir):
	for dirpath, dirname, files in os.walk(rootdir):
		for filename in files:
			path = os.path.join(dirpath, filename)
			name = filename.strip().split('.')
			if(name[len(name)-1] == 'gz' ):
				editDate(path)

parser = OptionParser()
parser.add_option("-l", "--location", action="store",type="string", metavar=" NAME", help="Location of fits files")
(opts,args) = parser.parse_args()
rootdir = opts.location

Loopfits(rootdir)
