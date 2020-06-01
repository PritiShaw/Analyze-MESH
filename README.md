# Table of contents
- `index.py`: Python code for extracting abstract, title from the XML files.
- `run.sh`:  Bash script to run the whole program. It takes three arguments that are mentioned in the _Instructions_.
- `AllData.tsv`: TSV file contains mesh details of all 100 articles.
- `AllMeshTerms.txt`: File contains the mesh terms of 100 articles which was obtained after merging all `meshterms.txt`(5 * 20=100).
- `compareMesh.tsv`: Shows the comparison between Mesh terms produced by using WebAPI and Eutil.
- `AllPMID.txt`: File contains _PMID_ of 100 articles.
- `CompareMeshCSV.py`: Pyhton code for comparing between Mesh terms produced by using WebAPI and Eutil and dispaying it in a TSV file.
- `merge.py`: Merges the pmid and mesh details of all the 5 diseases to the *AllPMID.txt* and *AllMeshTerms.txt* respectively.
- `AllData.py`: Pyhthon code for displaing mesh details of 100 articles in TSV file _(*AllData.tsv*)_.


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
├── AllMeshTerms.txt  
├── AllData.py 
├── merge.py  
├── compareMeshCSV.tsv  
├── AllPMID.txt
├── script.sh
├── run.sh
├── compare.tsv  
└── AllData.tsv  
</pre>

## Instructions
- Download the repository [https://github.com/PritiShaw/Analyze-MESH.git](https://github.com/PritiShaw/Analyze-MESH.git) and extract it.
- Download the WebAPI from [https://ii.nlm.nih.gov/Web_API/index.shtml](https://ii.nlm.nih.gov/Web_API/index.shtml) and extract it.
- open the terminal and `cd Analyze-MESH`
- `chmod +x script.sh`
- `chmod +x run.sh`
- `./run.sh PATH_TO_Analyze-MESH_REPO PATH_TO_WEPAPI_FOLDER Your_Email`
