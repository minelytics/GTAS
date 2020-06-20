class Base:
    def tag(self, data):
        return data.tag

    def parsed_message(self, sub_element, key, value, data):
        return {
            'tag': self.tag(data),
            'element': {
                sub_element: {
                    key: value
                }
            }
        }
