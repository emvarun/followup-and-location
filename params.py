import os
from Observatory import ObsDetail
#################################### EDIT-DATE ##########################################
#Location of all the fits file
rootdir = '/home/varun/IUCAA/O2-Analysis/Sky_Patch/EM-Analysis-Patch/All-2015'
#Suffix the modified patches with:
suffix2ModDateFits = 'Mod-Date'

#################################### LOCATIONS ##########################################
Observatory_Locations = ObsDetail()
############################## SKY PATCH AND LOOP SKY PATCH #############################
# Texp is how many hours after the trigger one could possibly followup
Texp = 24
# The list of Observatory location one wants to analyse
obsName = Observatory_Locations.keys()
# The list of square degrees of capability you wish to empower each location with
# CAUTION: Please ensure these numbers are in ascending order
NsqDeg = [ 1., 3., 10., 30., 100., 300. ]
# The location of all the fitsfile which one wishes to consider for analysis
folddir = '/home/varun/IUCAA/O2-Analysis/Sky_Patch/EM-Analysis-Patch/All-2015'
# The prefixed name of the output file containing the probability covered for the various 
# N square degrees considered. The actual-file will follow the name of observatory under
# consideraton

################################## Coverage Analysis ####################################
# Location_Datafiles is the desired location for saving the output text files
Location_Datafiles = '/home/varun/IUCAA/O2-Analysis/Sky_Patch/followup-and-location'
outfile = os.path.join(Location_Datafiles, 'Summary')

# Color coding for the different boxplots
boxColors = ['RoyalBlue', 'Orange', 'RoyalBlue', 'deepskyblue', 'deepskyblue', 'deepskyblue', 'deepskyblue', 
						 'Red', 'Red', 'darkgoldenrod', 'Lime', 'Red', 'Lime']

SubplotTitle = [ '1 sq. degrees', '3 sq. degrees', '10 sq. degrees', '30 sq. degrees', '100 sq. degrees', '300 sq. degrees' ]

# Y-axis limits of each of the subplots
yaxisTop = [0.015, 0.05, 0.15, 0.4, 0.8, 1.0]
yaxisBottom = 0.

# For Plots : 
#	Ndets: If one wishes to analyse only events with two detectors say ndets = 2 and IfAllNDet = False.
# IfAllNDet = True analyses and plots all the events irrespective of number of detectors involved.
#	If PeriodComb is set True when can study the events in a smaller window of time of the year. The
# Period variable defines this period of interest
Ndets = 2
IfAllNDet = False
Period = 'Sep'
PeriodComb = False
