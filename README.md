MTI Batch Processing
---
Python code to process Journal abstracts and get MeSH terms using MTI WebAPI.   


## Supporting libraries
The JAR files present in **lib** directory are taken from [ziy/skr-webapi](https://github.com/ziy/skr-webapi/)

## Pyjinius
- Version: 1.1.4
- JAR files included by pyjinius are present in lib folder.

## Functions
1. `getAbstract`: Take list of pmid as a input and generate text file of abstracts.
2. `handleMTIRequest`: Take abstract text file as input and print the MESH terms.  