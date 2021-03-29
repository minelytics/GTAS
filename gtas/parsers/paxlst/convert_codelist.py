import argparse
import json

# convert textual representation of codelist to json for use by this prettyprinter.
# save the text data as data.txt
# python convert_codelist.py  > o.json
# rename file and add to codelists.json index file

# text format is 3 lines per code entry:
# code
# name
# desc

# Tip you can get the codesets in this format by copy-pasting the html from
# https://www.truugo.com/edifact/d03a/cuscar/


# parser = argparse.ArgumentParser(description='Convert EDIFACT codeset to JSON')
# parser.add_argument('file', metavar='file', type=str, help='file to convert')
# args = parser.parse_args()

file = "d02b-paxlst.html"

with open(file) as raw_codelist_file:
    codes = {}
    while True:
        code = raw_codelist_file.readline().rstrip()
        if not code:
            break
        name = raw_codelist_file.readline().rstrip()
        desc = raw_codelist_file.readline().rstrip()

        codes[code] = {}
        codes[code]["name"] = name
        codes[code]["desc"] = desc

    print(json.dumps(codes))
