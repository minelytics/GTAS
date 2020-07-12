import re


class DataElementFormat:
    def __init__(self, elements):
        self.elements = elements

    @property
    def process(self):
        output = []
        for element in self.elements:
            output.append(
                {
                    "data_element_tag": element[0][:-1],
                    "segment_requirement": element[0][-1],
                    "data_element_type": " ".join(re.findall("[a-zA-Z]+", element[1])),
                    "max_length": list(map(int, re.findall(r"\d+", element[1])))[0],
                    "data_value": element[2],
                    "description": self.description(element[0]),
                }
            )

        return output

    def description(self, val):

        switch = {
            # UNBSegment
            # ===========
            "S001:0001M": "Syntax Identifier",
            "S001:0002M": "Syntax Version Number",
            "S002:0004M": "Interchange Sender Identification",
            "S002:0007C": "Identification Code Qualifier",
            "S003:0010M": "Interchange Recipient Identification",
            "S003:0007C": "Identification Code Qualifier",
            "S004:0017M": "Date",
            "S004:0019M": "Time",
            "0020M": "Interchange Control Reference",
            "0026M": "Application Reference",
            # UNGSegment
            # ===========
            "0038M": "Message Group Identification",
            "S006:0040M": "Application Sender Identifier",
            "S007:0044M": "Application Recipient Identification",
            # "S004:0017M": "Date",
            # "S004:0019M": "Time",
            "0048M": "Group Reference Number",
            "0051M": "Controlling Agency",
            "S008:0052M": "Message Version Number",
            "S008:0054M": "Message Release Number",
            # UNHSegment
            # ===========
            "0062M": "Message Reference Number",
            "S009:0065M": "Message Type Identifier",
            "S009:0052M": "Message Type Version",
            "S009:0054M": "Message Type Release Number",
            "S009:0051M": "Controlling Agency",
            "S009:0057C": "Association Assigned Code",
            "0068C": "Common Access Reference",
            "S010:0070C": "Sequence Message Transfer Number",
            "S010:0073C": "First/Last Message Transfer Indicator",
            # BGMSegment
            # ===========
            "C002:1001M": "Document Name Code",
            "C106:1004C": "Document Identifier",
            # RFFSegment
            # ===========
            "C506:1153M": "Reference Code Qualifier",
            "C506:1154M": "Reference Identifier",
            "C506:1060C": "Revision Identifier",
            # NADSegment
            # ===========
            "3035M": "Party Function Code Qualifier",
            "C080:3036M": "Party Name",
            # COMSegment
            # ===========
            "C076:3148M": "Communication Address Identifier",
            "C076:3155M": "Communication Address Code Qualifier",
            "C076:3148C": "Communication Address Identifier",
            "C076:3155C": "Communication Address Code Qualifier",
            # TDTSegment
            # ===========
            "8051M": "Transport Stage Qualifier",
            "8028C": "Means of Transport Journey Identifier",
            "C040:3127C": "Carrier Identifier",
            # LOCSegment
            # ===========
            "3227M": "Location Function Code Qualifier",
            "C517:3225M": "Location Name Code",
            # DTMSegment
            # ===========
            "C507:2005M": "Date/Time/Period Function Code Qualifier",
            "C507:2380M": "Date/Time/Period Value",
            "C507:2379C": "Date/Time/Period Format Code",
            # NADSegment
            # ===========
            # "3035M": "Party Function Code Qualifier",
            "C080:3036C": "Party Name",  # last
            # "C080:3036C": "Party Name", # first
            # "C080:3036C": "Party Name", # second
            "C059:3042C": "Number and Street Identifier",
            "3164C": "City Name",
            "C819:3229C": "Country Sub-entity Name Code",
            "3251C": "Postal Identification Code",
            "3207C": "Country Name Code",
            # ATTSegment
            # ===========
            "9017M": "Attribute Function Code Qualifier",
            "C956:9019M": "Attribute Description Code",
            # GEISegment
            # ===========
            "9649M": "Processing Information Code Qualifier",
            "C012:7365M": "Processing Indicator Description Code",
            # FTXSegment
            # ===========
            "4451M": "Text Subject Code Qualifier",
            "C108:4440M": "Text Literal",
            # LOCSegment
            # ===========
            # "3227M": "Location Function Code Qualifier",
            # "C517:3225M": "Location Name Code",
            "C519:3222C": "First Related Location Name",
            "C553:3232C": "Second Related Location Name",
            # EMPSegment
            # ===========
            "9003M": "Employment Details Qualifier Code",
            "C948:9005M": "Employment Category Description Code",
            "C948:1131C": "Code List Identification Code",
            "C948:3055C": "Code List Responsible Agency Code",
            # NATSegment
            # ===========
            "3493M": "Nationality Code Qualifier",
            "C042:3293M": "Nationality Name Code",
            # DOCSegment
            # ===========
            # "C002:1001M": "Document Name Code",
            "C002:1131C": "Code List Identification Code",
            "C002:3055C": "Code List Responsible Agency Code",
            "C503:1004M": "Document Identifier",
        }

        return switch.get(
            val, "Could not get description for 'data_element_tag': " + val
        )
