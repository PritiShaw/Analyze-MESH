# Table of contents
- `AllData.py`: Pyhthon code for displaing mesh details of 100 articles in TSV file _(*AllData.tsv*)_.
- `AllData.tsv`: TSV file contains mesh details of all 100 articles.
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
|    ├── index.py   
|    └── pmid-AgingMeshT-set.txt  
├── CommunicableDiseases   
|    ├── index.py  
|    └── pmid-Communicab-set.txt  
├── ComputationalBiology   
|    ├── index.py  
|    └── pmid-Computatio-set.txt  
├── Neoplasms  
|    ├── index.py  
|    └── pmid-NeoplasmsM-set.txt  
├── Neurosciences  
|    ├── index.py  
|    └── pmid-neurosciene-set.txt  
├── AllAPIMeshTerms.txt  
├── AllData.py  
├── AllData.tsv  
├── AllPMID.txt
├── script.shscript
├── run.sh
├── compareMesh.tsv  
└── compareMesh.tsv  
</pre>
