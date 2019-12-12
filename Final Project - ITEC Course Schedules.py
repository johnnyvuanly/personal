''''' Pre Project Notes

Write a program that reads the MCTC "Course Search Results" page, parses that page and creates a spreadsheet containing 7 columns
1. ID Number (ie. 000096)
2. Course Number (ie. 1150-61)
3. Course Title (ie. Programming Logic and Design)
4. Day of the week (ie. Wednesday)
5. Time the course meet (ie. 9:00am - 11:59am)
6. The credits for the course
7. The instructor'''

import requests # requests module lets you easily download files from the Web
from bs4 import BeautifulSoup # Had to install beautifulsoup4 or bs4 which allows me to extract information from an HTML page

# Request the URL we want to work with
page = requests.get('https://eservices.minnstate.edu/registration/search/advancedSubmit.html?campusid=305&searchrcid'
                    '=0305&searchcampusid=305&yrtr=20205&subject=ITEC&courseNumber=&courseId=&openValue'
                    '=OPEN_PLUS_WAITLIST&delivery=ALL&showAdvanced=&starttime=&endtime=&mntransfer=&credittype=ALL'
                    '&credits=&instructor=&keyword=&begindate=&site=&resultNumber=250')

try:
    page.raise_for_status()  # Checks to see if there was an error downloading the file and will do nothing if it succeeded
except Exception as exc:
    print('There was a problem: %s' % (exc))


# Creates a beautiful soup object from the request above.
soup = BeautifulSoup(page.content, 'html.parser')
type(soup)

print(soup)