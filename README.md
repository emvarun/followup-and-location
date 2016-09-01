I. PACKAGE REQUIRED AND INSTALLATION GUIDELINES
================================================

1.		ASTROPY
------------------------------------------------
		a.	Using pip
				pip install --no-deps astropy
		b.	Anaconda python distribution
				conda install astropy

2.		HEALPY
------------------------------------------------
		a.	Using pip
				pip install --user healpy
				To upgrade:
				pip install --user --upgrade healpy
		b.	curl -O https://pypi.python.org/packages/source/h/healpy/healpy-1.9.1.tar.gz
				To build:
				tar -xzf healpy-1.9.1.tar.gz
				pushd healpy-1.9.1
				python setup.py install --user
				popd

3.		EPHEM
------------------------------------------------
		a. pip install ephem


II. WORKING WITH THE CODE: STEP BY STEP
================================================

1.	Obtaining the fits files
------------------------------------------------
The released set of fits file can be downloaded from "http://www.ligo.org/scientists/first2years/".
The following step is to edit the dates of the fits file to the period of interest -- say LIGO 
observational period. Also, for ease of analysis segregate the patches into two folders one with 
patches recovered with two detector network and the other with three detectors.

2.	Edit dates with EditDate.py
------------------------------------------------
There are two cautions to be taken care of. First, the detector schedule during a given period. 
Further the events must be smeared uniformly over a given observational period. Second, the patch 
orientation doesn't change with respect to the earth. In other words, the sidereal time must 
remain invariant. 

3.	Getting the observed probability for each event -- given a location and time 't' after the trigger to followup
------------------------------------------------
One is free to use any location in the observatory file, add locations  in  the "Observatory.py" 
file to  consider other locations of interest. In our analysis we consider a period of 
twenty-four hours after the trigger. However, one can tune this  parameter. We consider the 
patch (rise or set) in steps of 600 seconds. The "Loop_SkyPatch.py" loops and analyses all the 
fits files present in a directory. For each location  considered in the list "obsName" of this 
file, one obtains the probability covered for all the events  ( fits files in the parsed 
directory) in an output text file named after the observatory considered. This covered 
probability is calculated in the 		"Sky_Patch.py" file. If one wishes to change the camera 
capability (N square degree), edit the variable "NsqDeg". NOTE: Observatory is a misnomer 
here. The correct word is location as we don't consider any observatory parameters. The term 
observatory is just used for convenient referencing.
				
4.	Analysis 
------------------------------------------------
The file "Results.py" gives the probability covered, however there are different combinations from which one could
choose. Like the number of detectors to consider(comb), take events only around a given period or the year or not 
(Indicomb), one can also add which pair of detectors to choose HL or LV or HV, however, that version isn't shared 
to avoid too much complicacy. Run "Coverage_Analysis.py" which summarizes the results in a boxplot. A table in 
"tex" format which has the values of median, median and the quartiles . 
	
For any queries feel free to contact "varun.srivastava@students.iiserpune.ac.in"
