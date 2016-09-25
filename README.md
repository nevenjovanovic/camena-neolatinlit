# CAMENA - Latin Texts of Early Modern Europe: the XML files

## Background

[CAMENA (Corpus Automatum Multiplex Electorum Neolatinitatis Auctorum)](http://www.uni-mannheim.de/mateo/camenahtdocs/camena_e.html), a [DFG-funded](http://www.dfg.de/) research project carried out at the German Department of Heidelberg University Chair of German Literature (Modern Period), in cooperation with the Information Technology Center and the Library of the University of Mannheim, and led by [Prof. Dr. Wilhelm Kühlmann](http://www.gs.uni-heidelberg.de/personen/kuehlmann.html), was active from 1999 to 2013. In our opinion, it was one of the most important Neo-Latin digital initiatives. Since the machine-readable texts of CAMENA (and its sub-projects MATEO / Alte Drucke) were made available under the [Creative Commons Attribution / Share Alike license](LICENSE.md), here we are republishing the XML files of all the CAMENA collections as a Github repository, with all the caveats of the original project regarding citing and reliability, and with the intent to enable further digital experiments with CAMENA Neo-Latin material.

Sincere gratitude goes to people involved in CAMENA for all their efforts, and for making this possible. *Sumus nani gigantum humeris insidentes.*

## Contents

In CAMENA, texts are divided in five collections: [POEMATA](poemata), Neo-Latin poetry composed by German authors; [HISTORICA & POLITICA](historicapolitica), Latin historical and political writing; [THESAURUS ERUDITIONIS](thesaurus), a reference collection of dictionaries and handbooks of the period 1500-1750; [CERA](cera), printed Latin letters, mostly by German scholars, from the period 1530-1770; and ITALI, works by Italian Renaissance humanists born before 1500. The collection ITALI has no XML files, so it was not included in this repository.

We were not able to find information on the exact number of XML files produced by CAMENA. This repository contains **949** XML files in the POEMATA section, **382** files in the HISTORICA & POLITICA, **296** files in the THESAURUS ERUDITIONIS, and **124** files in CERA, with the total of **1751** files. Included files contain **50,458,045** words (tokens) below the `text` element (more on this in [Word count](Wordcount.md).

Not all CAMENA XML files provide full text of the digitized source. For example, the file [Arenhold_conspectus_index_II.xml](cera/Arenhold_conspectus_index_II.xml) in CERA contains only the table of contents to the digitized volume of Arenhold, Silvester Johannes: *Conspectus Bibliothecae Universalis Historico-Literario-Criticae Epistolarum : Typis Expressarum Et M[anu]S[crip]tarum, Illustrium Omnis Aevi Et Eruditissimorum Auctorum.* - Hanoverae : Sumptibus Hereduum [!] Foersterianorum, 1746. In the [CAMENA-CERA version](http://www.uni-mannheim.de/mateo/cera/autoren/arenhold_cera.html), the table of contents contains links to respective page images of the digitized book. We did not try to exclude such partial XML publications from this repository.

## TEI validation

The XML documents were validated using oXygen default validation. The oXygen project file used during validation is [camena-xml.xpr](camena-xml.xpr). Its validation scenario was [camena-xml-validation.scenarios](camena-xml-validation.scenarios).

## Scripts for downloading

The CAMENA XML files were downloaded from its original site using [Python scripts and lists of XML files](downloading-scripts). As the CAMENA Project did not provide any instructions for downloading sources, the process required some ad-hoc hacking, and some addresses had to be corrected manually. This means that the downloading process is not easily replicable. Nevertheless, we are publishing the scripts and address lists as a starting point for eventual further efforts and corrections.

## Corrections

As the CAMENA files are now under version control, all changes and corrections are welcome. We propose you offer them, in the usual Github way, as [pull requests](https://help.github.com/articles/about-pull-requests/).

## Contact

Github repository archiving of the CAMENA XML files was done by [Neven Jovanović](orcid.org/0000-0002-9119-399X), Department of Classical Philology, Faculty of Humanities and Social Sciences, 
University of Zagreb.

