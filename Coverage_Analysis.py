import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import pylab as P
from matplotlib.backends.backend_pdf import PdfPages
from Results import Data
from astropy.table import Table
from params import *

def boxPlot(data, numBoxes, boxColors, ax):
	''' The function returns a boxplot for a given data set. The median of the 
			distribution is repreasented by a line, the mean is marked with a star.
			The edges of the box mark the first and the third quartile.
			To see more details of the parameters involved kindly visit:
			http://matplotlib.org/api/pyplot_api.html
	'''
	bp = ax.boxplot(data, notch=0, sym='+', vert=1, whis=1.5)
	plt.setp(bp['boxes'], color='black', lw = 2)
	plt.setp(bp['whiskers'], color='black', lw = 2)
	plt.setp(bp['fliers'], color='red', marker='+')

	ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.4)
	Cords = []
	for i in range(numBoxes):
		box = bp['boxes'][i]
		boxX = []
		boxY = []
		for j in range(5):
			boxX.append(box.get_xdata()[j])
			boxY.append(box.get_ydata()[j])
			boxCoords = list(zip(boxX, boxY))
		temp = [ boxCoords[1][1], boxCoords[2][1] ]
		Cords.append(temp)
		boxPolygon = Polygon(boxCoords, facecolor=boxColors[i])
		ax.add_patch(boxPolygon)
	return bp, Cords

def ReadData(Location_Datafiles, NsqDeg, obsName, Ndets, IfAllNDet, Period, PeriodComb):
	'''	Reads the data from the output text files obtained from Loop_SkyPatch and returns
			it as a nested list. The nested list enumerates the probability covered for all the 
			patches and NsqDeg covering capability for each location considered. 
	'''
	n = []
	for i in range(0, len(NsqDeg)):
		n.append([])

	for i in range (0, len(obsName)):
		t = Data(Location_Datafiles, NsqDeg, obsName[i], Ndets, IfAllNDet, Period, PeriodComb)
		for j in range(0, len(t)):
			n[j].append(t[j])
	return n, len(n[1])

def Analysis(n, numBoxes, nSubplots, top, bottom, boxColors, obsName, Observatory_Locations, title):
	'''	Creates the boxplots for different N square degrees covered and also writes 
			the table.
	'''
	plt.figure(num=None, figsize=(22, 28), dpi=80, facecolor='w', edgecolor='k')
	t = Table(names=("Observatory", "Lower Box", "Upper Box", "Mean", "Median"), dtype=('S20', 'S6', 'S6', 'S6', 'S6') ) 
	t["Observatory"].format = '^'
	xlabels = []
	for i,v in enumerate(xrange(nSubplots)):
		v = v+1
		ax1 = plt.subplot(nSubplots,1,v)
		plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.1)		
		medians = list(range(numBoxes))
		means = list(range(numBoxes))
		data = n[i]
		print i, v
		t.add_row( [ '', '', '', '', ''  ])
		t.add_row( [ '', '', title[i], '', ''  ])
		t.add_row( [ '', '', '', '', ''  ])
		ax1.set_title(title[i])
		bp, cords = boxPlot(data, numBoxes, boxColors, ax1)
		for k in range(numBoxes):
			med = bp['medians'][k]
			medianX = []
			medianY = []
			for j in range(2):
				medianX.append(med.get_xdata()[j])
				medianY.append(med.get_ydata()[j])
				ax1.plot(medianX, medianY, 'k', lw = 2)
				medians[k] = medianY[0]
				means[k] = np.average(data[k])
			ax1.plot([np.average(med.get_xdata())], [np.average(data[k])],
                color='w', marker='*', markeredgecolor='k', markersize = 14) 		
			t.add_row([ Observatory_Locations[obsName[k]].label , str(cords[k][0]), str(cords[k][1]), str(means[k]), str(medians[k]) ])
			xlabels.append(Observatory_Locations[obsName[k]].label)
		ax1.set_ylim(bottom, top[i])
		if(i != nSubplots -1 ):
			ax1.axes.get_xaxis().set_visible(False)

	plt.rcParams.update({'font.size': 21})
	ax1.set_xlim(0.5, numBoxes + 0.5)
	xtickNames = plt.setp(ax1, xticklabels=xlabels)
	plt.setp(xtickNames, rotation=90,  fontsize=24)
	plt.xticks(rotation=-90)
#	plt.xlabel("Observatories", fontsize = 24, y = 200.5) #8.5
	t.write('Mean-Median-Table.tex')
	pt.savefig()
	pt.close()



pt = PdfPages(BoxplotFile)

n, numBoxes = ReadData(Location_Datafiles, NsqDeg, obsName, Ndets, IfAllNDet, Period, PeriodComb)

Analysis(n, numBoxes, len(NsqDeg), yaxisTop, yaxisBottom, boxColors, obsName, Observatory_Locations, SubplotTitle)
