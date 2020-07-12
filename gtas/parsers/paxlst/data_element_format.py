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
                    "description": self.description(element[0][:-1]),
                }
            )

        return output

    def description(self, val):

        switch = {
            # UNBSegment
            # ===========
            "S001:0001": "Syntax Identifier",
            "S001:0002": "Syntax Version Number",
            "S002:0004": "Interchange Sender Identification",
            "S002:0007": "Identification Code Qualifier",
            "S003:0010": "Interchange Recipient Identification",
            "S003:0007": "Identification Code Qualifier",
            "S004:0017": "Date",
            "S004:0019": "Time",
            "0020": "Interchange Control Reference",
            "0026": "Application Reference",
            # UNGSegment
            # ===========
            "0038": "Message Group Identification",
            "S006:0040": "Application Sender Identifier",
            "S007:0044": "Application Recipient Identification",
            # "S004:0017": "Date",
            # "S004:0019": "Time",
            "0048": "Group Reference Number",
            "0051": "Controlling Agency",
            "S008:0052": "Message Version Number",
            "S008:0054": "Message Release Number",
            # UNHSegment
            # ===========
            "0062": "Message Reference Number",
            "S009:0065": "Message Type Identifier",
            "S009:0052": "Message Type Version",
            "S009:0054": "Message Type Release Number",
            "S009:0051": "Controlling Agency",
            "S009:0057": "Association Assigned Code",
            "0068": "Common Access Reference",
            "S010:0070": "Sequence Message Transfer Number",
            "S010:0073": "First/Last Message Transfer Indicator",
            # BGMSegment
            # ===========
            "C002:1001": "Document Name Code",
            "C106:1004": "Document Identifier",
            # RFFSegment
            # ===========
            "C506:1153": "Reference Code Qualifier",
            "C506:1154": "Reference Identifier",
            "C506:1060": "Revision Identifier",
            # NADSegment
            # ===========
            "3035": "Party Function Code Qualifier",
            "C080:3036": "Party Name",
            # COMSegment
            # ===========
            "C076:3148": "Communication Address Identifier",
            "C076:3155": "Communication Address Code Qualifier",
            # "C076:3148": "Communication Address Identifier",
            # "C076:3155": "Communication Address Code Qualifier",
        }

        return switch.get(
            val, "Could not get description for 'data_element_tag': " + val
        )
