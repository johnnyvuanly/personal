# Pre Project Notes

# Write a program that reads the MCTC "Course Search Results" page, parses that page and creates a spreadsheet containing 7 columns
# 1. ID Number (ie. 000096)
# 2. Course Number (ie. 1150-61)
# 3. Course Title (ie. Programming Logic and Design)
# 4. Day of the week (ie. Wednesday)
# 5. Time the course meet (ie. 9:00am - 11:59am)
# 6. The credits for the course
# 7. The instructor

# Beautiful Soup is a module for extracting information from an HTML page
import beautifulsoup4 as beautifulsoup4

# Used to install Beautiful Soup, Version 4
pip install beautifulsoup4

# To import Beautiful Soup you run import bs4, this parses which analyze and identify the parts of HTML file on the hard drive
import requests, bs4

# Had to install package requests
res = requests.get('https://eservices.minnstate.edu/registration/search/advancedSubmit.html?campusid=305&searchrcid=0305&searchcampusid=305&yrtr=20205&subject=ITEC&courseNumber=&courseId=&openValue=OPEN_PLUS_WAITLIST&delivery=ALL&showAdvanced=&starttime=&endtime=&mntransfer=&credittype=ALL&credits=&instructor=&keyword=&begindate=&site=&resultNumber=250')

