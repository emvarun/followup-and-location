I. PACKAGE REQUIRED
================================================

1.		NUMPY
------------------------------------------------
		a.	sudo apt-get install python-numpy



2.		ASTROPY
------------------------------------------------
		a.	Using pip
				pip install --no-deps astropy
		b.	Anaconda python distribution
				conda install astropy

3.		HEALPY
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

4.		EPHEM
------------------------------------------------
		a. pip install ephem


II.	INSTALLATION GUIDELINES
================================================
To download all the codes kindly run the following command in the terminal:
```html
git clone https://github.com/emvarun/followup-and-location
```


III. WORKING WITH THE CODE: STEP BY STEP
================================================


1.	Obtaining the fits files
------------------------------------------------
The released set of fits file can be downloaded from 'http://www.ligo.org/scientists/first2years/'.
Note: The patches are dependent on the detector senstivity, thus, the two detector 
patches of 'fits-2015' are for an LIGO-O1 detector sensitivity, while the same for 
'fits-2016' are with LIGO-O2 detector sensitivity. Thus, the two sets are fundamentally 
different


2.	Edit dates
------------------------------------------------
The following step is to edit the dates of trigger in the original fits file header 
to the period of interest -- say LIGO observational period. Run the file in the terminal 
as 
```python
python EditDate.py
```
The user will be  prompted if they want to change the date of 
injection in the released fits file to a period of their interest. The new files will be 
saved in the same directory with the released set of files but will have a 'Mod-Date' 
suffixed in their name. The user is free to move them to a convenient folder of his interest. 
Note: Update the variable 'folddir' in 'params.py' file to the folder directory which contains 
all the fits file one wishes to analyse over. Please change the variable accordingly.


3.	Analysis
------------------------------------------------
The locations that one wishes to analyse can be added in the 'Observatory.py' file.
To remove locations one can simply comment them out. Once the folder directory 'folddir' 
is updated. One can proceed with the analysis of the fits files. The variables involved are 
listed in 'params.py'. The file 'Sky_patch.py' evaluates the probability covered upto N 
square degrees for a given fits file. The file 'Loop_SkyPatch.py' loops over all the files 
in the folder 'folddir', and returns a text file which contains the probability covered upto 
the given N square degrees 'NsqDeg', for all the fits files one runs over. To run this part, 
open the terminal and once in the directory where these codes exist, run 
```
python Loop_SkyPatch.py
```
One will get the output files in the directory given by variable 'Location_Datafiles' in the 
'params.py' file. The file 'params.py' contains the description of all the variables involved.
				

4.	Post-Analysis: Plots and Tables
------------------------------------------------
The file 'Results.py' reads the output data files from the previous step. One needs to 
run
```python 
python Coverage_Analysis.py 
```
The code returns a boxplot which compares the performance
of different locations for all the fits files. A table is returned which contains the mean 
and median of the probability distribution for a given location and the first and third 
quartile values. The parameters taken by the function 'ReadData' are explained below. 
The variable 'IfAllNDet' is a bool value parameter which if True analyses and plots all 
the events  irrespective of the number of detectors involved. However, when set as False,
it reads only the those events which are recovered by the number of detectors defined by
'Ndets'. The variable 'PeriodComb' is also a bool variable which when initialized as True,
considers only those events in the analysis that occured during the period of the year defined
by 'Period'. Eg. if period is set to 'Sep', the analysis will consider all events that occur 
in August, September and October. The variable 'yaxisTop' defines the upper probability limit
of each of the subplots. This has to be editted accordingly when one makes any change to the
'NsqDeg' variable.


For any queries feel free to contact me Varun Srivastava (varun.srivastava@students.iiserpune.ac.in)
