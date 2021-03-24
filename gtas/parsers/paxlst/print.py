from pydifact.segmentcollection import Interchange
import edifact
import print_handler

edifact_filename = "./sample-edifact/sample05.edi"
schema_filename = "paxlst-d02b.json"

# original
# ========
# edifact_filename = "./sample-edifact/simple.edi"
# schema_filename = "schema01.json"

interchange = Interchange.from_file(edifact_filename)

ignore_codeset_errors = False
show_only_unknown = False
verbose = False
write_json = False

# for segment in interchange.segments:
#     # print('Segment tag: {}, content: {}'.format(
#     #     segment.tag, segment.elements))
#     schema_filename = f"./schema/{segment.tag}.json"
#
#     # print(schema_filename)
#
#     codeset_manager = edifact.CodesetManager(verbose, ignore_codeset_errors)
#     message = edifact.load_edifact(edifact_filename)
#     paxlst_schema = edifact.load_schema_file(schema_filename, verbose)
#
#     if write_json:
#         handler = print_handler.JsonPrintHandler()
#     else:
#         handler = print_handler.PrettyPrintHandler()
#     edifact.handle_message(message, paxlst_schema, codeset_manager, verbose, show_only_unknown, handler)


codeset_manager = edifact.CodesetManager(verbose, ignore_codeset_errors)
message = edifact.load_edifact(edifact_filename)
cuscar_schema = edifact.load_schema_file(schema_filename, verbose)
if write_json:
    handler = print_handler.JsonPrintHandler()
else:
    handler = print_handler.PrettyPrintHandler()
edifact.handle_message(message, cuscar_schema, codeset_manager, verbose, show_only_unknown, handler)
