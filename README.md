MTI Batch Processing
---
Python code to process Journal abstracts and get MeSH terms using MTI WebAPI.   

## Requirements
* To run the code, **Java** is required.  
* You will need MTI account, if you dont have kindly register at [UMLS Terminology Services](https://uts.nlm.nih.gov//license.html)

## Installation
To install dependencies:  
`pip install -r requirements.txt`

## Supporting classes/libraries
The JAR files present in **lib** directory are taken from [ziy/skr-webapi](https://github.com/ziy/skr-webapi/), these are required by Pyjnius

## Functions
1. `getAbstract`: Take list of pmid as a input and generate text file of abstracts.
2. `handleMTIRequest`: Take abstract text file as input and print the MESH terms.  

## Examples

1. **Get MeSH Terms from list of PMIDs**  
    Using `getAbstract`, we retreive the Abstracts and generate the input file for MTI Batch processor. This file is uploaded is processed using `handleMTIRequest` function.  
    [Code Pointer](./main.py#L73)

2. **Get MeSH Terms from space seperated Abstracts file**     
    [Code Pointer](./example.py)  
    
    ```
    usage: MTI_Extraction.py [-h] [-output OUTPUT] file email user

    positional arguments:
    file            Path to input file
    email           Email ID for identification by MTI
    user            MTI Username

    optional arguments:
    -h, --help      show this help message and exit
    -output OUTPUT  Output file path, Default: result.tsv
    ```

    To run  
    `python3 example.py sample-abstracts.txt UserName EmailID`  
    To continue ou will be prompted for MTI password