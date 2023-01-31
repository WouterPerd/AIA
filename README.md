# OntologyDownload.sh:
Run it in the terminal with validate.java (download from PieterRuanCronje github) and it will download all namespace
URI's. It will then convert all turtle formatted data into triples and save them in the corresponding text files.
The argument for validate.javamust be manually put in in line 4 of OntologyDownload.sh.

# CDM_Scraper.py:
Used to web scrape data from projects in the CDM registry. Run program with one argument which is the URL of the CDM project you want to scrape. Currently incomplete,
the comments in the python file specify what still needs to be added and fixed.
