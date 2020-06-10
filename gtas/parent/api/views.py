from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.viewsets import ModelViewSet

from gtas.parent.models.parent import Airport
from gtas.parent.models.parent import AirportRestore
from gtas.parent.models.parent import ApiAccess
from gtas.parent.models.parent import AppConfiguration
from gtas.parent.models.parent import AuditLog
from gtas.parent.models.parent import Carrier
from gtas.parent.models.parent import CarrierRestore
from gtas.parent.models.parent import CodeShareFlight
from gtas.parent.models.parent import Country
from gtas.parent.models.parent import CountryRestore
from gtas.parent.models.parent import DwellTime
from gtas.parent.models.parent import ErrorDetail
from gtas.parent.models.parent import FlightDirection
from gtas.parent.models.parent import NoteType

from gtas.parent.api.serializers import AirportSerializer
from gtas.parent.api.serializers import AirportRestoreSerializer
from gtas.parent.api.serializers import ApiAccessSerializer
from gtas.parent.api.serializers import AppConfigurationSerializer
from gtas.parent.api.serializers import AuditLogSerializer
from gtas.parent.api.serializers import CarrierSerializer
from gtas.parent.api.serializers import CarrierRestoreSerializer
from gtas.parent.api.serializers import CodeShareFlightSerializer
from gtas.parent.api.serializers import CountrySerializer
from gtas.parent.api.serializers import CountryRestoreSerializer
from gtas.parent.api.serializers import DwellTimeSerializer
from gtas.parent.api.serializers import ErrorDetailSerializer
from gtas.parent.api.serializers import FlightDirectionSerializer
from gtas.parent.api.serializers import NoteTypeSerializer


class AirportViewSet(ModelViewSet):
    serializer_class = AirportSerializer
    queryset = Airport.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class AirportRestoreViewSet(ModelViewSet):
    serializer_class = AirportRestoreSerializer
    queryset = AirportRestore.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class ApiAccessViewSet(ModelViewSet):
    serializer_class = ApiAccessSerializer
    queryset = ApiAccess.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class AppConfigurationViewSet(ModelViewSet):
    serializer_class = AppConfigurationSerializer
    queryset = AppConfiguration.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class AuditLogViewSet(ModelViewSet):
    serializer_class = AuditLogSerializer
    queryset = AuditLog.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class CarrierViewSet(ModelViewSet):
    serializer_class = CarrierSerializer
    queryset = Carrier.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class CarrierRestoreViewSet(ModelViewSet):
    serializer_class = CarrierRestoreSerializer
    queryset = CarrierRestore.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class CodeShareFlightViewSet(ModelViewSet):
    serializer_class = CodeShareFlightSerializer
    queryset = CodeShareFlight.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class CountryViewSet(ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class CountryRestoreViewSet(ModelViewSet):
    serializer_class = CountryRestoreSerializer
    queryset = CountryRestore.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class DwellTimeViewSet(ModelViewSet):
    serializer_class = DwellTimeSerializer
    queryset = DwellTime.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class ErrorDetailViewSet(ModelViewSet):
    serializer_class = ErrorDetailSerializer
    queryset = ErrorDetail.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class FlightDirectionViewSet(ModelViewSet):
    serializer_class = FlightDirectionSerializer
    queryset = FlightDirection.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class NoteTypeViewSet(ModelViewSet):
    serializer_class = NoteTypeSerializer
    queryset = NoteType.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
