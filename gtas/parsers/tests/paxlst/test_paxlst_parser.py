import math
from gtas.parsers.paxlst import edifact, print_handler


def test_paxlst_header_message():
    edifact_filename = "./resources/sample-edifact-messages/test_paxlst_header.edi"
    schema_filename = "paxlst-d02b.json"

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

    # failing test
    assert parsed_json == ""

