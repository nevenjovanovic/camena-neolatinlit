#!/usr/bin/python

"""getcamena.py: Parse a list of CAMENA htmls, download links ending with .xml."""


__author__ = 'Neven Jovanovic'
__copyright__ = "Neven Jovanovic, Zagreb, Hrvatska"
__credits__ = ["Neven Jovanovic"]
__license__ = "CC-BY"
__version__ = "0.0.2"
__maintainer__ = "Neven Jovanovic"
__email__ = "neven.jovanovic@ffzg.hr"
__status__ = "Prototype"

import urllib2
from bs4 import BeautifulSoup
import urllib
suffix = ".xml";
prefix = "http://www.uni-mannheim.de/mateo";
dots = "../"
# A list of files to be scraped:
popis = ["http://www.uni-mannheim.de/mateo/cera/autoren/baierfj_cera.html",
"http://www.uni-mannheim.de/mateo/cera/autoren/baier_cera.html",
"http://www.uni-mannheim.de/mateo/cera/autoren/bartholin_cera.html"]
for address in popis:
# Use urllib2 to open page    
    req = urllib2.Request(address)
    response = urllib2.urlopen(req)
    html = response.read()
# Use Beautiful Soup to parse HTML    
    soup = BeautifulSoup(html,'lxml')
    links = soup.find_all('a')
    for tag in links:
	link = tag.get('href',None)
        if link is not None:
# Select only links ending in .xml            
            if link.endswith(suffix) and link.startswith(prefix):
                filename=link.split('/')[-1]
                urllib.urlretrieve(link, filename)
# For relative links staring with ../                
            elif link.endswith(suffix) and link.startswith(dots):
                filename=link.split('/')[-1]
                link2="http://www.uni-mannheim.de/mateo/" + link[3:]
                urllib.urlretrieve(link2, filename)
