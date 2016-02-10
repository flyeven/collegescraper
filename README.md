# collegescraper
Scrape USNews and Wikipedia for leadership personnel of top-ranked US Colleges in Python 2.7.11

This is a simple demonstration of data acquisition through scraping information from web pages.

This python code scrapes USNews pages for the top ranked Colleges and Universities in the US. The script then scrapes Wikipedia for leadership information for each of the schools from the USNews list. The School, Rank, Position, and Name of the personnel are saved in a unicode compatible .csv file

Dependencies:

* Python 2.7.11
* bs4 (aka BeautifulSoup4 4.4.1) - for parsing web pages
* csv_utf8 - a csv reader/writer which allows utf8 encoding (uses csv, codecs, cStringIO)
* lxml (3.4.4) - for processing xml/html
* re - regex package for python
* requests (2.9.1) - for creating a web session which allows browsing and crawling web pages
* wikipedia (1.4.0) - small package for crawling wikipedia pages

Note: USNews data requires login credentials.
