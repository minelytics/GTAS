from django.shortcuts import render
from django.views import View


class AirportCRUDView(View):
    template_view = "parent/airport.html"

    def get(self, request):
        return render(request, "parent/airport.html")


class AirportRestoreCRUDView(View):
    template_view = "parent/airport_restore.html"

    def get(self, request):
        return render(request, "parent/airport_restore.html")


class ApiAccessCRUDView(View):
    template_view = "parent/api_access.html"

    def get(self, request):
        return render(request, "parent/api_access.html")


class AppConfigurationCRUDView(View):
    template_view = "parent/app_configuration.html"

    def get(self, request):
        return render(request, "parent/app_configuration.html")


class AuditLogCRUDView(View):
    template_view = "parent/audit_log.html"

    def get(self, request):
        return render(request, "parent/audit_log.html")


class CarrierCRUDView(View):
    template_view = "parent/carrier.html"

    def get(self, request):
        return render(request, "parent/carrier.html")


class CarrierRestoreCRUDView(View):
    template_view = "parent/carrier_restore.html"

    def get(self, request):
        return render(request, "parent/carrier_restore.html")


class CodeShareFlightCRUDView(View):
    template_view = "parent/code_share_flight.html"

    def get(self, request):
        return render(request, "parent/code_share_flight.html")


class CountryCRUDView(View):
    template_view = "parent/country.html"

    def get(self, request):
        return render(request, "parent/country.html")


class CountryRestoreCRUDView(View):
    template_view = "parent/country_restore.html"

    def get(self, request):
        return render(request, "parent/country_restore.html")


class DwellTimeCRUDView(View):
    template_view = "parent/dwell_time.html"

    def get(self, request):
        return render(request, "parent/dwell_time.html")


class ErrorDetailCRUDView(View):
    template_view = "parent/error_detail.html"

    def get(self, request):
        return render(request, "parent/error_detail.html")


class FlightDirectionCRUDView(View):
    template_view = "parent/flight_direction.html"

    def get(self, request):
        return render(request, "parent/flight_direction.html")


class NoteTypeCRUDView(View):
    template_view = "parent/note_type.html"

    def get(self, request):
        return render(request, "parent/note_type.html")
