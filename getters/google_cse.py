from googleapiclient.discovery import build


class GoogleCSE:
    def __init__(self, cse_id, api_key, search_term):
        self.cse_id = cse_id
        self.api_key = api_key
        self.search_term = search_term
        self.bookdump = []

    def google_search(self, search_term):
        service = build("customsearch", "v1", developerKey=self.api_key)
        res = service.cse().list(q=search_term, cx=self.cse_id).execute()
        return res['items']

    def get_google_dump(self):
        self.bookdump =  self.google_search("".join((self.search_term, " file:pdf")))

    def get(self):
        return_books = []
        for book in self.bookdump:
            if book['link'].endswith('.pdf') and book['fileFormat'] == 'PDF/Adobe Acrobat':
                return_books.append((book['title'],book['link']))
        return return_books
