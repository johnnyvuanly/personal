''''' Pre Project Notes

Write a program that reads the MCTC "Course Search Results" page, parses that page and creates a spreadsheet containing 7 columns
1. ID Number (ie. 000096)
2. Course Number (ie. 1150-61)
3. Course Title (ie. Programming Logic and Design)
4. Day of the week (ie. Wednesday)
5. Time the course meet (ie. 9:00am - 11:59am)
6. The credits for the course
7. The instructor'''

# requests module lets you easily download files from the Web
import requests
# Had to install beautifulsoup4 or bs4 which allows me to extract information from an HTML page
from bs4 import BeautifulSoup

# Request the URL we want to work with
res = requests.get('https://eservices.minnstate.edu/registration/search/advancedSubmit.html?campusid=305&searchrcid'
                    '=0305&searchcampusid=305&yrtr=20205&subject=ITEC&courseNumber=&courseId=&openValue'
                    '=OPEN_PLUS_WAITLIST&delivery=ALL&showAdvanced=&starttime=&endtime=&mntransfer=&credittype=ALL'
                    '&credits=&instructor=&keyword=&begindate=&site=&resultNumber=250')
try:
    # raise_for_status raises an exception if there was an error downloading the file and will do nothing if the
    # download succeeded
    res.raise_for_status()
except Exception as exc:
    # prints this statement if download failed "There was a problem: 404 Client Error: Not Found"
    print('There was a problem: %s' % (exc))

# Creates a beautiful soup object that is stored in the variable soup
soup = BeautifulSoup(res.content, 'html.parser')

# grab the table of web page and use the data within it. Inside of <div id="resultsContainer">
tableTag = soup.find(id='resultsTable')


resRows = []
rowTags = tableTag.find_all('tr')
headerTags = rowTags[0].findAll('th')
headers = []
for headerTag in headerTags:
    headers.append(headerTag.text.strip())
#print(headers)
for rowTag in rowTags:
    columnTags = rowTag.findAll('td')
    resCol = []
    for columnTag in columnTags:
        resCol.append(columnTag.text.strip())
    resRows.append(resCol)
#print(resRows)

#[0-"" 1-'ID #', 2-'Subj', 3-'#', 4-'Sec', 5-'Title', 6-'Dates', 7-'Days', 8-'Time', 9-'Cr/Hr',
# 10-'Status', 11-'Instructor', 12-'Delivery Method', 13-'Loc']
colIndices = [1, 3, 5, 7, 8, 9, 11]
listCols = [[], [], [], [], [], [], []]
for rowTag in rowTags[1:]:
    columnTags = rowTag.findAll('td')
    i = 0
    for colIndex in colIndices:
        value = columnTags[colIndex].text.strip().replace('\xa0', ' ').replace('\n', ' ')
        listCols[i].append(value)
        i = i + 1
    #resCol = []
    #for columnTag in columnTags:
    #    resCol.append(columnTag.text.strip())
    #resRows.append(resCol)
print(listCols)


