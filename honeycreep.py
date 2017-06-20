#!/bin/env python3

import sys, os, argparse, textwrap, configparser
from urllib.request import urlopen
from getters import google_cse

def main():
    # TODO: implement ConfigParser and make it generally work

    title = None
    engine = "googleCSE"
    cse_id = ""

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''
            honeycreep
            ----------------------------------------------------------
                A proof-of-concept ebook downloading script
        '''),
        epilog=textwrap.dedent('''
        "The only way to deal with an unfree world is to become so absolutely
        free that your very existence is an act of rebellion." - Albert Camus
            -created by bjornpagenatgmaildotcom
        ''')
    )
    
    parser.add_argument("t", metavar="NAME_OF_BOOK", type=str,
            help="title of the desired book")
    parser.add_argument("-d", "--dir", metavar="DIR", type=str,
            help="dir to download books", default = os.getcwd())

    group_google_cse = parser.add_argument_group()
    group_google_cse.add_argument("c", metavar="CSE_ID",
            type=str, help="custom cse id for google")
    group_google_cse.add_argument("a", metavar="API_KEY",
            type=str, help="custom api key for google")

    args = parser.parse_args()

    # create/read from configuration file

    getter = google_cse.GoogleCSE(args.c, args.a, args.t)
    getter.get_google_dump()
    book_list = getter.get()

    for book in book_list:
        print("hi")
        download_file(book[0],book[1])

def download_file(pdf_name, download_url):
    try:
        print("Downloading " + pdf_name)
        web_file = urlopen(download_url)
        local_file = open(pdf_name, 'wb')
        local_file.write(web_file.read())
        web_file.close()
        local_file.close()
    except:
        print("Unable to download file...")
    else:
        print("Success!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user...")
        sys.exit()
