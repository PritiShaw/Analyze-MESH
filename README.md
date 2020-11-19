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

## How to use with MTI API Key
[`handleMTIRequest(filename, mailId, additional_args=[], username=None, password=None, apikey=None)`](./main.py#L41)  
The function handles both, authentication with **username/password** and authentication using **API key**. You can get your API Key under My Profile section of your UTS account.   

**For using API key,** do not pass `username` and `password` arguments, only pass `apikey` as follows:  
`handleMTIRequest(filename, mailID, apikey=<API-KEY>, ...)`  

**[DEPRECATED] For using Username/Password,** do not pass `apikey` argument, only pass `username` and `password` as follows:  
`handleMTIRequest(filename, mailID, username=<USERNAME>, password=<PASSWORD> , ...)`  

**NOTE:** **API key takes precedence** over Username/Password, ie if both api-key and username/password is given then authentication will be done using API key.

## Examples

1. **Get MeSH Terms from list of PMIDs**  
    Using `getAbstract`, we retreive the Abstracts and generate the input file for MTI Batch processor. This file is uploaded is processed using `handleMTIRequest` function.  
    [Code Pointer](./main.py#L84)

2. **Get MeSH Terms from space seperated Abstracts file**     
    [Code Pointer](./example.py)  
    
    ```
    usage: example.py [-h] [--user USER] [--output OUTPUT] file email

    positional arguments:
    file                  Path to input file
    email                 Email ID for identification by MTI

    optional arguments:
    -h, --help            show this help message and exit
    --user USER, -u USER  MTI Username, if not provided, API key will be required
    --output OUTPUT       Output file path, Default: result.tsv
    ```

    To run  
    - Using MTI API Key
        `python3 example.py sample-abstracts.txt EmailID`  
        To continue you will be prompted for MTI API Key
    - Using Username/Password [DEPRECATED]
        `python3 example.py sample-abstracts.txt EmailID -u USERNAME`  
        To continue you will be prompted for MTI password