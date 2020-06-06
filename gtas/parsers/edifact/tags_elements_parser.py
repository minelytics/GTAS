class TagsElementsParser:
    def parsed_output(self, messages):
        output = []
        for message in messages:
            temp = {}
            temp["tag"] = message["tag"]
            data = []
            if message["tag"] == "LOC":
                if message["elements"][0] == "125":
                    data.append({"DEPARTURE_AIRPORT": message["elements"][1]})
                elif message["elements"][0] == "87":
                    data.append({"ARRIVAL_AIRPORT": message["elements"][1]})
                elif message["elements"][0] == "92":
                    data.append({"BOTH_DEPARTURE_AND_ARRIVAL_AIRPORT": message["elements"][1]})
                elif message["elements"][0] == "130":
                    data.append({"FINAL_DESTINATION": message["elements"][1]})
                elif message["elements"][0] == "188":
                    data.append({"FILING_LOCATION": message["elements"][1]})
                elif message["elements"][0] == "172":
                    data.append({"REPORTING_LOCATION": message["elements"][1]})
                elif message["elements"][0] == "91":
                    data.append({"GATE_PASS_ISSUE_LOCATION": message["elements"][1]})
                elif message["elements"][0] == "22":
                    data.append({"AIRPORT_OF_FIRST_US_ARRIVAL": message["elements"][1]})
                elif message["elements"][0] == "174":
                    data.append({"COUNTRY_OF_RESIDENCE": message["elements"][1]})
                elif message["elements"][0] == "178":
                    data.append({"PORT_OF_EMBARKATION": message["elements"][1]})
                elif message["elements"][0] == "179":
                    data.append({"PORT_OF_DEBARKATION": message["elements"][1]})
                elif message["elements"][0] == "100":
                    data.append({"PLACE_OF_BIRTH": message["elements"][1]})
                else:
                    data.append({"Not Idetified": message["elements"][1]})

            temp["elements"] = data
            output.append(temp)
        return output
