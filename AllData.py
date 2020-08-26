import csv
file = open("AllMeshTerms.txt","r")
with open('AllData.csv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file)  
    headers = ['PMID', 'Terms', 'CUI', 'Score', 'Type', 'Misc', 'Location', 'Paths','']
    header_count = len(headers)
    tsv_writer.writerow(headers)
    for line in file:
        fields=line.strip().split("|")
        while len(fields)!=header_count:
            fields.append("")        
        tsv_writer.writerow(fields)
out_file.close()
        
