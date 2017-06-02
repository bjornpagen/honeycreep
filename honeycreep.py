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

    parser.add_argument("t", metavar="NAME_OF_BOOK", type=str, help="title of the desired book")
    parser.add_argument("-e", "--engine", metavar="NAME_OF_ENGINE", type=str, help="method of downloading books",
                        default="googleCSE")
    parser.add_argument("-c", "--cse-id", metavar="CSE_ID", type=str, help="custom cse id for google")
    parser.add_argument("-a", "--api-key", metavar="API_KEY", type=str, help="custom api key for google")
    parser.add_argument("-d", "--dir", metavar="DIR", type=str, help="dir to download books", default = os.getcwd())

    args = parser.parse_args()

    # create configuration file

    getter = None
    if args.e == "googleCSE":
        getter = google_cse.GoogleCSE(args.c, args.a, args.t)

    def download_file(download_url, pdf_name):
        try:
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
