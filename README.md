# Table of contents
- `AllData.py`: Pyhthon code for displaing mesh terms of 100 articles in TSV file _(*AllData.tsv*)_.
- `AllData.tsv`: TSV file contains details of all 100 articles.
- `AllPMID.txt`: File contains _PMID_ of 100 articles.
- `AllAPIMeshTerms.txt`: File contains the mesh terms of 100 articles which was obtained after merging all `meshterms.txt`(5 * 20=100).
- `CompareMeshCSV.py`: Pyhton code for comparing between Mesh terms produced by using WebAPI and Eutil and dispaying it in a TSV file.
- `compareMesh.tsv`: Shows the comparison between Mesh terms produced by using WebAPI and Eutil.
- `final.sh`: Bash script to run the whole program.
- `main.py`: Python code for extracting abstract, title from the XML files. 
- `abstract.txt`: Contains the pmid(UI), title(TI) and abstract(AB) of 20 articles which was extracted from the XML file.
- `meshterms.txt`: Contains the mesh terms which was obtained after running the Web API.


## File Structure
<pre>
├── Aging  
|    ├── final.sh  
|    ├── abstract.txt   
|    ├── index.py  
|    ├── meshterms.txt  
|    └── pmid-AgingMeshT-set.txt  
├── CommunicableDiseases  
|    ├── final.sh  
|    ├── abstract.txt  
|    ├── index.py  
|    ├── meshterms.txt  
|    └── pmid-Communicab-set.txt  
├── ComputationalBiology  
|    ├── final.sh  
|    ├── abstract.txt  
|    ├── index.py  
|    ├── meshterms.txt  
|    └── pmid-Computatio-set.txt  
├── Neoplasms  
|    ├── final.sh  
|    ├── abstract.txt  
|    ├── index.py  
|    ├── meshterms.txt  
|    └── pmid-NeoplasmsM-set.txt  
├── Neurosciences  
|    ├── final.sh  
|    ├── abstract.txt  
|    ├── index.py  
|    ├── meshterms.txt  
|    └── pmid-neurosciene-set.txt  
├── AllAPIMeshTerms.txt  
├── AllData.py  
├── AllData.tsv  
├── AllPMID.txt  
├── compareMesh.tsv  
└── compareMesh.tsv  
</pre>

