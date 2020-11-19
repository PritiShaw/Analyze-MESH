import jnius_config
jnius_config.add_classpath("./lib/*")

import os
import html
from xml.etree.ElementTree import parse
from urllib.request import urlopen
from jnius import autoclass


def get_abstract(content):
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
    with open('.abstract.txt', 'w') as o:
        for i in content:
            var_url = urlopen(
                'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id={}'.format(i))
            xmldoc = parse(var_url)
            for item in xmldoc.iterfind('PubmedArticle'):
                abstract_text = item.findtext(
                    'MedlineCitation/Article/Abstract/AbstractText')
                article_title = item.findtext(
                    'MedlineCitation/Article/ArticleTitle')
                pmid = int(i)
                print('UI  - ', pmid, file=o)
                print('TI  - ', article_title, file=o)
                print('AB  - ', html.unescape(abstract_text), file=o)
                print("\n", file=o)


def handle_mti_request(filename, mail_id, additional_args=[], username=None, password=None, apikey=None):
    """
    Parameters
    ----------
    filename: str
        Path to input file containing abstracts
    mail_id: str
        Registered Email Id
    username: str
        username of UMLS Terminology Services
    password: str
        password of UMLS Terminology Services
    apikey: str
        apikey of UMLS Terminology Services
    additional_args: [str]
        List of arguments to be passed to MTI Generic Batch Processor.
        Send ["-h"] to see all supported flags
    [If you dont have username and password, kindly create one at 'https://uts.nlm.nih.gov//license.html']

    Returns
    ------
    result_dict: Dictionary 
        Dictionary containing MESH terms
    """
    GenericBatchNew = autoclass("GenericBatchNew")
    batch = GenericBatchNew()
    filepath = os.path.abspath(filename)
    command = ["--email", mail_id, filepath]
    command = additional_args + command

    if apikey:
        result = batch.processor(command, apikey)
    else:
        result = batch.processor(command, username, password)

    result_dict = {}
    for line in result.splitlines():
        result_arr = line.split("|")
        pmid = result_arr[0]
        if pmid in result_dict:
            result_dict[pmid].append(result_arr[1:])
        else:
            result_dict[pmid] = [result_arr[1:]]
    return result_dict


if __name__ == "__main__":
    with open("sample-pmid-list.txt", "r") as f:
        content = f.read().splitlines()

    print("STEP 1 :\t Fetching abstracts")
    get_abstract(content)
    print("STEP 1 :\t Complete")
    email = "Enter_Email_id"
    apikey = "Enter_apikey"

    print("STEP 2 :\t Send abstracts to MTI")
    result = handle_mti_request('.abstract.txt', email, apikey)
    print("STEP 2 :\t Response received, printing results")
    print(result)
    print("STEP 2 :\t Complete")
