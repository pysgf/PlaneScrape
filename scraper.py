#!/usr/bin/python

# import modules used here -- sys is a very standard one
import sys
import re
import requests
from BeautifulSoup import BeautifulSoup
from models import *

MAGIC_CARDS_ROOT_URL = 'http://magiccards.info'

def main():
    setup_database()
    cardset_links = get_cardset_links()
    for cardset in cardset_links:
        get_cards_in_set(cardset)
#     session.commit()

def setup_database():
    setup_all()
    create_all()

def get_cardset_links():
    r = requests.get(MAGIC_CARDS_ROOT_URL + '/sitemap.html')
    soup = BeautifulSoup(r.content)
    englishTable = soup.findAll('table')[1]
    set_titles_links = englishTable.findAll('a')
    links_list = [link['href'] for link in set_titles_links]
    return links_list

def get_cards_in_set(cardset_link):
    r = requests.get(MAGIC_CARDS_ROOT_URL + cardset_link)
    print cardset_link
    soup = BeautifulSoup(r.content)
    cardRows = soup.findAll('table')[3].findAll('tr')[1:]
    card_list = [row_to_card(cardRow) for cardRow in cardRows]
    for card in card_list:
        scrape_card_page(card)


def row_to_card(row):
    data = row.findAll('td')
    ctype = str(data[0]).split(' ')
    power, toughness, cardType = None, None, None
    if '/' in str(ctype[-1]):
        # This card has a power & toughness; split it from the type.
        power,toughness = ctype[-1].split('/')
        cardType = ctype[:-1]
    else:
        cardType = ctype

    card = Card(
            name = str(data[1].find(text=True)),
            link = str(data[1].find('a')['href']),
            cardtype = str(cardType),
            cost = str(data[3].find(text=True)),
            rarity = str(data[4].find(text=True)),
            artist = str(data[5].find(text=True)),
            edition = str(data[6].find(text=True)),
            power = power,
            toughness = toughness,
            cardnum = str(data[0].find(text=True))
    )
    print card.name
    return card

def scrape_card_page(card):
    r = requests.get(MAGIC_CARDS_ROOT_URL + card.link)
    soup = BeautifulSoup(r.content)
    print card.name
    card.text = soup.find('p', {"class": "ctext"}).find('b')
    card.flavor_text = soup.find('i')
    card.legalities = soup.find(text=re.compile("Illus\."))
    card.rulings = [legal.find(text=True) for legal in soup.findAll('li', {"class": "legal"})]
    card.image = soup.find(src=re.compile("scans"))['src']

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
