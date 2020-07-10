from django.shortcuts import render
from django.views import View

from gtas.parent.forms.parent import AirportForm
from gtas.parent.forms.parent import AirportRestoreForm
from gtas.parent.forms.parent import ApiAccessForm
from gtas.parent.forms.parent import AppConfigurationForm
from gtas.parent.forms.parent import AuditLogForm
from gtas.parent.forms.parent import CarrierForm
from gtas.parent.forms.parent import CarrierRestoreForm
from gtas.parent.forms.parent import CodeShareFlightForm
from gtas.parent.forms.parent import CountryForm
from gtas.parent.forms.parent import CountryRestoreForm
from gtas.parent.forms.parent import DwellTimeForm
from gtas.parent.forms.parent import ErrorDetailForm
from gtas.parent.forms.parent import FlightDirectionForm
from gtas.parent.forms.parent import NoteTypeForm


class AirportCRUDView(View):
    template_view = "parent/airport.html"

    def get(self, request):
        form = AirportForm()
        return render(request, "parent/airport.html", {"form": form})


class AirportRestoreCRUDView(View):
    template_view = "parent/airport_restore.html"

    def get(self, request):
        form = AirportRestoreForm()
        return render(request, "parent/airport_restore.html", {"form": form})


class ApiAccessCRUDView(View):
    template_view = "parent/api_access.html"

    def get(self, request):
        form = ApiAccessForm()
        return render(request, "parent/api_access.html", {"form": form})


class AppConfigurationCRUDView(View):
    template_view = "parent/app_configuration.html"

    def get(self, request):
        form = AppConfigurationForm()
        return render(request, "parent/app_configuration.html", {"form": form})


class AuditLogCRUDView(View):
    template_view = "parent/audit_log.html"

    def get(self, request):
        form = AuditLogForm()
        return render(request, "parent/audit_log.html", {"form": form})


class CarrierCRUDView(View):
    template_view = "parent/carrier.html"

    def get(self, request):
        form = CarrierForm()
        return render(request, "parent/carrier.html", {"form": form})


class CarrierRestoreCRUDView(View):
    template_view = "parent/carrier_restore.html"

    def get(self, request):
        form = CarrierRestoreForm()
        return render(request, "parent/carrier_restore.html", {"form": form})


class CodeShareFlightCRUDView(View):
    template_view = "parent/code_share_flight.html"

    def get(self, request):
        form = CodeShareFlightForm()
        return render(request, "parent/code_share_flight.html", {"form": form})


class CountryCRUDView(View):
    template_view = "parent/country.html"

    def get(self, request):
        form = CountryForm()
        return render(request, "parent/country.html", {"form": form})


class CountryRestoreCRUDView(View):
    template_view = "parent/country_restore.html"

    def get(self, request):
        form = CountryRestoreForm()
        return render(request, "parent/country_restore.html", {"form": form})


class DwellTimeCRUDView(View):
    template_view = "parent/dwell_time.html"

    def get(self, request):
        form = DwellTimeForm()
        return render(request, "parent/dwell_time.html", {"form": form})


class ErrorDetailCRUDView(View):
    template_view = "parent/error_detail.html"

    def get(self, request):
        form = ErrorDetailForm()
        return render(request, "parent/error_detail.html", {"form": form})


class FlightDirectionCRUDView(View):
    template_view = "parent/flight_direction.html"

    def get(self, request):
        form = FlightDirectionForm()
        return render(request, "parent/flight_direction.html", {"form": form})


class NoteTypeCRUDView(View):
    template_view = "parent/note_type.html"

    def get(self, request):
        form = NoteTypeForm()
        return render(request, "parent/note_type.html", {"form": form})
