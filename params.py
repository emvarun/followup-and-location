import os
from Observatory import ObsDetail
#################################### EDIT-DATE ##########################################
#Location of all the fits file downloaded 
rootdir = '/home/varun/IUCAA/O2-Analysis/Sky_Patch/EM-Analysis-Patch/All-2015'
#Suffix the modified patches with:
suffix2ModDateFits = 'O1-Dates'
# The location where the files with modified days are saved. 
folddir = '/home/varun/IUCAA/O2-Analysis/Sky_Patch/Mod-Dates/O1-Period'
if not os.path.exists(folddir):
	os.makedirs(folddir)

#################################### LOCATIONS ##########################################
Observatory_Locations = ObsDetail()

############################## SKY PATCH AND LOOP SKY PATCH #############################
# Texp is how many hours after the trigger one could possibly followup
Texp = 24
# stepsize: Time in seconds after which the sky is considered. Ie after every 10 mins we
#	consider the realization how much has the patch set or risen.
stepsize = 600
# The list of Observatory location one wants to analyse
obsName = Observatory_Locations.keys()
# The list of square degrees of capability you wish to empower each location with
# CAUTION: Please ensure these numbers are in ascending order
NsqDeg = [ 1., 3., 10., 30., 100., 300. ]

################################## Coverage Analysis ####################################
# Location_Datafiles is the desired location for saving the output text files
Location_Datafiles = '/home/varun/IUCAA/O2-Analysis/Sky_Patch/followup-and-location'
if not os.path.exists(Location_Datafiles):
	os.makedirs(Location_Datafiles)
# The prefixed name of the output file containing the probability covered for the various 
# N square degrees considered. The actual-file will follow the name of observatory  under
# consideraton 
outfile = os.path.join(Location_Datafiles, 'O1-Summary') 

# Color coding for the different boxplots
boxColors = []
for i in obsName:
	boxColors.append(Observatory_Locations[i].color)

# Sub-titles in the box plots
SubplotTitle = []
for i in NsqDeg:
	SubplotTitle.append( str(i) + ' Square Degrees')

# Y-axis limits of each of the subplots
yaxisTop = [0.015, 0.05, 0.15, 0.4, 0.8, 1.0]
yaxisBottom = 0.

# BoxplotFile: The file name which contains the plots. This file is returned in the same 
#	folder which contains the code.
BoxplotFile = 'test.pdf'

# For Plots : 
#	Ndets: If  one  wishes  to  analyse  only  events with two detectors say ndets = 2 and 
#	IfAllNDet = False. IfAllNDet = True analyses and plots all the events  irrespective of 
#	number of detectors involved. If PeriodComb is set True when can study the events in a 
#	smaller window of time of the year. The period variable defines this period of interest.
Ndets = 2
IfAllNDet = False
Period = 'Sep'
PeriodComb = False
