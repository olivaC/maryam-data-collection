#!/usr/bin/env python3
from bs4 import BeautifulSoup

import urllib.request
import re


def generate_names(url):
    """
    This function will write to a .txt file a list of researchers names in the <h3> tag.
    This is custom made to work for the Program Committee ISSTA 2018 Technical Papers.

    :param url: The URL containing a webpage of researchers
    :return: None
    """
    soup = BeautifulSoup(urllib.request.urlopen(url), "html.parser")
    headings = soup.find_all(["h3"])
    file = open("association_names.txt", "a")
    index = 1
    for i in headings:
        i = str(i)
        if i.startswith('<h3 class="media-heading'):
            result = re.search('<h3 class="media-heading">(.*) <small>', i)
            file.write("{} R{}\n".format(result.group(1), index))
            index += 1


def main():
    url = input("Enter in URL: ")
    generate_names(url)


if __name__ == "__main__":
    main()
