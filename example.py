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


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('file', help="Path to input file")
    parser.add_argument('email', help="Email ID for identification by MTI")
    parser.add_argument('user', help="MTI Username")

    parser.add_argument(
        '-output', help="Output file path, Default: result.tsv", default="result.tsv")

    args = parser.parse_args()

    password = getpass.getpass("Enter MTI password > ")
    temp_file = ".tmp_mti_process_non_ascii.txt"

    remove_non_ascii(args.file, temp_file)

    # processed_result is a Dictionary
    processed_result = handleMTIRequest(
        temp_file, args.email, args.user, password, ["--singleLinePMID"])

    # Handle output format
    with open(args.output, "w+") as res_op:
        for key in processed_result:
            for term in processed_result[key]:
                res_op.write(key + '\t' + '\t'.join(term) + '\n')
