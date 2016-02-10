import re
import wikipedia
from bs4 import BeautifulSoup


# Accepts list of schools and ranks to search Wikipedia and a requests.session for browsing
def get_wikipedia(s, allSchools, allRanks):

    # Initialize data set
    allPeople = {}

    # Track pages which aren't found on Wikipedia (for troubleshooting).
    pageNotFound = []

    for school, rank in zip(allSchools, allRanks):
        # Defaults for positions
        chairman = []
        chancellor = []
        president = []
        provost = []

        # Try to find Wikipedia page (some special cases). If not found move to next school.
        try:
            wikiURL = wikipedia.page(school).url
        except:
            if school == u'Brigham Young University--Provo':
                wikiURL = wikipedia.page('Brigham Young University').url
            elif school == u'University of the Pacific':
                wikiURL = wikipedia.page('University of the Pacific (United States)').url
            elif school == u'University of St. Thomas':
                wikiURL = wikipedia.page('University of St. Thomas (Minnesota)').url
            elif school == u'Rutgers, The State University of New Jersey--Newark':
                wikiURL = wikipedia.page('Rutgers University').url
            elif school == u"St. John's University":
                wikiURL = wikipedia.page(u"St. John's University (New York City)").url
            else:
                schoolInfo = {'Rank': rank, 'Chairman': chairman, 'Chancellor': chancellor, 'President': president,
                              'Provost': provost}
                allPeople.update({school: schoolInfo})
                pageNotFound.append(school)
                continue

        # Pull page
        page = s.get(wikiURL)
        soup = BeautifulSoup(page.content, 'lxml')

        # Try to find as much leadership information as possible
        try:
            chairman = soup.find('table', class_='infobox vcard').find('th', text='Chairman').find_next_sibling().\
                get_text()
        except:
            chairman = []

        try:
            chancellor = soup.find('table', class_='infobox vcard').find('th', text='Chancellor').find_next_sibling().\
                get_text()
        except:
            chancellor = []

        try:
            president = soup.find('table', class_='infobox vcard').find('th', text='President').find_next_sibling().\
                get_text()
        except:
            president = []

        try:
            provost = soup.find('table', class_='infobox vcard').find('th', text='Provost').find_next_sibling().\
                get_text()
        except:
            provost = []

        # Package information.
        peopleInfo = {'Chairman': chairman, 'Chancellor': chancellor, 'President': president,
                      'Provost': provost}
        # Remove Wikipedia citations. Format
        peopleInfo = {x: re.sub('\[*.\]', '', peopleInfo[x]) for x in peopleInfo if peopleInfo[x] != []}
        peopleInfo = {x: re.sub('\n', ' ', peopleInfo[x]) for x in peopleInfo if peopleInfo[x] != []}

        schoolInfo = {'Rank': rank, 'People': peopleInfo}

        allPeople.update({school: schoolInfo})

    print(pageNotFound if pageNotFound != [] else [])

    return allPeople
