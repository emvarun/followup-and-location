import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import pylab as P
from matplotlib.backends.backend_pdf import PdfPages
from Results import Data
from astropy.table import Table

def boxPlot(data, numBoxes, boxColors, ax):
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


def var_Init():
	Observ = [ 'BOOTES3', 'MASTER-SAAO', 'Skymapper', 'DECam', 'LaSilla', 'VST', 'TOROS', 'keck',
					 'PanSTARRS', 'Liverpool', 'Hanle', 'PTF', 'Kiso']

	folddir = '/home/varun/IUCAA/O2-Analysis/Sky_Patch/Data-Mod-Dates/O1andO2-2Det/'

	ticknom = [ 'Blenheim',  'Sutherland', 'Siding Spring', 'La Serena', 'La Silla', 'Cerro Paranal', 'Salta', 'Mauna Kea', 
						'Haleakala', 'Canary Islands', 'Hanle', 'Palomar', 'Mt. Ontake']

	boxColors = ['RoyalBlue', 'Orange', 'RoyalBlue', 'deepskyblue', 'deepskyblue', 'deepskyblue', 'deepskyblue', 
						 'Red', 'Red', 'darkgoldenrod', 'Lime', 'Red', 'Lime']

	title = [ '1 sq. degrees', '3 sq. degrees', '10 sq. degrees', '30 sq. degrees', '100 sq. degrees', '300 sq. degrees' ]

	top = [0.015, 0.05, 0.15, 0.4, 0.8, 1.0]
	bottom = 0.
	return Observ, folddir, ticknom, boxColors, title, top, bottom

def ReadData(Observ, folddir):
	det = [ ['H1', 'L1'], ['H1', 'V1'], ['L1', 'V1'], ['H1', 'L1', 'V1'] ]
	n1 = []
	n3 = []
	n10 = []
	n30 = []
	n100 = [] 
	n200 = []
	n300 = []
	for i in range (0, len(Observ)):
		t1, t2, t3, t4, t5, t6, t7 = Data((Observ[i]), folddir, 'Dec', 2, det[0], IndiComb = False, comb = True)
		n1.append(t1)
		n3.append(t2)
		n10.append(t3)
		n30.append(t4)
		n100.append(t5)
		n200.append(t6)
		n300.append(t7)
	n = [ n1, n3, n10, n30, n100, n300]
	return n, len(Observ)

def Analysis(n, numBoxes, nSubplots, top, bottom, boxColors, ticknom, title):
	plt.figure(num=None, figsize=(22, 28), dpi=80, facecolor='w', edgecolor='k')
	t = Table(names=("Observatory", "Lower Box", "Upper Box", "Mean", "Median"), dtype=('S20', 'S6', 'S6', 'S6', 'S6') ) 
	t["Observatory"].format = '^'
	for i,v in enumerate(xrange(nSubplots)):
		v = v+1
		ax1 = plt.subplot(nSubplots,1,v)
		plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.1)		
		medians = list(range(numBoxes))
		means = list(range(numBoxes))
		data = n[i]
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
			t.add_row([ticknom[k] , str(cords[k][0]), str(cords[k][1]), str(means[k]), str(medians[k]) ])
		ax1.set_ylim(bottom, top[i])
		if(i != nSubplots -1 ):
			ax1.axes.get_xaxis().set_visible(False)

	plt.rcParams.update({'font.size': 21})
	ax1.set_xlim(0.5, numBoxes + 0.5)
	xtickNames = plt.setp(ax1, xticklabels=ticknom)
	plt.setp(xtickNames, rotation=90,  fontsize=24)
	plt.xticks(rotation=-90)
#	plt.xlabel("Observatories", fontsize = 24, y = 200.5) #8.5
	t.write('Mean-Median-Table.tex')
	pt.savefig()
	pt.close()



pt = PdfPages('test.pdf')

Observatory, folddir, ticknom, boxColors, title, top, bottom = var_Init()

n, numBoxes = ReadData(Observatory, folddir)

Analysis(n, numBoxes, 6, top, bottom, boxColors, ticknom, title)
