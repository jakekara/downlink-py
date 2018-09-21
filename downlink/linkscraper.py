from __future__ import print_function

try:
    from future.standard_library import install_aliases
except:
    pass
    

install_aliases()
from urllib.parse import urljoin, urlsplit, urlunsplit
from sys import stderr
from bs4 import BeautifulSoup
import requests
from os.path import basename, dirname

class LinkScraper(object):

    """ Scrape links from an HTML page  """

    @staticmethod
    def is_valid_url(url_str):
        parts = urlsplit(url_str)
        return len(parts[0]) > 0 and len(parts[1]) > 0

    # @staticmethod
    # def file_name(url):
    #     """ Get the file name from a link """
    #     return basename(url)

    def full_url(self, link_url):
        if LinkScraper.is_valid_url(link_url):
            return link_url
        try:
            return urljoin(str(self.base_url),str(link_url))
        except Exception as e:
            print("Error creating url from parts (%s, %s): %s" % (str(self.base_url),str(link_url),str(e)),  file=stderr)
            return None
                     
    # def parse_link(self, link):
    #     return (self.full_url(link["href"]),link.text)

    def filter_links(self, link):
        """ Should the link tuple be included in the output? Default to yes """
        return True
        
    # def get_clean_file_links(self):
    #     return [self.parse_link(x) for x in self.get_links()]

    def get_all_links(self, href=True):
        if not hasattr(self, "all_links"):        
            self.all_links = self.get_soup().find_all("a",href=href)
        return self.all_links
        

    def get_links(self, href=True):

        """ Returns iterable of  bs4 tag objects """
        
        if not hasattr(self, "links"):
            self.links = filter(
                self.filter_links,
                self.get_all_links(href=href))

        # return filter(self.links, self.filter_links)
        return self.links

    def get_soup(self):
        if not hasattr(self,"soup"):
            self.soup = BeautifulSoup(self.get_html(), "html.parser")
        return self.soup

    @staticmethod
    def get_base_url(url):
        url_parts = urlsplit(url)

        return urlunsplit((
            url_parts.scheme,
            url_parts.netloc,
            dirname(url_parts.path),
            "",
            ""
            ))

    def get_html(self):
        if not hasattr(self, "html"):
            resp = requests.get(self.url)
            if resp.status_code != 200:
                raise Exception("Error loading HTML:" + str(resp.status))
            self.html = resp.content
            
        return self.html

    def __init__(self, url,
                 # ext="pdf",
                 html=None):
        self.url = url

        self.base_url = LinkScraper.get_base_url(self.url)
        
        # self.ext = ext

        # bypass need to make requests
        if html is not None:
            self.html = html


