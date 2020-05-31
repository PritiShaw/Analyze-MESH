import csv
from urllib.request import urlopen
from xml.etree.ElementTree import parse

f = open("AllPMID.txt", "r")
Dictonary ={}
for i in f:
    var_url = urlopen('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id={}'.format(i))
    i= str(i.strip())
    Dictonary[i] = {'eutil':[],'webapi':[]}
    xmldoc = parse(var_url)
    for item in xmldoc.iterfind('PubmedArticle/MedlineCitation/MeshHeadingList'):
        for e in item.findall('MeshHeading'):
            if(e.find('DescriptorName').text):
                Dictonary[i]['eutil'].append(e.find('DescriptorName').text)
    #print(Dict)
f.close()
print("STEP1 Completed...")

readfile = open('APIMeshTerms.txt', "r")
for line in readfile:
        Type = line.split("|")
        PMID = Type[0]
        MESH = Type[1]
        #print(PMID,MESH)
        Dictonary[PMID]['webapi'].append(MESH)
#print(Dictonary)
print("STEP2 Completed...")


with open('compare.tsv', mode='w') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    print("PMID","EUTIL","WEBAPI",sep='\t',file=f)
    for key,val in Dictonary.items():
        list_A= val['eutil']
        list_B= val['webapi']
        len_A=len(list_A)
        len_B=len(list_B)
        max_length= max(len_A,len_B)
        for idx in range(max_length):
            row = [key,"",""]
            row[1] = list_A[idx] if idx<len_A else "NA"
            row[2] = list_B[idx] if idx<len_B else "NA"
            print('\t'.join(row),file=f)
print("STEP3 Completed...")
