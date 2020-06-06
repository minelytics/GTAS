class EdifactGenerator:
    def generate_edifact(self, tag, elements):
        data = []
        for element in elements:
            if isinstance(element, list):
                temp = ":".join(element)
                data.append(str(temp))
            else:
                data.append(element)
        message = tag + "+" + "+".join(data) + "'"
        return message
