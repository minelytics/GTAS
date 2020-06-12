from rest_framework import serializers

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


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = (
        'id', 'city', 'country', 'iata', 'icao', 'latitude', 'longitude', 'name', 'origin_id', 'timezone', 'utc_offset')


class AirportRestoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirportRestore
        fields = ('id', 'city', 'country', 'iata', 'icao', 'latitude', 'longitude', 'name', 'timezone', 'utc_offset')


class ApiAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiAccess
        fields = ('id', 'email', 'organization', 'password', 'username')


class AppConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppConfiguration
        fields = ('id', 'description', 'opt', 'val')


class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = ('id', 'action_data', 'action_status', 'action_type', 'action_message', 'action_target')


class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = ('id', 'iata', 'icao', 'name', 'origin_id')


class CarrierRestoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarrierRestore
        fields = ('id', 'iata', 'icao', 'name')


class CodeShareFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeShareFlight
        fields = ('id', 'marketing_flight_number', 'operating_flight_id', 'operating_flight_number')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'iso2', 'iso3', 'iso_numeric', 'name', 'origin_id')


class CountryRestoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryRestore
        fields = ('id', 'iso2', 'iso3', 'iso_numeric', 'name')


class DwellTimeSerializer(serializers.ModelSerializer):
    arrival_time = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M", input_formats=['%Y-%m-%d %H:%M'])
    departure_at = serializers.DateTimeField(default=None, format="%Y-%m-%d %H:%M", input_formats=['%Y-%m-%d %H:%M'])

    class Meta:
        model = DwellTime
        fields = ('id', 'arrival_time', 'departure_at', 'dwell_time', 'flying_from', 'flying_to', 'arrival_airport')


class ErrorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorDetail
        fields = ('id', 'code', 'description', 'details')


class FlightDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightDirection
        fields = ('id', 'code', 'description')


class NoteTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteType
        fields = ('id', 'nt_type')
