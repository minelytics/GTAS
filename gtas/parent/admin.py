from django.contrib import admin
from reversion.admin import VersionAdmin

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


@admin.register(Airport)
class AirportAdmin(VersionAdmin):
    """Admin class for Airport"""

    exclude = ('created_by', 'updated_by', 'deleted_at')
    list_display = ('city', 'country', 'iata', 'icao', 'latitude', 'longitude', 'name', 'origin_id', 'timezone', 'utc_offset')
    list_filter = ('updated_at',)
    ordering = ('name',)
    search_fields = ('city', 'country')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user.id
        obj.updated_by = request.user.id
        super().save_model(request, obj, form, change)


@admin.register(AirportRestore)
class AirportRestoreAdmin(VersionAdmin):
    """Admin class for AirportRestore"""

    exclude = ('created_by', 'updated_by', 'deleted_at')
    list_display = ('city', 'country', 'iata', 'icao', 'latitude', 'longitude', 'name', 'timezone', 'utc_offset')
    list_filter = ('updated_at',)
    ordering = ('name',)
    search_fields = ('city', 'country')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user.id
        obj.updated_by = request.user.id
        super().save_model(request, obj, form, change)


@admin.register(ApiAccess)
class ApiAccessAdmin(VersionAdmin):
    """Admin class for ApiAccess"""

    exclude = ('created_by', 'updated_by', 'deleted_at')
    list_display = ('email', 'organization', 'password', 'username')
    list_filter = ('updated_at',)
    ordering = ('username',)
    search_fields = ('email', 'organization',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user.id
        obj.updated_by = request.user.id
        super().save_model(request, obj, form, change)


@admin.register(AppConfiguration)
class AppConfigurationAdmin(VersionAdmin):
    """Admin class for AppConfiguration"""

    exclude = ('created_by', 'updated_by', 'deleted_at')
    list_display = ('description', 'opt', 'val')
    list_filter = ('updated_at',)
    ordering = ('val',)
    search_fields = ('description',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user.id
        obj.updated_by = request.user.id
        super().save_model(request, obj, form, change)


@admin.register(AuditLog)
class AuditLogAdmin(VersionAdmin):
    """Admin class for AuditLog"""

    exclude = ('created_by', 'updated_by', 'deleted_at')
    list_display = ('action_data', 'action_status', 'action_type', 'action_message', 'action_target')
    list_filter = ('updated_at',)
    ordering = ('action_status',)
    search_fields = ('action_type', 'action_message')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user.id
        obj.updated_by = request.user.id
        super().save_model(request, obj, form, change)


@admin.register(Carrier)
class CarrierAdmin(VersionAdmin):
    """Admin class for Carrier"""

    exclude = ('created_by', 'updated_by', 'deleted_at')
    list_display = ('iata', 'icao', 'name', 'origin_id')
    list_filter = ('updated_at',)
    ordering = ('name',)
    search_fields = ('iata', 'icao')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user.id
        obj.updated_by = request.user.id
        super().save_model(request, obj, form, change)


@admin.register(CarrierRestore)
class CarrierRestoreAdmin(VersionAdmin):
    """Admin class for CarrierRestore"""

    exclude = ('created_by', 'updated_by', 'deleted_at')
    list_display = ('iata', 'icao', 'name')
    list_filter = ('updated_at',)
    ordering = ('name',)
    search_fields = ('iata', 'icao')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user.id
        obj.updated_by = request.user.id
        super().save_model(request, obj, form, change)


@admin.register(CodeShareFlight)
class CodeShareFlightAdmin(VersionAdmin):
    """Admin class for CodeShareFlight"""

    exclude = ('created_by', 'updated_by', 'deleted_at')
    list_display = ('marketing_flight_number', 'operating_flight_id', 'operating_flight_number')
    list_filter = ('updated_at',)
    ordering = ('operating_flight_number',)
    search_fields = ('operating_flight_number',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user.id
        obj.updated_by = request.user.id
        super().save_model(request, obj, form, change)


@admin.register(Country)
class CountryAdmin(VersionAdmin):
    """Admin class for Country"""

    exclude = ('created_by', 'updated_by', 'deleted_at')
    list_display = ('iso2', 'iso3', 'iso_numeric', 'name', 'origin_id')
    list_filter = ('updated_at',)
    ordering = ('name',)
    search_fields = ('iso2', 'iso3', 'iso_numeric')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user.id
        obj.updated_by = request.user.id
        super().save_model(request, obj, form, change)


@admin.register(CountryRestore)
class CountryRestoreAdmin(VersionAdmin):
    """Admin class for CountryRestore"""

    exclude = ('created_by', 'updated_by', 'deleted_at')
    list_display = ('iso2', 'iso3', 'iso_numeric', 'name')
    list_filter = ('updated_at',)
    ordering = ('name',)
    search_fields = ('iso2', 'iso3', 'iso_numeric')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user.id
        obj.updated_by = request.user.id
        super().save_model(request, obj, form, change)


@admin.register(DwellTime)
class DwellTimeAdmin(VersionAdmin):
    """Admin class for DwellTime"""

    exclude = ('created_by', 'updated_by', 'deleted_at')
    list_display = ('arrival_time', 'departure_at', 'dwell_time', 'flying_from', 'flying_to', 'arrival_airport')
    list_filter = ('updated_at',)
    ordering = ('flying_from', 'flying_to')
    search_fields = ('flying_from', 'flying_to')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user.id
        obj.updated_by = request.user.id
        super().save_model(request, obj, form, change)


@admin.register(ErrorDetail)
class ErrorDetailAdmin(VersionAdmin):
    """Admin class for ErrorDetail"""

    exclude = ('created_by', 'updated_by', 'deleted_at')
    list_display = ('code', 'description', 'details')
    list_filter = ('updated_at',)
    ordering = ('code',)
    search_fields = ('code', 'description')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user.id
        obj.updated_by = request.user.id
        super().save_model(request, obj, form, change)


@admin.register(FlightDirection)
class FlightDirectionAdmin(VersionAdmin):
    """Admin class for FlightDirection"""

    exclude = ('created_by', 'updated_by', 'deleted_at')
    list_display = ('code', 'description')
    list_filter = ('updated_at',)
    ordering = ('code',)
    search_fields = ('code', 'description')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user.id
        obj.updated_by = request.user.id
        super().save_model(request, obj, form, change)


@admin.register(NoteType)
class NoteTypeAdmin(VersionAdmin):
    """Admin class for NoteType"""

    exclude = ('created_by', 'updated_by', 'deleted_at')
    list_display = ('nt_type',)
    list_filter = ('updated_at',)
    ordering = ('nt_type',)
    search_fields = ('nt_type',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user.id
        obj.updated_by = request.user.id
        super().save_model(request, obj, form, change)
