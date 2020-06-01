# Table of contents
<<<<<<< HEAD
- `main.py`: Python code for extracting abstract, title from the XML files.
- `run.sh`:  Bash script to run the whole program. It takes three arguments that are mentioned in the _Instructions_.
- `AllData.csv`: CSV file contains mesh details of all 100 articles.
=======
- `index.py`: Python code for extracting abstract, title from the XML files.
- `run.sh`:  Bash script to run the whole program. It takes three arguments that are mentioned in the _Instructions_.
- `AllData.tsv`: TSV file contains mesh details of all 100 articles.
>>>>>>> b7b35ea0d1153095e1dff82651984b4bce32770b
- `AllMeshTerms.txt`: File contains the mesh terms of 100 articles which was obtained after merging all `meshterms.txt`(5 * 20=100).
- `compareMesh.tsv`: Shows the comparison between Mesh terms produced by using WebAPI and Eutil.
- `AllPMID.txt`: File contains _PMID_ of 100 articles.
- `CompareMeshCSV.py`: Pyhton code for comparing between Mesh terms produced by using WebAPI and Eutil and dispaying it in a TSV file.
- `merge.py`: Merges the pmid and mesh details of all the 5 diseases to the *AllPMID.txt* and *AllMeshTerms.txt* respectively.
- `AllData.py`: Pyhthon code for displaing mesh details of 100 articles in TSV file _(*AllData.tsv*)_.


## Directory Structure
<pre>
├── Aging     
|    ├── main.py   
|    └── pmid-AgingMeshT-set.txt  
├── CommunicableDiseases   
|    ├── main.py  
|    └── pmid-Communicab-set.txt  
├── ComputationalBiology   
|    ├── main.py  
|    └── pmid-Computatio-set.txt  
├── Neoplasms  
|    ├── main.py  
|    └── pmid-NeoplasmsM-set.txt  
├── Neurosciences  
|    ├── main.py  
|    └── pmid-neurosciene-set.txt  
├── AllMeshTerms.txt  
<<<<<<< HEAD
├── AllData.py  
├── merge.py  
├── compareMeshCSV.tsv  
├── AllPMID.txt
├── script.sh  
├── run.sh  
├── compare.tsv  
└── AllData.csv  
=======
├── AllData.py 
├── merge.py  
├── compareMeshCSV.tsv  
├── AllPMID.txt
├── script.sh
├── run.sh
├── compare.tsv  
└── AllData.tsv  
>>>>>>> b7b35ea0d1153095e1dff82651984b4bce32770b
</pre>

## Instructions
- Download the repository [https://github.com/PritiShaw/Analyze-MESH.git](https://github.com/PritiShaw/Analyze-MESH.git) and extract it.
- Download the WebAPI from [https://ii.nlm.nih.gov/Web_API/index.shtml](https://ii.nlm.nih.gov/Web_API/index.shtml) and extract it.
- open the terminal and `cd Analyze-MESH`
- `chmod +x script.sh`
- `chmod +x run.sh`
- `./run.sh PATH_TO_Analyze-MESH_REPO PATH_TO_WEPAPI_FOLDER Your_Email`
<<<<<<< HEAD
- You will be prompted for username password, register at [https://uts.nlm.nih.gov/license.html](https://uts.nlm.nih.gov/license.html) to get them.
=======
>>>>>>> b7b35ea0d1153095e1dff82651984b4bce32770b
