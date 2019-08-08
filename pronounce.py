"""
Author: David Foalrin
Version: 3.6+
"""

import argparse
import requests
from bs4 import BeautifulSoup

def get_word():
    """ Returns command line argument corresponding to word to get pronounciation for
    """
    parser = argparse.ArgumentParser(description="Get pronounciation audio file for a word.")
    parser.add_argument("word", help="word to get pronounciation for")
    args = parser.parse_args()
    return args.word

def save_french_pronounciation(word):
    """ Saves the pronounciation audio file for a french word to the current directory
    """
    html_parser = "html.parser"
    url = "https://en.wiktionary.org/wiki/File:Fr-{}.ogg".format(word)
    web_request = requests.get(url)
    soup = BeautifulSoup(web_request.text, html_parser)
    media_div = soup.find("div", class_="fullMedia")
    media_url = media_div.p.a["href"]
    media_title = media_div.p.a["title"]
    media_request = requests.get("https:" + media_url, allow_redirects=True)

    with open(media_title, "wb") as media_file:
        media_file.write(media_request.content)


if __name__ == "__main__":
    save_french_pronounciation(get_word())
