from gtas.parsers.paxlst.segment.base import Base
from datetime import datetime


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
        sub_element = key = value = None

        for element in data.elements:
            if isinstance(element, list):
                sub_element = element[0]
                key = self.datetime_function_code_qualifier(sub_element)

                if len(element) == 3:
                    value = self.get_datetime(element[1], element[2])
                elif len(element) == 2:
                    value = self.get_datetime(element[1])
            else:
                if len(data.elements) == 1:
                    sub_element = element
                    key = self.datetime_function_code_qualifier(element)

        return self.parsed_message(sub_element, key, value, data)
