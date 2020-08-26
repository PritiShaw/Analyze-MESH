import csv
from urllib.request import urlopen
from xml.etree.ElementTree import parse

filenames = ["Aging/pmid-AgingMeSHT-set.txt", "CommunicableDiseases/pmid-Communicab-set.txt",
 "ComputationalBiology/pmid-Computatio-set.txt", "Neoplasms/pmid-NeoplasmsM-set.txt", "Neurosciences/pmid-neurosciene-set.txt"]
def search(pmid):
    for filename in filenames:
        with open(filename) as infile:
            datafile = infile.readlines()
            for line in datafile:
                if int(pmid)==int(line):
                    return(filename.split('/')[0])

f = open("AllPMID.txt", "r")
Dictonary ={}
for i in f:
    var_url = urlopen('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id={}'.format(i))
    i= str(i.strip())
    Dictonary[i] = {'eutil':[],'webapi':[], 'topic_term':[]}
    Dictonary[i]['topic_term'].append((search(i)))
    xmldoc = parse(var_url)
    for item in xmldoc.iterfind('PubmedArticle/MedlineCitation/MeshHeadingList'):
        for e in item.findall('MeshHeading'):
            if(e.find('DescriptorName').text):
                Dictonary[i]['eutil'].append(e.find('DescriptorName').text)
    #print(Dict)
f.close()
#print("STEP1 Completed...")

readfile = open('AllMeshTerms.txt', "r")
for line in readfile:
        Type = line.split("|")
        if(len(Type)<2):
            continue
        else:
            pmid = Type[0]
            mesh = Type[1]
        #print(PMID,MESH)
        Dictonary[pmid]['webapi'].append(mesh)
#print(Dictonary)
#print("STEP2 Completed...")


with open('compare.tsv', mode='w') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    print("PMID","EUTIL","WEBAPI", "TOPIC TERM",sep='\t',file=f)
    for key,val in Dictonary.items():
        list_A=val['eutil']
        list_B=val['webapi']
        list_C=val['topic_term']
        for i in list_B:
            row = [key,"","",""]
            if i in list_A or i[1:] in list_A:
                continue
            else:
                row[1]="NA"
                row[2]= i
                row[3]= list_C[0]
                print('\t'.join(row),file=f)
        for i in list_A:
            if i in list_B or '*'+i in list_B:
                row[1]= i
                row[2]= i
                row[3]= list_C[0]
                print('\t'.join(row),file=f)
            else:
                row[1]=i
                row[2]= "NA"
                row[3]= list_C[0]
                print('\t'.join(row),file=f)
#print("STEP3 completed...")