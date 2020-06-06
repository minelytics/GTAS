from pydifact.message import Message


class EdifactParser:
    def message_input(self, filename):
        file = open(filename, "r")
        lines = file.readlines()
        message = []
        for line in lines:
            message.append(line.replace("\n", ""))
        file.close()
        return message

    def get_parsed_message(self, filename):
        parsed_message = []
        messages = self.message_input(filename)
        for message in messages:
            collection = Message.from_str(message)

            for segment in collection.segments:
                elements = []
                temp = {}
                for element in segment.elements:
                    elements.append(element)

                temp["tag"] = segment.tag
                temp["elements"] = elements

                parsed_message.append(temp)
        return parsed_message
