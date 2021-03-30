import math

from gtas.parsers.paxlst import edifact, print_handler


def test_paxlst_header_message():
    edifact_filename = (
        "./gtas/parsers/tests/resources/sample-edifact-messages/test_paxlst_header.edi"
    )
    schema_filename = "./gtas/parsers/tests/paxlst/paxlst-d02b.json"

    ignore_codeset_errors = False
    show_only_unknown = False
    verbose = False
    write_json = True

    codeset_manager = edifact.CodesetManager(verbose, ignore_codeset_errors)
    message = edifact.load_edifact(edifact_filename)
    paxlst_schema = edifact.load_schema_file(schema_filename, verbose)

    if write_json:
        handler = print_handler.JsonPrintHandler()
    else:
        handler = print_handler.PrettyPrintHandler()

    parsed_json = edifact.handle_message(
        message, paxlst_schema, codeset_manager, verbose, show_only_unknown, handler
    )

    expected_json = [
        {
            "hierarchy": "UNB",
            "desc": "",
            "code": "UNB",
            "conditional": "Mandatory",
            "cardinality": 1,
            "attributes": [
                {
                    "code": "0001",
                    "name": "Syntax identifier",
                    "desc": "",
                    "value": "UN/ECE level A",
                    "value_coded": "UNOA",
                },
                {
                    "code": "0002",
                    "name": "Syntax version number",
                    "desc": "",
                    "value": "Version 4",
                    "value_coded": "4",
                },
                {
                    "code": "0004",
                    "name": "Interchange sender identification",
                    "desc": "",
                    "value": "APIS*ABE",
                },
                {
                    "code": "0010",
                    "name": "Interchange recipient identification",
                    "desc": "",
                    "value": "USADHS",
                },
                {"code": "0017", "name": "Date", "desc": "", "value": "070429"},
                {"code": "0019", "name": "Time", "desc": "", "value": "0900"},
                {
                    "code": "0020",
                    "name": "Interchange control reference",
                    "desc": "",
                    "value": "000000001",
                },
                {
                    "code": "0022",
                    "name": "Recipient reference/password",
                    "desc": "",
                    "value": "",
                },
                {
                    "code": "0026",
                    "name": "Application reference",
                    "desc": "",
                    "value": "USADHS",
                },
            ],
        },
        {
            "hierarchy": "UNH",
            "desc": "A service segment starting and uniquely identifying a message. The message type code for the Passenger list message is PAXLST.",
            "code": "UNH",
            "conditional": "Mandatory",
            "cardinality": "1",
            "attributes": [
                {
                    "code": "0062",
                    "name": "MESSAGE REFERENCE NUMBER",
                    "desc": "Unique message reference assigned by the sender.",
                    "value": "PAX001",
                },
                {
                    "code": "0065",
                    "name": "Message type",
                    "desc": "Code identifying a type of message and assigned by its controlling agency.",
                    "value": "Passenger list message",
                    "value_coded": "PAXLST",
                },
                {
                    "code": "0052",
                    "name": "Message version number",
                    "desc": "Version number of a message type.",
                    "value": "Draft version/UN/EDIFACT Directory",
                    "value_coded": "D",
                },
                {
                    "code": "0054",
                    "name": "Message release number",
                    "desc": "Release number within the current message version number.",
                    "value": "Release 2002 - B",
                    "value_coded": "02B",
                },
                {
                    "code": "0051",
                    "name": "Controlling agency, coded",
                    "desc": "Code identifying a controlling agency.",
                    "value": "UN/CEFACT",
                    "value_coded": "UN",
                },
                {
                    "code": "0057",
                    "name": "Association assigned code",
                    "desc": "Code, assigned by the association responsible for the design and maintenance of the message type concerned, which further identifies the message.",
                    "value": "IATA",
                },
                {
                    "code": "0068",
                    "name": "COMMON ACCESS REFERENCE",
                    "desc": "Reference serving as a key to relate all subsequent transfers of data to the same business case or file.",
                    "value": "API01",
                },
                {
                    "code": "0070",
                    "name": "Sequence of transfers",
                    "desc": "Number assigned by the sender indicating the transfer sequence of a message related to the same topic. The message could be an addition or a change to an earlier transfer related to the same topic.",
                    "value": "01",
                },
            ],
        },
        {
            "hierarchy": "BGM",
            "desc": "A segment to indicate the type and function of the message.",
            "code": "BGM",
            "conditional": "Mandatory",
            "cardinality": "1",
            "attributes": [
                {
                    "code": "1001",
                    "name": "Document name code",
                    "desc": "Code specifying the document name.",
                    "value": "Passenger list",
                    "value_coded": "745",
                }
            ],
        },
        {
            "hierarchy": "RFF",
            "desc": "A segment to specify message reference.",
            "code": "RFF",
            "conditional": "Conditional",
            "cardinality": "1",
            "attributes": [
                {
                    "code": "1153",
                    "name": "Reference code qualifier",
                    "desc": "Code qualifying a reference.",
                    "value": "Transaction reference number",
                    "value_coded": "TN",
                },
                {
                    "code": "1154",
                    "name": "Reference identifier",
                    "desc": "Identifies a reference.",
                    "value": "BA123456789",
                },
                {
                    "code": "1156",
                    "name": "Document line identifier",
                    "desc": "To identify a line of a document.",
                    "value": "",
                },
                {
                    "code": "4000",
                    "name": "Reference version identifier",
                    "desc": "To identify the version of a reference.",
                    "value": "",
                },
                {
                    "code": "1060",
                    "name": "Revision identifier",
                    "desc": "To identify a revision.",
                    "value": "1",
                },
            ],
        },
    ]

    # # failing test
    # assert parsed_json == ""

    # passing test
    assert parsed_json == expected_json
