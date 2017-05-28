#!/bin/env python3

import sys, os, argparse, textwrap
from getters import *

def main():
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
    parser.add_argument("-e", "--engine", metavar="NAME_OF_ENGINE", type=str, help="method of downloading books")
    parser.add_argument("-c", "--cse-id", metavar="CSE_ID", type=str, help="custom cse id for google")
    parser.add_argument("-a", "--api-key", metavar="API_KEY", type=str, help="custom api key for google")
    parser.add_argument("-d", "--dir", metavar="DIR", type=str, help="dir to download books", default = os.getcwd())

    args = parser.parse_args()

if __name__ == "__main__":
    try: 
        main()
    except KeyboardInterrupt:
        print("Interrupted by user...")
        sys.exit()
