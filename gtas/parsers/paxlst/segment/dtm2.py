from gtas.parsers.paxlst.element2 import Element
from gtas.parsers.paxlst.definition import Definition
from gtas.parsers.paxlst.group import Group


class DTM:
    def parse(self, message, group=None):
        elements = message.segments[0].elements
        e = Element()

        output = {
            "segment": "DTM",
            "segment_description": "Date/Time/Period",
            "group": group,
        }
        output.update(Group.get("DTM", group))

        output["elements"].append(
            Definition.get(
                data_element="C507",
                component_element="2005M",
                attributes="an..3",
                data=elements[0][0],
            )
        )
        output["elements"].append(
            Definition.get(
                data_element="C507",
                component_element="2380M",
                attributes="n..10",
                data=elements[0][1],
            )
        )

        if e.struct(elements) == "list(list(str,str,str))":
            output["elements"].append(
                Definition.get(
                    data_element="C507",
                    component_element="2379C",
                    attributes="an..3",
                    data=elements[0][2],
                )
            )

        return output
