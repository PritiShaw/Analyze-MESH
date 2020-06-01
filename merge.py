filenames = ["Aging/pmid-AgingMeSHT-set.txt", "CommunicableDiseases/pmid-Communicab-set.txt",
 "ComputationalBiology/pmid-Computatio-set.txt", "Neoplasms/pmid-NeoplasmsM-set.txt", "Neurosciences/pmid-neurosciene-set.txt"]

meshFile = ["Aging/meshterms.txt", "CommunicableDiseases/meshterms.txt",
 "ComputationalBiology/meshterms.txt", "Neoplasms/meshterms.txt", "Neurosciences/meshterms.txt"]

with open("AllPMID.txt", "w") as outfile:
    for filename in filenames:
        with open(filename) as infile:
            contents = infile.read()
            outfile.write(contents)
        outfile.write("\n")

with open("AllMeshTerms.txt", "w") as outfile:
    for filename in meshFile:
        with open(filename) as infile:
            contents = infile.read()
            outfile.write(contents)
        outfile.write("\n")
