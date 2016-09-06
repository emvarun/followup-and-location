import numpy as np
import astropy.units as u
from astropy.coordinates import EarthLocation

class Observatory(object):
	def __init__(self, lat, lon, alt, horizon, location_label):
		self.location = EarthLocation(lat=lat*u.deg,lon=lon*u.deg, height=alt*u.m) # lat lon input to astropy
		self.horizon = horizon
		self.twilight = 18.
		self.label = location_label

def ObsDetail():
	Observatory_Locations = { 
		'IGO': Observatory( 19.083333, 73.666667, 1000.0, 24., 'Girawali'),
		'Hanle': Observatory( 32.779444, 78.964167, 4500.0, 24., 'Hanle' ),
		'BlackGEM': Observatory( -29.261167, -70.731333, 2400.0, 24., 'LaSilla' ),
		'PTF': Observatory( 33.355833, -116.863889, 1712.0, 24., 'Palomar'),
		'Skymapper': Observatory( -31.2733, 149.0644, 1163.0, 24., 'Siding Spring'),
		'BOOTES3':	Observatory( -45.039699, 169.6835, 27.0, 24., 'Blenheim'),
		'MASTER-SAAO':	Observatory( -32.298, 20.810, 1760.0, 24., 'Sutherland'),
		'TOROS':	Observatory( -24.61, -67.32, 4650.0, 24., 'Salta'),
		'VST':	Observatory( -24.6272, -70.4036, 2600.0, 24., 'Cerro Paranal'),
		'keck':	Observatory( 19.82636, -155.47501, 4145.0, 24., 'Mauna Kea'),
		'PanSTARRS':	Observatory( 20.7083, -156.2571, 3052.0, 24., 'Haleakala'),
		'Kiso':	Observatory( 35.794167, 137.628333, 1130.0, 24., 'Mt. Ontake'),
		'LaSilla':	Observatory( -29.261167, -70.731333, 2400.0, 24., 'LaSilla'),
		'DECam':	Observatory( -30.169661, -70.806525, 2207.0, 24., 'La Serena'),
		'Liverpool':	Observatory( 28.76234, -17.87925, 2363.0, 24., 'Canary Islands')
	}
	return Observatory_Locations
