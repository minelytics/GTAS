from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from gtas.users.api.views import UserViewSet

from gtas.parent.api.views import AirportViewSet
from gtas.parent.api.views import AirportRestoreViewSet
from gtas.parent.api.views import ApiAccessViewSet
from gtas.parent.api.views import AppConfigurationViewSet
from gtas.parent.api.views import AuditLogViewSet
from gtas.parent.api.views import CarrierViewSet
from gtas.parent.api.views import CarrierRestoreViewSet
from gtas.parent.api.views import CodeShareFlightViewSet
from gtas.parent.api.views import CountryViewSet
from gtas.parent.api.views import CountryRestoreViewSet
from gtas.parent.api.views import DwellTimeViewSet
from gtas.parent.api.views import ErrorDetailViewSet
from gtas.parent.api.views import FlightDirectionViewSet
from gtas.parent.api.views import NoteTypeViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

router.register("airport", AirportViewSet)
router.register("airport_restore", AirportRestoreViewSet)
router.register("api_access", ApiAccessViewSet)
router.register("app_configuration", AppConfigurationViewSet)
router.register("audit_log", AuditLogViewSet)
router.register("carrier", CarrierViewSet)
router.register("carrier_restore", CarrierRestoreViewSet)
router.register("code_share_flight", CodeShareFlightViewSet)
router.register("country", CountryViewSet)
router.register("country_restore", CountryRestoreViewSet)
router.register("dwell_time", DwellTimeViewSet)
router.register("error_detail", ErrorDetailViewSet)
router.register("flight_direction", FlightDirectionViewSet)
router.register("note_type", NoteTypeViewSet)


app_name = "api"
urlpatterns = router.urls
