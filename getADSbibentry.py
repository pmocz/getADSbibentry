import sys, getopt
import requests
import urllib.request
import time
from bs4 import BeautifulSoup


def main(argv):
  inputtags = sys.argv[1]
   
  # loop over cite tags
  for tag in inputtags.split(','):
    
    # set URL and connect
    url = 'https://ui.adsabs.harvard.edu/abs/' + tag + '/exportcitation'
    response = requests.get(url)
    
    # parse HTML 
    soup = BeautifulSoup(response.text, "html.parser")
    
    # export
    export_text = soup.findAll('textarea')[0].contents[0]
    
    sys.stdout.write(export_text)

if __name__ == "__main__":
   main(sys.argv[1:])

    


