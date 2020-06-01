import csv
file = open("AllMeshTerms.txt","r")
with open('AllData.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')  
    tsv_writer.writerow(['PMID', 'Terms', 'CUI', 'Score', 'Type', 'Misc', 'Location', 'Paths'])
    for line in file:
        fields = line.split("|")
        tsv_writer.writerow(fields)
        
