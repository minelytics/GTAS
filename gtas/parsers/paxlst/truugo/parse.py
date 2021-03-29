import argparse
import json

import html_parser as parse


def convert_attribute(attribute):
    json = {"code": attribute.code, "desc": attribute.desc, "name": attribute.name}
    if len(attribute.attributes) > 0:
        json["element_type"] = "Composite Attribute"
        json["conditional"] = attribute.repeat
        json["attributes"] = []
        for a in attribute.attributes:
            json["attributes"].append(convert_attribute(a))
    else:
        json["element_type"] = "Attribute"
        json["content_length"] = attribute.length
        json["conditional"] = attribute.repeat
        json["content_type"] = attribute.type

    if attribute.codeset is not None:
        json["codeset"] = attribute.codeset

    return json


def section_repeat_string_to_conditional(s):
    if s.startswith("C"):
        return "Conditional"
    else:
        return "Mandatory"


def section_repeat_string_to_cardinality(s):
    return s[1:].lstrip()


def convert_section(section):
    json = {
        "code": section.code,
        "desc": section.desc,
        "element_type": "Segment",
        "name": section.name,
        "conditional": section_repeat_string_to_conditional(section.repeat),
        "cardinality": section_repeat_string_to_cardinality(section.repeat),
        "attributes": [],
    }
    for a in section.attributes:
        json["attributes"].append(convert_attribute(a))
    return json


def group_repeat_string_to_conditional(s):
    return s.split(" ")[0]


def group_repeat_string_to_cardinality(s):
    return s.split(" ")[1].lstrip()


def convert_group(grp):
    json = {
        "code": grp.code,
        "desc": grp.desc,
        "element_type": "Group",
        "conditional": group_repeat_string_to_conditional(grp.repeat),
        "cardinality": group_repeat_string_to_cardinality(grp.repeat),
        "sections": [],
    }
    for section in grp.sections:
        if isinstance(section, parse.MySection):
            json["sections"].append(convert_section(section))
        elif isinstance(section, parse.MyGroup):
            json["sections"].append(convert_group(section))
    return json


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description='Parse Truugo html schema description')
    # parser.add_argument('file', metavar='file', type=str, help='truugo html src file to parse')
    # args = parser.parse_args()

    # html_filename = args.file

    html_filename = "d02b-paxlst.html"

    with open(html_filename, "r") as html_file:
        html_text = html_file.read()

    parser = parse.FormatParser()
    parser.parse(html_text)

    json_schema = []

    for section in parser.my_sections:
        if isinstance(section, parse.MySection):
            json_schema.append(convert_section(section))
        elif isinstance(section, parse.MyGroup):
            json_schema.append(convert_group(section))

    print(json.dumps(json_schema))
