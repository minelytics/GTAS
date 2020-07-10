from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse


class DashboardView(LoginRequiredMixin, View):
    template_name = "parent/dashboard.html"

    def get(self, request):
        return render(request, "parent/dashboard.html")


class JsonView(LoginRequiredMixin, View):
    def get(self, request, name):

        switch = {
            "passengers_type": self.passengers_type(),
            "doc_types": self.doc_types(),
            "genders": self.genders(),
            "dictionary": self.dictionary(),
        }

        return JsonResponse(
            switch.get(name, "Json not available for the parameter: " + name),
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
