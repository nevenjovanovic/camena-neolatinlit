#!/usr/bin/python

"""getcamena2.py: Parse a list of CAMENA Thesaurus htmls, write to file only the links ending in .xml."""


__author__ = 'Neven Jovanovic'
__copyright__ = "Neven Jovanovic, Zagreb, Hrvatska"
__credits__ = ["Neven Jovanovic"]
__license__ = "CC-BY"
__version__ = "0.0.1"
__maintainer__ = "Neven Jovanovic"
__email__ = "neven.jovanovic@ffzg.hr"
__status__ = "Prototype"
import os
import urllib2
from bs4 import BeautifulSoup
# We want to get links ending in this:
suffix = ".xml";
prefix = "http://www.uni-mannheim.de/mateo";
dots = "../"
# A list of HTML pages to scrape for links:
popis = ["http://www.uni-mannheim.de/mateo/camena/AUTBIO/pont.html",
"http://www.uni-mannheim.de/mateo/camenaref/adam.html",
"http://www.uni-mannheim.de/mateo/camenaref/alegambe.html",
"http://www.uni-mannheim.de/mateo/camenaref/avity.html",
"http://www.uni-mannheim.de/mateo/camenaref/barth.html",
"http://www.uni-mannheim.de/mateo/camenaref/bartholin1.html",
"http://www.uni-mannheim.de/mateo/camenaref/becmann.html",
"http://www.uni-mannheim.de/mateo/camenaref/bertius1.html",
"http://www.uni-mannheim.de/mateo/camenaref/besold.html",
"http://www.uni-mannheim.de/mateo/camenaref/beyerlinck.html",
"http://www.uni-mannheim.de/mateo/camenaref/beze.html",
"http://www.uni-mannheim.de/mateo/camenaref/blanckaert.html",
"http://www.uni-mannheim.de/mateo/camenaref/borrichius.html",
"http://www.uni-mannheim.de/mateo/camenaref/boschius.html",
"http://www.uni-mannheim.de/mateo/camenaref/calepinus.html",
"http://www.uni-mannheim.de/mateo/camenaref/cartari.html",
"http://www.uni-mannheim.de/mateo/camenaref/cluever.html",
"http://www.uni-mannheim.de/mateo/camenaref/cmh/cmh.html",
"http://www.uni-mannheim.de/mateo/camenaref/comenius.html",
"http://www.uni-mannheim.de/mateo/camenaref/crell.html",
"http://www.uni-mannheim.de/mateo/camenaref/dausque.html",
"http://www.uni-mannheim.de/mateo/camenaref/declarationes.html",
"http://www.uni-mannheim.de/mateo/camenaref/ducange.html",
"http://www.uni-mannheim.de/mateo/camenaref/dupuy.html",
"http://www.uni-mannheim.de/mateo/camenaref/estienne_ref.html",
"http://www.uni-mannheim.de/mateo/camenaref/exner.html",
"http://www.uni-mannheim.de/mateo/camenaref/gesner.html",
"http://www.uni-mannheim.de/mateo/camenaref/gesner2.html",
"http://www.uni-mannheim.de/mateo/camenaref/giovio1.html",
"http://www.uni-mannheim.de/mateo/camenaref/giovio2.html",
"http://www.uni-mannheim.de/mateo/camenaref/gruterus.html",
"http://www.uni-mannheim.de/mateo/camenaref/hackspan.html",
"http://www.uni-mannheim.de/mateo/camenaref/hofmann.html",
"http://www.uni-mannheim.de/mateo/camenaref/hondorff.html",
"http://www.uni-mannheim.de/mateo/camenaref/imperiali.html",
"http://www.uni-mannheim.de/mateo/camenaref/jonston.html",
"http://www.uni-mannheim.de/mateo/camenaref/jonston.html",
"http://www.uni-mannheim.de/mateo/camenaref/jonston.html",
"http://www.uni-mannheim.de/mateo/camenaref/jonston.html",
"http://www.uni-mannheim.de/mateo/camenaref/jonston.html",
"http://www.uni-mannheim.de/mateo/camenaref/junus.html",
"http://www.uni-mannheim.de/mateo/camenaref/kahl.html",
"http://www.uni-mannheim.de/mateo/camenaref/kirsch.html",
"http://www.uni-mannheim.de/mateo/camenaref/koenig.html",
"http://www.uni-mannheim.de/mateo/camenaref/lauterbach.html",
"http://www.uni-mannheim.de/mateo/camenaref/leiden.html",
"http://www.uni-mannheim.de/mateo/camenaref/lonitzer.html",
"http://www.uni-mannheim.de/mateo/camenaref/lotichius.html",
"http://www.uni-mannheim.de/mateo/camenaref/lycosthenes.html",
"http://www.uni-mannheim.de/mateo/camenaref/magirus.html",
"http://www.uni-mannheim.de/mateo/camenaref/magri.html",
"http://www.uni-mannheim.de/mateo/camenaref/manuzio.html",
"http://www.uni-mannheim.de/mateo/camenaref/masen1.html",
"http://www.uni-mannheim.de/mateo/camenaref/masen4.html",
"http://www.uni-mannheim.de/mateo/camenaref/masen5.html",
"http://www.uni-mannheim.de/mateo/camenaref/masen6.html",
"http://www.uni-mannheim.de/mateo/camenaref/masen7.html",
"http://www.uni-mannheim.de/mateo/camenaref/masen8.html",
"http://www.uni-mannheim.de/mateo/camenaref/masen9.html",
"http://www.uni-mannheim.de/mateo/camenaref/micraelius.html",
"http://www.uni-mannheim.de/mateo/camenaref/muliers.html",
"http://www.uni-mannheim.de/mateo/camenaref/nolte.html",
"http://www.uni-mannheim.de/mateo/camenaref/pena.html",
"http://www.uni-mannheim.de/mateo/camenaref/pexenfelder.html",
"http://www.uni-mannheim.de/mateo/camenaref/piccart.html",
"http://www.uni-mannheim.de/mateo/camenaref/ravisius.html",
"http://www.uni-mannheim.de/mateo/camenaref/reusner1.html",
"http://www.uni-mannheim.de/mateo/camenaref/rossi.html",
"http://www.uni-mannheim.de/mateo/camenaref/sanson.html",
"http://www.uni-mannheim.de/mateo/camenaref/sanson.html",
"http://www.uni-mannheim.de/mateo/camenaref/sanson.html",
"http://www.uni-mannheim.de/mateo/camenaref/sanson.html",
"http://www.uni-mannheim.de/mateo/camenaref/scarlattini.html",
"http://www.uni-mannheim.de/mateo/camenaref/schott.html",
"http://www.uni-mannheim.de/mateo/camenaref/schurzfleisch.html",
"http://www.uni-mannheim.de/mateo/camenaref/sennert1.html",
"http://www.uni-mannheim.de/mateo/camenaref/sennert2.html",
"http://www.uni-mannheim.de/mateo/camenaref/siglalatina.html",
"http://www.uni-mannheim.de/mateo/camenaref/societasjesu.html",
"http://www.uni-mannheim.de/mateo/camenaref/societasjesu.html#sj2",
"http://www.uni-mannheim.de/mateo/camenaref/societasjesu.html#sj3",
"http://www.uni-mannheim.de/mateo/camenaref/societasjesu.html#sj4",
"http://www.uni-mannheim.de/mateo/camenaref/societasjesu.html#sj5",
"http://www.uni-mannheim.de/mateo/camenaref/spener.html",
"http://www.uni-mannheim.de/mateo/camenaref/spener.html",
"http://www.uni-mannheim.de/mateo/camenaref/spitzel.html",
"http://www.uni-mannheim.de/mateo/camenaref/teissier.html",
"http://www.uni-mannheim.de/mateo/camenaref/tixier.html",
"http://www.uni-mannheim.de/mateo/camenaref/tomasini2.html",
"http://www.uni-mannheim.de/mateo/camenaref/valeriano.html",
"http://www.uni-mannheim.de/mateo/camenaref/vossius1.html",
"http://www.uni-mannheim.de/mateo/camenaref/vossius2.html",
"http://www.uni-mannheim.de/mateo/camenaref/vossius2.html",
"http://www.uni-mannheim.de/mateo/camenaref/vossius2.html",
"http://www.uni-mannheim.de/mateo/camenaref/wein.html",
"http://www.uni-mannheim.de/mateo/camenaref/witte.html",
"http://www.uni-mannheim.de/mateo/camenaref/witzel1.html",
"http://www.uni-mannheim.de/mateo/camenaref/zwinger.html"]
for address in popis:
# Use urllib2 to open page    
    req = urllib2.Request(address)
    response = urllib2.urlopen(req)
    html = urllib2.urlopen(req).read()
    soup = BeautifulSoup(html,'lxml')
    links = soup.find_all('a')
    for tag in links:
	link = tag.get('href',None)
        if link is not None:
            if link.endswith(suffix) and link.startswith(prefix):
# Open file listthesxml.txt, add links to it:            
                f = open('listthesxml.txt', 'a')
# Add the newline character (depending on OS):                
                f.write(link + os.linesep)
            elif link.endswith(suffix) and link.startswith(dots):
# These links will probably have to be corrected by hand:                
                link2="http://www.uni-mannheim.de/mateo/" + link[3:]
                f = open('listthesxml.txt', 'a')
                f.write(link2 + os.linesep)
