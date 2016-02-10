# collegescraper
Scrape USNews and Wikipedia for leadership personnel of top-ranked US Colleges in python

This is a simple demonstration of data acquisition through scraping information from web pages.

This python code scrapes USNews pages for the top ranked Colleges and Universities in the US. The script then scrapes Wikipedia for leadership information for each of the schools from the USNews list. The School, Rank, Position, and Name of the personnel are saved in a unicode compatible .csv file

Dependencies:

requests - for creating a web session which allows browsing and crawling web pages
csv_utf8 - a csv reader/writer which allows utf8 encoding (uses csv, codecs, cStringIO)
bs4 (aka BeautifulSoup) - for parsing web pages
re - regex package for python
wikipedia - small package for crawling wikipedia pages

Note: USNews data requires login credentials.
