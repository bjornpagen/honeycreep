from googleapiclient.discovery import build


class GoogleCSE:
    def __init__(self, cse_id, api_key, search_term):
        self.cse_id = cse_id
        self.api_key = api_key

    def get(self, search_term):
        return self.get_links(self.pdf_search(search_term))

    def google_search(self, search_term):
        service = build("customsearch", "v1", developerKey=self.api_key)
        res = service.cse().list(q=search_term, cx=self.cse_id).execute()
        return res['items']

    def pdf_search(self, search_term):
        return self.google_search("".join((search_term, " file:pdf")))

    def get_links(books):
        book_links = []
        for book in books:
            if book['link'].endswith('.pdf') and book['fileFormat'] == 'PDF/Adobe Acrobat':
                book_links.append(book['link'])
        return book_links
