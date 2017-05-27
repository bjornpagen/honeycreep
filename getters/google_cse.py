from googleapiclient.discovery import build
from urllib.request import urlopen
import urllib

class GoogleCSE:

    def __init__(self,

    def google_search(search_term, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        return res['items']

    def pdf_search(search_term):
        return google_search("".join((search_term, " file:pdf")))

    def pdf_shear(books): 
        newbooks = []
        for book in books:
            if book['link'].endswith('.pdf') and book['fileFormat'] == 'PDF/Adobe Acrobat':
                newbooks.append(book)
        return newbooks

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

    def bunch_download(search_term):
        print('Chdir to /home/' + getpass.getuser() + '/Documents/books...')
        os.chdir('/home/' + getpass.getuser() + '/Documents/books')
        print('Searching for books...')
        books = pdf_search(search_term, num=10)
        print('Weeding out the baddies...')
        books = pdf_shear(books)
        print('Downloading ' + str(len(books)) + ' books...')
        for book in books:
            print('Downloading ' + book['title'] + '...')
            download_file(book['link'], book['title'])
