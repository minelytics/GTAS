class ElementsStructure:
    def __init__(self, elements):
        self.elements = elements

    @property
    def struct(self):
        structure = []
        if isinstance(self.elements, list):
            structure.append(type(self.elements).__name__ + "(")
            for element in self.elements:
                if isinstance(element, list):
                    structure.append(type(element).__name__ + "(")
                    for data in element:
                        structure.append(type(data).__name__ + ",")
                    structure.append("),")
                if isinstance(element, str):
                    structure.append(type(element).__name__ + ",")
            structure.append(")")
        return "".join(structure).replace(",)", ")")
