# Max Wagner
# Not overly complicated, but I think it does the job just fine for a wikipedia page.
# I played with being more specific when grabbing text from the page, but in this form it should analyze any page.

from bs4 import BeautifulSoup
from alchemyapi import AlchemyAPI
import urllib


# Load some raw html, and grab the text from it with urllib and bs4
def getSoup():
    sock = urllib.urlopen('https://en.wikipedia.org/wiki/Motocross')
    sockRaw = sock.read()
    soup = BeautifulSoup(sockRaw, "html.parser")
    soupText = soup.get_text()

# use the alchemyAPI to find the keyword/phrases from the texts
    alchemyapi = AlchemyAPI()
    response = alchemyapi.keywords('text', soupText, {'maxRetrieve': 10})
    if response['status'] == 'OK':
        print "\nThe Keywords are:"
        for i in response['keywords']:
            print "Word: " + i["text"] + ", Relevance: " + i["relevance"]
    else:
        print "Something went wrong with Alchemy."


if __name__ == "__main__":
    getSoup()