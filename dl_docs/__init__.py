from bs4 import BeautifulSoup
import requests
from os.path import basename

class PageScraper:

    @staticmethod
    def file_name(url):
        """ Get the file name from a link """
        
        return basename(url)
    
    @staticmethod
    def parse_link(link):
        return (link["href"], link.text)

    def get_doc_links(self, ext=None):
        if ext is None:
            ext = self.ext
        links = self.get_clean_file_links()
        return [x for x in links if x[0].upper().endswith(ext.upper())]

    def get_clean_file_links(self):
        return [PageScraper.parse_link(x) for x in self.get_links()]

    def get_file_links(self):
        return self.get_links()

    def get_links(self):
        if not hasattr(self, "links"):
            self.links = self.get_soup().find_all("a",href=True)
        return self.links

    def get_soup(self):
        if not hasattr(self,"soup"):
            self.soup = BeautifulSoup(self.get_html(), "html.parser")
        return self.soup

    def get_html(self):
        if not hasattr(self, "html"):
            resp = requests.get(self.url)
            if resp.status_code != 200:
                raise Exception("Error loading HTML:" + str(resp.status))
            self.html = resp.content
            
        return self.html
        

    def __init__(self, url, ext="pdf"):
        self.url = url
        self.ext = ext
