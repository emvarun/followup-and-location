import numpy as np

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


def Data(obsName, folddir, val, detNos, detNet, IndiComb, comb):
	n1 = []
	n3 = []
	n10 = []
	n30 = []
	n100 = []
	n200 = []
	n300 = []
	D1 = []
	D3 = []
	D10 = []
	D30 = []
	D100 = []
	D200 = []
	D300 = []

	filename = str(folddir) + str(obsName)

	with open(str(filename) + '.txt') as f:
		print f
		for line in f:
			line = line.replace("[", "")
			line = line.replace("]", "")
			line = line.replace("'", "")
			line = line.replace(" ", "")
			data = line.strip().split(',')
			result = []
			detail = []
			for i in range (0, len(data)):
				if( isfloat(data[i]) ):
					result.append(float(data[i]))
				else:
					detail.append(data[i])
			temp = detail[0].strip().split('-')
			detail[0] = int(temp[1])

			if(len(result) < 14):
				if(int(result[0]) != 1):
					result = [result[0], result[1], result[0], result[1], result[0], result[1], result[0], result[1], 
										result[0], result[1], result[0], result[1], result[0], result[1] ]
				elif(int(result[2]) != 3):
					result = [result[0], result[1],       3.0, result[3],      10.0, result[3],     30.0, result[3], 
										    100.0, result[3],     200.0, result[3],	   300.0, result[3] ]
				elif(int(result[4]) != 10):
					result = [result[0], result[1], result[2], result[3],      10.0, result[5],     30.0, result[5], 
										    100.0, result[5],     200.0, result[5],     300.0, result[5] ]
				elif(int(result[6]) != 30):
					result = [result[0], result[1], result[2], result[3], result[4], result[5],     30.0, result[7], 
										    100.0, result[7],     200.0, result[7],     300.0, result[7] ]
				elif(int(result[8]) != 100):
					result = [result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], 
										    100.0, result[9],     200.0, result[9],     300.0, result[9] ]
				elif(int(result[10]) != 200):
					result = [result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], 
										result[8], result[9],    200.0, result[11],    300.0, result[11] ]
				elif(int(result[12]) != 300):
					result = [result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], 
										result[8], result[9],result[10],result[11],    300.0, result[13] ]


			# D set will contain all the patches with the same no of detectors in action
			# d set will contain all the patches with the same no of detectors in that period of the year
			D1.append(result[1])
			D3.append(result[3])
			D10.append(result[5])
			D30.append(result[7])
			D100.append(result[9])
			D200.append(result[11])
			D300.append(result[13])
			if(IndiComb == False):
				if( (len(detail) - 1) == detNos):
					n1.append(result[1])
					n3.append(result[3])
					n10.append(result[5])
					n30.append(result[7])
					n100.append(result[9])
					n200.append(result[11])
					n300.append(result[13])
			else:
				if( (len(detail) - 1) == detNos):
					if (val == 'Mar'):
						if(detail[0] == 2 or detail[0] == 3 or detail[0] == 4):
							if( detail[1] == detNet[0] and detail[2] == detNet[1]):
								n1.append(result[1])
								n3.append(result[3])
								n10.append(result[5])
								n30.append(result[7])
								n100.append(result[9])
								n200.append(result[11])
								n300.append(result[13])
					if (val == 'Jun'):	
						if(detail[0] == 5 or detail[0] == 6 or detail[0] == 7):
							if( detail[1] == detNet[0] and detail[2] == detNet[1]):
								n1.append(result[1])
								n3.append(result[3])
								n10.append(result[5])
								n30.append(result[7])
								n100.append(result[9])
								n200.append(result[11])
								n300.append(result[13])
					if (val == 'Sep'):
						if(detail[0] == 8 or detail[0] == 9 or detail[0] == 10):
							if( detail[1] == detNet[0] and detail[2] == detNet[1]):
								n1.append(result[1])
								n3.append(result[3])
								n10.append(result[5])
								n30.append(result[7])
								n100.append(result[9])
								n200.append(result[11])
								n300.append(result[13])
					if (val == 'Dec'):
						if(detail[0] == 11 or detail[0] == 12 or detail[0] == 1):
							if( detail[1] == detNet[0] and detail[2] == detNet[1]):
								n1.append(result[1])
								n3.append(result[3])
								n10.append(result[5])
								n30.append(result[7])
								n100.append(result[9])
								n200.append(result[11])
								n300.append(result[13])

	if(comb == True):
		return n1, n3, n10, n30, n100, n200, n300
	else:
		return D1, D3, D10, D30, D100, D200, D300

# D set will contain all the patches with the same no of detectors in action
# n set will contain all the patches with the same no of detectors in that period of the year
