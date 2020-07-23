class Element:
    def struct(self, elements):
        structure = []
        if isinstance(elements, list):
            structure.append(type(elements).__name__ + "(")
            for element in elements:
                if isinstance(element, list):
                    structure.append(type(element).__name__ + "(")
                    for data in element:
                        structure.append(type(data).__name__ + ",")
                    structure.append("),")
                if isinstance(element, str):
                    structure.append(type(element).__name__ + ",")
            structure.append(")")
        return "".join(structure).replace(",)", ")")

    def definition(
        self, data_element=None, component_element=None, attributes=None, data=None
    ):
        if data_element is None:
            description = self.description(component_element)
        else:
            description = self.description(":".join([data_element, component_element]))

        return {
            "data_element": data_element,
            "component_element": component_element,
            "attributes": attributes,
            "data": data,
            "description": description,
        }

    
