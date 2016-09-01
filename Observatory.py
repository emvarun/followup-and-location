import numpy as np

class Observatory(object):
	def __init__(self, lat, lon, alt, horizon):
		self.location = EarthLocation(lat=lat*u.deg,lon=lon*u.deg, height=alt*u.m) # lat lon input to astropy
		self.horizon = horizon
		self.twilight = 18.

def ObsDetail(ObsName):
	if(ObsName == 'IGO'):
		Obs = Observatory( 19.083333, 73.666667, 1000.0, 24.)
	if(ObsName == 'Hanle'):
		Obs = Observatory( 32.779444, 78.964167, 1000.0, 24.)
	if(ObsName == 'BlackGEM'):
		Obs = Observatory( -29.261167, -70.731333, 2400.0, 24.)
	if(ObsName == 'PTF'):
		Obs = Observatory( 33.355833, -116.863889, 1712.0, 24.)
	if(ObsName == 'Skymapper'):
		Obs = Observatory( -31.2733, 149.0644, 1163.0, 24.)
	if(ObsName == 'BOOTES3'):
		Obs = Observatory( -45.039699, 169.6835, 27.0, 24.)
	if(ObsName == 'MASTER-SAAO'):
		Obs = Observatory( -32.298, 20.810, 1760.0, 24.)
	if(ObsName == 'TOROS'):
		Obs = Observatory( -24.61, -67.32, 4650.0, 24.)
	if(ObsName == 'TAROT'):
		Obs = Observatory( -29.261111, -70.731389, 2375.0, 24.)
	if(ObsName == 'VST'):
		Obs = Observatory( -24.6272, -70.4036, 2600.0, 24.)
	if(ObsName == 'keck'):
		Obs = Observatory( 19.82636, -155.47501, 4145.0, 24.)
	if(ObsName == 'PanSTARRS'):
		Obs = Observatory( 20.7083, -156.2571, 3052.0, 24.)
	if(ObsName == 'Kiso'):
		Obs = Observatory( 35.794167, 137.628333, 1130.0, 24.)
	if(ObsName == 'LaSilla'):
		Obs = Observatory( -29.261167, -70.731333, 2400.0, 24.)
	if(ObsName == 'DECam'):
		Obs = Observatory( -30.169661, -70.806525, 2207.0, 24.)
	if(ObsName == 'Liverpool'):
		Obs = Observatory( 28.76234, -17.87925, 2363.0, 24.)
	if(ObsName == 'P200Hale'):
		Obs = Observatory( 33.3558, -116.8639, 1712.0, 24.)
	return Obs
