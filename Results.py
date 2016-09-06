import numpy as np
import os
from params import *

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


def Data(Location_Datafiles, NsqDeg, obsName, Ndets, IfAllNDet = False, Period = None, PeriodComb = False ):
	n = []
	D = []
	for i in range(0, len(NsqDeg)):
		n.append([])
		D.append([])

	filename = os.path.join(Location_Datafiles, 'Summary')
	filename = filename + '-' + str(obsName)+ '.txt'
	print filename
	with open(filename) as f:
		for line in f:
			line = line.replace("[", "")
			line = line.replace("]", "")
			line = line.replace("'", "")
			line = line.replace(" ", "")
			data = line.strip().split(',')
			for i in range(0, len(NsqDeg)):
				D[i].append(float(data[2*i + 1]))

			detail = []
			for i in range (0, len(data)):
				if( isfloat(data[i]) == False ):
					detail.append(data[i])
			temp = detail[0].strip().split('-')
			month = int(temp[1])

			if(PeriodComb == False):
				if( (len(detail) - 1) == Ndets):
					for i in range(0, len(NsqDeg)):
						n[i].append(float(data[2*i + 1]))

			else:
				if( (len(detail) - 1) == Ndets):
					if (Period == 'Mar'):
						if(month == 2 or month == 3 or month == 4):
							for i in range(0, len(NsqDeg)):
								n[i].append(float(data[2*i + 1]))
					if (Period == 'Jun'):	
						if(month == 5 or month == 6 or month == 7):
							for i in range(0, len(NsqDeg)):
								n[i].append(float(data[2*i + 1]))

					if (Period == 'Sep'):
						if(month == 8 or month == 9 or month == 10):
							for i in range(0, len(NsqDeg)):
								n[i].append(float(data[2*i + 1]))

					if (Period == 'Dec'):
						if(month == 11 or month == 12 or month == 1):
							for i in range(0, len(NsqDeg)):
								n[i].append(float(data[2*i + 1]))

	if(IfAllNDet == True):
		return n
	else:
		return D
