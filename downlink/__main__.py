""" CLI tool for downloading documents from a web page """

from . import DocumentLinkScraper
import argparse
import requests
import os

def main():

    parser = argparse.ArgumentParser(
        description='Download all the links of a given file extension from a web page.')
    parser.add_argument('url', type=str, help='A valid URL to download links from')
    parser.add_argument('dst', type=str, help='A path to a directory in which to save the files')
    parser.add_argument('--ext',
                        type=str,
                        default="pdf",
                        help='the file extension/type of file to download')    

    args = parser.parse_args()

    scraper = DocumentLinkScraper(args.url, ext=args.ext)

    # for link in scraper.get_doc_links():
    for link in scraper.get_links():
        print (link["href"], scraper.full_url(link["href"]), link.text)
        # url = link[0]
        open(os.path.join(args.dst, os.path.basename(link["href"])),"wb")\
            .write(requests.get(scraper.full_url(link["href"])).content)

if __name__ == "__main__":
    main()
