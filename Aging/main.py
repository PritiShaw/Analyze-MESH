import requests
from urllib.request import urlopen
from xml.etree.ElementTree import parse

f = open("pmid-AgingMeSHT-set.txt", "r")
with open('abstract.txt','w') as o:
    for i in f:
        var_url = urlopen('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id={}'.format(i))
        xmldoc = parse(var_url)
        for item in xmldoc.iterfind('PubmedArticle'):
            abstract_text = item.findtext('MedlineCitation/Article/Abstract/AbstractText')
            article_title = item.findtext('MedlineCitation/Article/ArticleTitle')
            pmid = int(i)
            print('UI  - ', pmid, file=o)
            print('TI  - ', article_title, file=o)
            print('AB  - ', abstract_text.encode(encoding="ascii",errors="namereplace"), file=o)
            print("\n", file=o)
    o.close()
f.close()
