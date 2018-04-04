#!/usr/bin/env python3
from bs4 import BeautifulSoup

import codecs
import os
import sys


def generate_titles(html_file, profile, ind):
    """
    This function is used to create R_Papers as well as add to the association_names file. It is also used to create
    a new Reviewer profile.

    :param html_file: The html file of the person
    :param profile: The profile number (e.g. R1)
    :param ind: the index to use for file numbers
    :return: None
    """
    r_path = '/Users/Carlo/Work/maryam-data-collection/R_Papers'
    a_path = '/Users/Carlo/Work/maryam-data-collection/'
    rev_path = '/Users/Carlo/Work/maryam-data-collection/Reviewers'
    a_name = os.path.join(a_path, 'associative.txt')
    rev_name = os.path.join(rev_path, '{}.txt'.format(profile))
    file = codecs.open(html_file, 'r')
    associative_file = open(a_name, "a")
    rev_file = open(rev_name, "a")
    soup = BeautifulSoup(file, "html.parser")
    headings = soup.find_all('tr', {'class': 'gsc_a_tr'})
    index = int(ind)
    for i in headings:
        x = BeautifulSoup(str(i), "html.parser")
        y = x.find_all('span', {'class': 'gsc_a_h gsc_a_hc gs_ibl'})
        z = x.find_all('a', {'class': 'gsc_a_at'})

        for k in y:
            if k.text and 2008 <= int(k.text) <= 2018:
                for j in z:
                    associative_file.write("{},P{}\n".format(profile, index))
                    filename = os.path.join(r_path, 'P{}.txt'.format(index))
                    papers = open(filename, 'a')
                    papers.write("{}".format(j.text))
                    papers.close()
                    rev_file.write("{}\n\n".format(j.text))
                    index = index + 1
    last = os.path.join(a_path, 'last_file.txt')
    last_file = open(last, "a")
    last_file.write("Index to start: {}\n".format(index))
    rev_file.close()
    last_file.close()



def main():
    file = sys.argv[1]
    reviewer = sys.argv[2]
    index = sys.argv[3]
    generate_titles(file, reviewer, index)
    print("Done...")


if __name__ == "__main__":
    main()
