from urllib.request import urlopen

filenames = ["Aging/pmid-AgingMeSHT-set.txt", "CommunicableDiseases/pmid-Communicab-set.txt",
 "ComputationalBiology/pmid-Computatio-set.txt", "Neoplasms/pmid-NeoplasmsM-set.txt", "Neurosciences/pmid-neurosciene-set.txt"]
def search(pmid):
    for filename in filenames:
        with open(filename) as infile:
            datafile = infile.readlines()
            for line in datafile:
                if int(pmid)==int(line):
                    return(filename.split('/')[0])

print(search(30731065))
        