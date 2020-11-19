from argparse import ArgumentParser
import getpass
from main import handleMTIRequest


def remove_non_ascii(filepath, temp_file):
    # MTI cannot handle non-ascii charachters hence those charachters needs to be removed/replaced
    uc = open(filepath)
    op = open(temp_file, "w+")

    for line in uc.readlines()[1:]:
        ascii = line.encode('ascii', 'replace').decode()
        components = ascii.split('\t', 1)
        pmid = components[0]
        abstract = components[1]
        op_line = pmid + "|" + abstract
        op.write(op_line)

    uc.close()
    op.close()

def getInput(msg, err = "Please enter valid input"):
    res = ""
    while True:
        res = getpass.getpass(msg)
        if len(res)>0:
            return res
        else:
            print(err)

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('file', help="Path to input file")
    parser.add_argument('email', help="Email ID for identification by MTI")

    parser.add_argument(
        '--user', '-u', help="MTI Username, if not provided, API key will be required", default=None)
    parser.add_argument(
        '--output', help="Output file path, Default: result.tsv", default="result.tsv")

    args = parser.parse_args()

    temp_file = ".tmp_mti_process_non_ascii.txt"
    remove_non_ascii(args.file, temp_file)

    if args.user:
        password = getInput("Enter MTI password > ", "Please Enter valid Password")
        processed_result = handleMTIRequest(
            temp_file, args.email, ["--singleLinePMID"], username=args.user, password=password)
    else:
        apikey = getInput("Enter MTI APIKey > ", "Please Enter valid API-Key")
        processed_result = handleMTIRequest(
            temp_file, args.email, ["--singleLinePMID"], apikey=apikey)

    # processed_result is a Dictionary

    # Handle output format
    with open(args.output, "w+") as res_op:
        for key in processed_result:
            for term in processed_result[key]:
                res_op.write(key + '\t' + '\t'.join(term) + '\n')
