import numpy as np
from subprocess import check_output
import os
import subprocess	
from subprocess import Popen, PIPE
from Sky_Patch import Coverage
from params import *

#LIST OF LOCATIONS CONSIDERED
for i in range (0, len(obsName)):
	tCoverage = []
	for dirpath, dirname, files in os.walk(folddir):
		for filename in files:
			path = os.path.join(dirpath, filename)
			name = filename.strip().split('.')
			if(name[-1] == 'gz' ):
				print obsName[i], path
				nlist = Coverage(str(path), obsName[i], Texp, NsqDeg, stepsize)
				tCoverage.append(nlist)

	f=open( str(outfile) + '-' + str(obsName[i]) + '.txt','w') 
	for item in tCoverage:
		f.write(str(item) + '\n')
	f.close()
