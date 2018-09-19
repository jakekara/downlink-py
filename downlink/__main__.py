from downlink import PageScraper
import argparse
import requests
import os

# ===================================

def main():

    parser = argparse.ArgumentParser(description='Download all the links from a web page.')
    parser.add_argument('url', type=str, help='A valid URL to download links from')
    parser.add_argument('dst', type=str, help='A path to a directory in which to save the files')

    args = parser.parse_args()

    scraper = PageScraper(args.url)

    for link in scraper.get_doc_links():
        url = link[0]
        open(os.path.join(args.dst, PageScraper.file_name(url)),"w")\
            .write(requests.get(url).content)

if __name__ == "__main__":
    main()
