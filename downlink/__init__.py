
from __future__ import print_function
from future.standard_library import install_aliases


install_aliases()
from urllib.parse import urljoin, urlsplit, urlunsplit
from sys import stderr
from bs4 import BeautifulSoup
import requests
from os.path import basename, dirname

def is_valid_url(url_str):
    parts = urlsplit(url_str)
    return len(parts[0]) > 0 and len(parts[1]) > 0

class PageScraper:

    @staticmethod
    def file_name(url):
        """ Get the file name from a link """
        return basename(url)

    def full_url(self, link_url):
        if is_valid_url(link_url):
            return link_url
        try:
            return urljoin(str(self.base_url),str(link_url))
        except Exception as e:
            print("Error creating url from parts (%s, %s): %s" % (str(self.base_url),str(link_url),str(e)),  file=stderr)
            return None
                     
    def parse_link(self, link):
        return (self.full_url(link["href"]),link.text)

    def get_doc_links(self, ext=None):
        if ext is None:
            ext = self.ext
        links = self.get_clean_file_links()
        return [x for x in links if x[0].upper().endswith(ext.upper())]

    def get_clean_file_links(self):
        return [self.parse_link(x) for x in self.get_links()]

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

        url_parts = urlsplit(self.url)
        self.base_url = urlunsplit((
            url_parts.scheme,
            url_parts.netloc,
            dirname(url_parts.path),
            "",
            ""
            ))
        self.ext = ext
