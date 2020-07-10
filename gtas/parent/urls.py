from django.urls import path
from rest_framework import routers

from gtas.parent.views.parent import AirportCRUDView
from gtas.parent.views.parent import AirportRestoreCRUDView
from gtas.parent.views.parent import ApiAccessCRUDView
from gtas.parent.views.parent import AppConfigurationCRUDView
from gtas.parent.views.parent import AuditLogCRUDView
from gtas.parent.views.parent import CarrierCRUDView
from gtas.parent.views.parent import CarrierRestoreCRUDView
from gtas.parent.views.parent import CodeShareFlightCRUDView
from gtas.parent.views.parent import CountryCRUDView
from gtas.parent.views.parent import CountryRestoreCRUDView
from gtas.parent.views.parent import DwellTimeCRUDView
from gtas.parent.views.parent import ErrorDetailCRUDView
from gtas.parent.views.parent import FlightDirectionCRUDView
from gtas.parent.views.parent import NoteTypeCRUDView

from gtas.parent.views.views import DashboardView
from gtas.parent.views.views import JsonView

app_name = "parent"

router = routers.DefaultRouter()

urlpatterns = [
    path("airport", AirportCRUDView.as_view(), name="airport_crud"),
    path(
        "airport_restore", AirportRestoreCRUDView.as_view(), name="airport_restore_crud"
    ),
    path("api_access", ApiAccessCRUDView.as_view(), name="api_access_crud"),
    path(
        "app_configuration",
        AppConfigurationCRUDView.as_view(),
        name="app_configuration_crud",
    ),
    path("audit_log", AuditLogCRUDView.as_view(), name="audit_log_crud"),
    path("carrier", CarrierCRUDView.as_view(), name="carrier_crud"),
    path(
        "carrier_restore", CarrierRestoreCRUDView.as_view(), name="carrier_restore_crud"
    ),
    path(
        "code_share_flight",
        CodeShareFlightCRUDView.as_view(),
        name="code_share_flight_crud",
    ),
    path("country", CountryCRUDView.as_view(), name="country_crud"),
    path(
        "country_restore", CountryRestoreCRUDView.as_view(), name="country_restore_crud"
    ),
    path("dwell_time", DwellTimeCRUDView.as_view(), name="dwell_time_crud"),
    path("error_detail", ErrorDetailCRUDView.as_view(), name="error_detail_crud"),
    path(
        "flight_direction",
        FlightDirectionCRUDView.as_view(),
        name="flight_direction_crud",
    ),
    path("note_type", NoteTypeCRUDView.as_view(), name="note_type_crud"),
    path("", DashboardView.as_view(), name="dashboard"),
    path("json/<str:name>", JsonView.as_view(), name="json"),
]
