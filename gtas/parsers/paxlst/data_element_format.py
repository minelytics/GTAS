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
        }

        return switch.get(
            val, "Could not get description for 'data_element_tag': " + val
        )
