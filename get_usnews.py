from bs4 import BeautifulSoup
import re


# Logs into USNews and scrapes school and ranking data from their annual list
def get_usnews(s, loginData):

    # URL and credential information.
    usNewsURL = 'http://premium.usnews.com'
    usNewsRankingsURL = 'http://premium.usnews.com/best-colleges/rankings/national-universities'
    usNewsLoginURL = 'https://secure.usnews.com/member/login?ref=http%3A%2F%2Fpremium.usnews.com%2Fbest-colleges%2Frankings%2Fnational-universities'

    # Login and get first web page.
    s.get(usNewsLoginURL)
    s.post(usNewsLoginURL, data=loginData)
    page = s.get(usNewsRankingsURL)

    # Parse web tags to get Schools and Ranks.
    soup = BeautifulSoup(page.content, 'lxml')
    schools = soup.find_all('a', class_='school-name')
    allSchools = [x.get_text() for x in schools]

    ranks = soup.find_all('span', class_='rankscore-bronze cluetip cluetip-stylized')
    allRanks = [x.get_text() for x in ranks]

    # Look for 'next page' link. Loop through all pages until link no longer found.
    while True:
        try:
            nextPageLink = soup.find('a', text=re.compile('Next'))['href']
        except TypeError:
            break

        # Get URL for next page.
        nextPageURL = usNewsURL + nextPageLink
        page = s.get(nextPageURL)
        soup = BeautifulSoup(page.content, 'lxml')

        # Parse web tags for Schools and Ranks.
        schools = soup.find_all('a', class_='school-name')
        schools = [x.get_text() for x in schools]
        allSchools = allSchools + schools

        # Accumulate information.
        ranks = soup.find_all('span', class_='rankscore-bronze cluetip cluetip-stylized')
        ranks = [x.get_text() for x in ranks]
        allRanks = allRanks + ranks
        ranks = soup.find_all('span', class_='rankscore-bronze cluetip cluetip-stylized rankscore-grayedout')
        ranks = [x.get_text() for x in ranks]
        allRanks = allRanks + ranks

    # Formatting.
    allRanks = [x.replace('#', '') for x in allRanks]
    allRanks = [u'RNP' if x == u'\n                RNP\n                \n            ' else x for x in allRanks]
    allRanks = [u'Unranked' if x == u'\n                Unranked\n            ' else x for x in allRanks]

    return allSchools, allRanks
