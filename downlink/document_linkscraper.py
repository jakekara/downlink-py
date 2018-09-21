from .linkscraper import LinkScraper

class DocumentLinkScraper(LinkScraper):

    """ Scrape "document" links, links that end in a given file extension """

    def filter_links(self, link):

        """ Override to filter out non-document links """
        
        return link["href"].upper().endswith(self.ext.upper())

    def __init__(self, url, ext="pdf", *args, **kwargs):

        super(DocumentLinkScraper, self).__init__(url, *args, **kwargs)

        self.ext = "pdf"

