from datetime import datetime


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


class ATT(Base):
    def attribute_function_code_qualifier(self, val):
        switch = {
            "2": "GENDER"
        }
        return switch.get(val, "ATT Unknown Attribute Function Code Qualifier: " + val)

    def process(self, data):
        sub_element = data.elements[0]
        key = self.attribute_function_code_qualifier(sub_element)
        value = data.elements[2]

        return self.parsed_message(sub_element, key, value, data)


class BGM(Base):
    def document_name_code(self, val):
        switch = {
            "745": "PASSENGER_LIST",
            "250": "CREW_LIST",
            "266": "FLIGHT_STATUS_UPDATE",
            "336": "MASTER_CREW_LIST",
            "655": "GATE_PASS_REQUEST"
        }
        return switch.get(val, "BGM Unknown Document Name Code: " + val)

    def document_identifier(self, val):
        switch = {
            # PASSENGER_LIST
            "CP": "CHANGE_PAX_DATA",
            "XR": "CANCEL_RESERVATION",
            "RP": "REDUCTION_IN_PARTY",

            # FLIGHT_STATUS_UPDATE
            "CL": "FLIGHT_CLOSE",
            "CLNB": "FLIGHT_CLOSE_WITH_PAX_NOT_ON_BOARD",
            "CLOB": "FLIGHT_CLOSE_WITH_PAX_ON_BOARD",
            "XF": "CANCEL_FLIGHT",
            "CF": "CHANGE_FLIGHT",

            # CREW_LIST
            "C": "PASSENGER_FLIGHT_REGULAR_SCHEDULED_CREW",
            "CC": "PASSENGER_FLIGHT_CREW_CHANGE",
            "B": "CARGO_FLIGHT_REGULAR_SCHEDULED_CREW",
            "BC": "CARGO_FLIGHT_CREW_CHANGE",
            "A": "OVERFLIGHT_OF_PASSENGER_FLIGHT",
            "D": "OVERFLIGHT_OF_CARGO_FLIGHT",
            "E": "DOMESTIC_CONTINUANCE_OF_PASSENGER_FLIGHT_REGULAR_SCHEDULED_CREW",
            "EC": "DOMESTIC_CONTINUANCE_OF_PASSENGER_FLIGHT_CREW_CHANGE",
            "F": "DOMESTIC_CONTINUANCE_OF_CARGO_FLIGHT_REGULAR_SCHEDULED_CREW",
            "FC": "DOMESTIC_CONTINUANCE_OF_CARGO_FLIGHT_CREW_CHANGE",

            # MASTER_CREW_LIST
            "G": "ADD",
            "H": "DELETE",
            "I": "CHANGE"
        }
        return switch.get(val, "BGM Unknown Document Identifier: " + val)

    def process(self, data):
        sub_element = None
        key = None
        value = None

        if len(data.elements) == 1:
            sub_element = data.elements[0]
            key = self.document_name_code(sub_element)
            value = "No Document Identifier used"
        elif len(data.elements) == 2:
            sub_element = data.elements[0]
            key = self.document_name_code(sub_element)
            value = self.document_identifier(data.elements[1])

        return self.parsed_message(sub_element, key, value, data)


class CNT(Base):
    def control_total_type_code_qualifier(self, val):
        switch = {
            "41": "TOTAL_PASSENGERS",
            "42": "TOTAL_CREW_MEMBERS"
        }
        return switch.get(val, "CNT Unknown Control Total Type Code Qualifier: " + val)

    def process(self, data):
        sub_element = key = value = None
        # key = None
        # value = None

        for element in data.elements:
            if isinstance(element, list):
                if len(element) == 2:
                    sub_element = element[0]
                    key = self.control_total_type_code_qualifier(sub_element)
                    value = element[1]

        return self.parsed_message(sub_element, key, value, data)


class COM(Base):
    def communication_address_code_qualifier(self, val):
        switch = {
            "TE": "TELEPHONE",
            "FX": "TELEFAX",
            "EM": "EMAIL"
        }
        return switch.get(val, "COM Unknown Communication Address Code Qualifier: " + val)

    def process(self, data):
        temp = {"tag": "COM", "element": {}}
        for element in data.elements:
            if isinstance(element, list):
                sub_element = element[1]
                key = self.communication_address_code_qualifier(sub_element)
                value = element[0]

                if len(data.elements) == 1:
                    return self.parsed_message(sub_element, key, value, data)
                elif len(data.elements) > 1:
                    temp["element"].update({sub_element: {key: value}})
        return temp


class DTM(Base):
    def get_datetime(self, dt, code=None):
        if code == "201":
            ft_in = "%y%m%d%H%M"
            ft_out = "%Y-%m-%d %H:%M"
        else:
            ft_out = "%Y-%m-%d"
            if 1 <= int(dt[:2]) <= 31:
                ft_in = "%d%m%y"
            else:
                ft_in = "%y%m%d"
        return datetime.strptime(dt, ft_in).strftime(ft_out)

    def datetime_function_code_qualifier(self, val):
        switch = {
            "189": "DEPARTURE_DATETIME",
            "232": "ARRIVAL_DATETIME",
            "554": "DEPARTURE_ARRIVAL_DATETIME_MCL",
            "329": "DATE_OF_BIRTH",
            "36": "PASSPORT_EXPIRATION_DATE"
        }
        return switch.get(val, "DTM Unknown Datetime Function Code Qualifier: " + val)

    def process(self, data):
        sub_element = None
        key = None
        value = None

        for element in data.elements:
            if isinstance(element, list):
                if len(element) == 3:
                    sub_element = element[0]
                    key = self.datetime_function_code_qualifier(sub_element)
                    value = self.get_datetime(element[1], element[2])
                if len(element) == 2:
                    sub_element = element[0]
                    key = self.datetime_function_code_qualifier(sub_element)
                    value = self.get_datetime(element[1])
                else:
                    pass
            else:
                if len(data.elements) == 1:
                    sub_element = element
                    key = self.datetime_function_code_qualifier(element)

        return self.parsed_message(sub_element, key, value, data)


class LOC(Base):
    def location_function_code_qualifier(self, val):
        switch = {
            "125": "DEPARTURE_AIRPORT",
            "87": "ARRIVAL_AIRPORT",
            "92": "BOTH_DEPARTURE_AND_ARRIVAL_AIRPORT",
            "130": "FINAL_DESTINATION",
            "188": "FILING_LOCATION",
            "172": "REPORTING_LOCATION",
            "91": "GATE_PASS_ISSUE_LOCATION",
            "22": "AIRPORT_OF_FIRST_US_ARRIVAL",
            "174": "COUNTRY_OF_RESIDENCE",
            "178": "PORT_OF_EMBARKATION",
            "179": "PORT_OF_DEBARKATION",
            "180": "PLACE_OF_BIRTH"
        }
        return switch.get(val, "LOC Unknown Location Function Code Qualifier: " + val)

    def process(self, data):
        sub_element = data.elements[0]
        key = self.location_function_code_qualifier(data.elements[0])
        value = data.elements[1]

        return self.parsed_message(sub_element, key, value, data)
