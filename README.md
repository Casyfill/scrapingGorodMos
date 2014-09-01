Scraping problems of Moscow
=====================
###from **gorod.mos.ru** govermental crowdsourcing platform

Platform is pretty hard to scrape, so after several experiments with *scraper-wiki* and *Kimono* I decided to write my own parser. It uses selenium web-browsing library for python to camouflage script as a common browser.

I. First step of scraping is getting all regions and zones ID. Zone ID's were scraped manually, there is just 5 of them:
script: *regions_scraper.py*  
data: *regions_indexes.csv*

II. (done) Scraping problem counters by type in each region

III. (toDo) group properties

IV. (toDo) Scraping each problem by region.



