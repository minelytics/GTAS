from gtas.parsers.paxlst.element2 import Element


class DTM:
    def __init__(self, message, group=None):
        self.elements = message.segments[0].elements
        self.group = group

    @property
    def parse(self):
        e = Element()
        output = {
            "segment": "DTM",
            "segment_description": "Date/Time/Period",
            "group": self.group,
        }
        output.update(e.segment_group("DTM", self.group))

        output["elements"].append(
            e.definition(
                data_element="C507",
                component_element="2005M",
                attributes="an..3",
                data=self.elements[0][0],
            )
        )
        output["elements"].append(
            e.definition(
                data_element="C507",
                component_element="2380M",
                attributes="n..10",
                data=self.elements[0][1],
            )
        )

        if e.struct(self.elements) == "list(list(str,str,str))":
            output["elements"].append(
                e.definition(
                    data_element="C507",
                    component_element="2379C",
                    attributes="an..3",
                    data=self.elements[0][2],
                )
            )

        return output
