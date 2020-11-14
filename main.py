import jnius_config
jnius_config.add_classpath("./lib/*")

import requests
from urllib.request import urlopen
from xml.etree.ElementTree import parse

import sys
import os
import html
from jnius import autoclass

def getAbstract(content):
    """
    Parameters
    ----------
    content: list
        List contains the PMID of the paper
    Returns
    -------
    abstract.txt: text file
        Generate a text file that will contain title and abstract based on PMID
    """
    with open('.abstract.txt','w') as o:
        for i in content:
            var_url = urlopen('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id={}'.format(i))
            xmldoc = parse(var_url)
            for item in xmldoc.iterfind('PubmedArticle'):
                abstract_text = item.findtext('MedlineCitation/Article/Abstract/AbstractText')
                article_title = item.findtext('MedlineCitation/Article/ArticleTitle')
                pmid = int(i)
                print('UI  - ', pmid, file=o)
                print('TI  - ', article_title, file=o)
                print('AB  - ', html.unescape(abstract_text), file=o)
                print("\n", file=o)

def handleMTIRequest(filename, mailId, username, password, additional_args = []):
    """
    Parameters
    ----------
    filename: str
        Path to input file containing abstracts
    mailId: str
        Registered Email Id
    username: str
        username of UMLS Terminology Services
    password: str
        password of UMLS Terminology Services
    additional_args: [str]
        List of arguments to be passed to MTI Generic Batch Processor.
        Send ["-h"] to see all supported flags
    [If you dont have username and password, kindly create one at 'https://uts.nlm.nih.gov//license.html']

    Returns
    ------
    resultDict: Dictionary 
        Dictionary containing MESH terms
    """
    GenericBatchNew = autoclass("GenericBatchNew")
    batch = GenericBatchNew()
    filepath = os.path.abspath(filename)
    command = ["--email", mailId ,filepath]
    command = additional_args + command
    result = batch.processor(command, username, password)
    resultDict = {}
    for line in result.splitlines():
        resultArr = line.split("|")
        pmid = resultArr[0]
        if pmid in resultDict:
            resultDict[pmid].append(resultArr[1:])
        else:
            resultDict[pmid] = [resultArr[1:]]
    return resultDict

if __name__ == "__main__":
    with open("sample-pmid-list.txt", "r") as f:
        content= f.read().splitlines()
    
    print("STEP 1 :\t Fetching abstracts")
    getAbstract(content)
    print("STEP 1 :\t Complete")
    email="Enter_EmailID"
    userName="Enter_Username"
    password="Enter_Password"

    print("STEP 2 :\t Send abstracts to MTI")
    result = handleMTIRequest( '.abstract.txt', email, userName, password )
    print("STEP 2 :\t Response received, printing results")
    print(result)
    print("STEP 2 :\t Complete")

