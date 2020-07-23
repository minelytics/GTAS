class Group:    
    @staticmethod
    def get(segment, group):
        switch = {
            "DTM": {
                "Segment Group 3": {
                    "segment_function": "Flight Leg Arrival/Departure",
                    "group_description": "Place/Location Identification",
                    "group_usage": "C",
                    "level": 3,
                    "usage": "C",
                    "max_use": 1,
                    "purpose": "A segment to specify associated dates and/or times as required related to locations.",
                    "elements": [],
                },
                "Segment Group 4": {
                    "segment_function": "Traveler Date of Birth",
                    "group_description": "Name and Address",
                    "group_usage": "C",
                    "level": 2,
                    "usage": "C",
                    "max_use": 1,
                    "purpose": "A segment to specify date of birth.",
                    "elements": [],
                },
                "Segment Group 5": {
                    "segment_function": "Traveler Document Expiration",
                    "group_description": "Document/Message Details",
                    "group_usage": "C",
                    "level": 3,
                    "usage": "C",
                    "max_use": 1,
                    "purpose": "A segment to specify associated dates/times related to documents.",
                    "elements": [],
                },
            }
        }
        return switch.get(segment, "Incorrect Segment: {}".format(segment)).get(
            group, "Incorrect Segment Group: {}".format(group)
        )
