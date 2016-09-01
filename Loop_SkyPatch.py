import numpy as np
from subprocess import check_output
import os
import subprocess	
from subprocess import Popen, PIPE
from Sky_Patch import Coverage
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--inputdir", action="store", type="string", metavar=" NAME", help="Input Directory of fits files")
parser.add_option("-o", "--outfile", action="store", type="string", metavar=" NAME", help="Name of output file")
parser.add_option("-t", "--exptime", action="store", type="int", metavar=" NAME", help="time allowed to followup each event")
(opts,args) = parser.parse_args()

rootdir = opts.inputdir
outfile = opts.outfile
Texp = opts.exptime

#LIST OF LOCATIONS CONSIDERED
obsName = ['PTF', 'Hanle']
NsqDeg = [ 1., 3., 10., 30., 100., 200., 300. ]

for i in range (0, len(obsName)):
	tCoverage = []
	for dirpath, dirname, files in os.walk(rootdir):
		for filename in files:
			path = os.path.join(dirpath, filename)
			name = filename.strip().split('.')
			if(name[-1] == 'gz' ):
				print obsName[i], path
				nlist = Coverage(str(path), obsName[i], Texp, NsqDeg)
				tCoverage.append(nlist)

	f=open( str(outfile) + '-' + str(obsName[i]) + '.txt','w') 
	for item in tCoverage:
		f.write(str(item) + '\n')
	f.close()
