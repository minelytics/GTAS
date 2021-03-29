from pydifact.segmentcollection import Interchange
import edifact
import print_handler

edifact_filename = "./sample-edifact/sample05.edi"
schema_filename = "paxlst-d02b.json"

interchange = Interchange.from_file(edifact_filename)

ignore_codeset_errors = False
show_only_unknown = False
verbose = False

# pretty print output - write_json = False
# ========================================
# json print output - write_json = True
# =====================================
write_json = True

codeset_manager = edifact.CodesetManager(verbose, ignore_codeset_errors)
message = edifact.load_edifact(edifact_filename)
paxlst_schema = edifact.load_schema_file(schema_filename, verbose)

if write_json:
    handler = print_handler.JsonPrintHandler()
else:
    handler = print_handler.PrettyPrintHandler()

parsed_json = edifact.handle_message(message, paxlst_schema, codeset_manager, verbose, show_only_unknown, handler)

print("PRINT PARSED JSON: ", parsed_json)
