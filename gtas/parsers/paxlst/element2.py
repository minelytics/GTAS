class Element:
    @staticmethod
    def struct(elements):
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

   
    
