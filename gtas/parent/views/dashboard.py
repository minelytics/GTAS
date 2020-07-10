from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse


class DashboardView(LoginRequiredMixin, View):
    """roles: [USER_ROLES.ADMIN, USER_ROLES.VIEW_FLIGHT_PASSENGERS, USER_ROLES.MANAGE_QUERIES, USER_ROLES.MANAGE_RULES, USER_ROLES.MANAGE_WATCHLIST]"""

    def get(self, request):
        kibana_url = "https://get_kibana_url"

        rule_list = [
            {
                "rule_name": "N-SSA-m8992",
                "rule_hits": "556",
                "created_on": "1990-01-12",
            },
            {
                "rule_name": "N-SSA-c4592",
                "rule_hits": "767",
                "created_on": "1990-01-12",
            },
        ]

        airport_stats = [
            {
                "airport": "ORD",
                "flights": "440,210",
                "watch_list_hits": "52256",
                "rule_hits": "5560",
            },
            {
                "airport": "BOS",
                "flights": "323,210",
                "watch_list_hits": "52256",
                "rule_hits": "5560",
            },
        ]

        context = {
            "kibana_url": kibana_url,
            "rules_list": rule_list,
            "airport_stats": airport_stats,
        }

        return render(request, "dashboards/dashboard.html", context)


class DashboardServiceView(LoginRequiredMixin, View):
    def get(self, request, service):

        # TODO: Add start_date and end_date parameters for functions:
        #   get_flights_and_passengers_and_hits_count()
        #   get_flights_and_passengers_and_hits_count_inbound()
        #   get_flights_and_passengers_and_hits_count_outbound()
        #   get_messages_count()

        switch = {
            "get_flights_and_passengers_and_hits_count": self.get_flights_and_passengers_and_hits_count(),
            "get_flights_and_passengers_and_hits_count_inbound": self.get_flights_and_passengers_and_hits_count_inbound(),
            "get_flights_and_passengers_and_hits_count_outbound": self.get_flights_and_passengers_and_hits_count_outbound(),
            "get_messages_count": self.get_messages_count(),
            "get_ytd_rules_count": self.get_ytd_rules_count(),
            "get_ytd_airport_stats": self.get_ytd_airport_stats(),
        }

        return JsonResponse(
            {
                service: switch.get(
                    service, "Service not available for the parameter: " + service
                )
            },
            safe=False,
        )

    def get_flights_and_passengers_and_hits_count(self):
        return [{"service": "get_flights_and_passengers_and_hits_count"}]

    def get_flights_and_passengers_and_hits_count_inbound(self):
        """Pushing data to AmCharts"""
        return [{"service": "get_flights_and_passengers_and_hits_count_inbound"}]

    def get_flights_and_passengers_and_hits_count_outbound(self):
        """Pushing data to AmCharts"""
        return [{"service": "get_flights_and_passengers_and_hits_count_outbound"}]

    def get_messages_count(self):
        return [{"service": "get_messages_count"}]

    def get_ytd_rules_count(self):
        return [{"service": "get_ytd_rules_count"}]

    def get_ytd_airport_stats(self):
        return [{"service": "get_ytd_airport_stats"}]


class JsonView(LoginRequiredMixin, View):
    def get(self, request, name):

        switch = {
            "passengers_type": self.passengers_type(),
            "doc_types": self.doc_types(),
            "genders": self.genders(),
            "dictionary": self.dictionary(),
        }

        return JsonResponse(
            {name: switch.get(name, "Json not available for the parameter: " + name)},
            safe=False,
        )

    def passengers_type(self):
        return [
            {"id": "P", "name": "Passenger"},
            {"id": "C", "name": "Crew"},
            {"id": "I", "name": "Intransit"},
        ]

    def doc_types(self):
        return [
            {"id": "P", "name": "P"},
            {"id": "V", "name": "V"},
            {"id": "IP", "name": "IP"},
            {"id": "A", "name": "A"},
            {"id": "C", "name": "C"},
            {"id": "I", "name": "I"},
            {"id": "F", "name": "F"},
        ]

    def genders(self):
        return [
            {"id": "F", "name": "Female"},
            {"id": "M", "name": "Male"},
            {"id": "U", "name": "Undisclosed"},
            {"id": "FI", "name": "Female Infant"},
            {"id": "MI", "name": "Male Infant"},
        ]

    def dictionary(self):
        return [
            {"id": "PNR", "definition": "Passenger's Name Record"},
            {"id": "equal", "definition": "Equals"},
            {"id": "ETA", "definition": "Estimated Time of Arrival"},
            {"id": "ETD", "definition": "Estimated Time of Departure"},
            {"id": "P", "definition": "Passport"},
            {"id": "V", "definition": "Visa"},
            {"id": "IP", "definition": "Passport Card"},
            {"id": "A", "definition": "Identity Card"},
            {"id": "C", "definition": "Identity Card"},
            {"id": "I", "definition": "Identity Card"},
            {
                "id": "F",
                "definition": "Approved non-standard identity documents used for travel",
            },
        ]
