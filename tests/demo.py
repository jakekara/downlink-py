import os, requests
from dl_docs import PageScraper

# url = "https://data.ct.gov/Health-and-Human-Services/DSS-Program-Participation-by-Month-2016-2018/sx77-vjbh"
url = "https://www.ct.gov/doh/cwp/view.asp?a=4513&q=530462"
base_url = "https://www.ct.gov/doh/cwp/"

scraper = PageScraper(url)

links = scraper.get_doc_links()

for link in links:
    url = urljoin(base_url,link[0])
    fname = PageScraper.file_name(url)
    dst = os.path.join("out", fname)
    print ("Downloading %s" % (fname))

    file_contents = requests.get(url).content
    
    open(dst, "wb").write(file_contents)


