# from pydifact.message import Message
# from pydifact.segments import Segment


class EdifactGenerator:
    def generate_edifact(self, tag, elements):
        # message = Message()
        data = []
        for element in elements:
            if isinstance(element, list):
                temp = ":".join(element)
                data.append(str(temp))
            else:
                data.append(element)
        # message.add_segment(Segment(tag, data))
        # return message.serialize().replace("?:", ":")
        message = tag + "+" + "+".join(data) + "'"
        return message

# tag = "UNB"
# elements = [['UNOA', '4'], ['SAMPLE CARRIER NAME', 'ZZ'], ['HDQCH2X', 'ZZ'], ['200506', '1700'], '123456789', '', 'PAXLST']
# gen = EdifactGenerator()
# message = gen.generate_edifact(tag, elements)
# print(message)
