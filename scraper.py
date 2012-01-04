#!/usr/bin/python

# import modules used here -- sys is a very standard one
import sys
import requests
from BeautifulSoup import BeautifulSoup

# Gather our code in a main() function
def main():
    cardset_links = get_links()
    
#     for cardset in cardset_links:


def get_links():
    r = requests.get('http://magiccards.info/sitemap.html')
    soup = BeautifulSoup(r.contents)
    englishTable = soup.findAll('table')[1]
    set_titles_links = englishTable.findAll('a')
    links_list = [link['href'] for link in set_titles_links]
    return links_list


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
