from django.db import models
from gtas.admin.models.delete import SoftDeletionModel
import reversion

from gtas.apis.models import Flight
from gtas.users.models import User


@reversion.register()
class Airport(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    iata = models.CharField(max_length=3, blank=True, null=True)
    icao = models.CharField(max_length=4, blank=True, null=True)
    latitude = models.IntegerField(blank=True, null=True)
    longitude = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    originid = models.BigIntegerField(db_column='originId', blank=True, null=True)  # Field name made lowercase.
    timezone = models.CharField(max_length=255, blank=True, null=True)
    utc_offset = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'airport'


@reversion.register()
class AirportRestore(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    iata = models.CharField(max_length=3, blank=True, null=True)
    icao = models.CharField(max_length=4, blank=True, null=True)
    latitude = models.IntegerField(blank=True, null=True)
    longitude = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    timezone = models.CharField(max_length=255, blank=True, null=True)
    utc_offset = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'airport_restore'


@reversion.register()
class ApiAccess(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'api_access'


@reversion.register()
class AppConfiguration(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    opt = models.CharField(max_length=255, blank=True, null=True)
    val = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'app_configuration'


@reversion.register()
class AuditLog(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    action_data = models.CharField(max_length=10485760, blank=True, null=True)
    actionstatus = models.CharField(db_column='actionStatus', max_length=32)  # Field name made lowercase.
    action_type = models.CharField(max_length=32)
    action_message = models.CharField(max_length=255, blank=True, null=True)
    action_target = models.CharField(max_length=1024)
    timestamp = models.DateTimeField()
    user = models.ForeignKey(User, models.DO_NOTHING)
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'audit_log'


@reversion.register()
class Carrier(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    iata = models.CharField(max_length=2, blank=True, null=True)
    icao = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    originid = models.BigIntegerField(db_column='originId', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'carrier'


@reversion.register()
class CarrierRestore(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    iata = models.CharField(max_length=2, blank=True, null=True)
    icao = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'carrier_restore'


@reversion.register()
class Country(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    iso2 = models.CharField(max_length=2, blank=True, null=True)
    iso3 = models.CharField(max_length=3, blank=True, null=True)
    iso_numeric = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    originid = models.BigIntegerField(db_column='originId', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'country'


@reversion.register()
class CountryRestore(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    iso2 = models.CharField(max_length=2, blank=True, null=True)
    iso3 = models.CharField(max_length=3, blank=True, null=True)
    iso_numeric = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'country_restore'


@reversion.register()
class ErrorDetail(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    code = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    details = models.CharField(max_length=10485760, blank=True, null=True)
    timestamp = models.DateTimeField()
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'error_detail'


@reversion.register()
class FlightDirection(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    code = models.CharField(max_length=1)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'flight_direction'


@reversion.register()
class MutableFlightDetails(SoftDeletionModel):
    flight = models.OneToOneField(Flight, models.DO_NOTHING, primary_key=True)
    full_utc_eta_timestamp = models.DateTimeField(blank=True, null=True)
    eta_date = models.DateField(blank=True, null=True)
    full_utc_etd_timestamp = models.DateTimeField(blank=True, null=True)
    full_eta_timestamp = models.DateTimeField(blank=True, null=True)
    full_etd_timestamp = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'mutable_flight_details'


@reversion.register()
class NoteType(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    nt_type = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'note_type'
