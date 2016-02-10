import requests
import csv_utf8 as csv
from get_usnews import get_usnews
from get_wikipedia import get_wikipedia
import os.path


# Begin web session
s = requests.Session()

csvExists = os.path.isfile('collegepeople.csv')
if csvExists:
    print('Initial crawl .csv file already exists.')
else:
    print('No crawl .csv file exists. Grabbing initial content...')

    # USNews login credentials
    username = ''
    password = ''
    loginData = dict(username=username, password=password)

    # Get list of schools and rankings from USNews website.
    print('Getting schools and rankings from USNews...')

    allSchools, allRanks = get_usnews(s, loginData)

    # Get President and Provost off Wikipedia pages for each school
    print('Getting leadership personnel from Wikipedia...')

    allPeople = get_wikipedia(s, allSchools, allRanks)

    # Sort schools alphabetically
    sortedSchools = allPeople.keys()
    sortedSchools.sort()

    # Output to csv file
    print('Reporting to csv file...')

    with open('collegepeople.csv', 'wb') as csvfile:
        collegeWriter = csv.UnicodeWriter(csvfile, delimiter=',')
        collegeWriter.writerow(['College', 'Rank', 'Title', 'Name'])
        for college in sortedSchools:
            for person in allPeople[college]['People'].keys():
                collegeWriter.writerow([college, allPeople[college]['Rank'], person, allPeople[college]['People'][person]])

    print('Content grab complete.')
