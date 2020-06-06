from django.db import models
from gtas.parent.models.delete import SoftDeletionModel
import reversion

from gtas.users.models import User


@reversion.register()
class Airport(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    iata = models.CharField(max_length=3, blank=True, null=True, db_index=True)
    icao = models.CharField(max_length=4, blank=True, null=True)
    latitude = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=6)
    longitude = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=6)
    name = models.CharField(max_length=255, blank=True, null=True)
    origin_id = models.BigIntegerField(blank=True, null=True)
    timezone = models.CharField(max_length=255, blank=True, null=True)
    utc_offset = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'airport'


@reversion.register()
class AirportRestore(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    iata = models.CharField(max_length=3, blank=True, null=True, db_index=True)
    icao = models.CharField(max_length=4, blank=True, null=True)
    latitude = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=6)
    longitude = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=6)
    name = models.CharField(max_length=255, blank=True, null=True)
    timezone = models.CharField(max_length=255, blank=True, null=True)
    utc_offset = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'airport_restore'


@reversion.register()
class ApiAccess(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'api_access'


@reversion.register()
class AppConfiguration(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    opt = models.CharField(max_length=255, blank=True, null=True)
    val = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'app_configuration'


@reversion.register()
class AuditLog(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    action_data = models.CharField(max_length=10485760, blank=True, null=True)
    action_status = models.CharField(max_length=32)
    action_type = models.CharField(max_length=32)
    action_message = models.CharField(max_length=255, blank=True, null=True)
    action_target = models.CharField(max_length=1024)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'audit_log'


@reversion.register()
class Carrier(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    iata = models.CharField(max_length=2, blank=True, null=True, db_index=True)
    icao = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    origin_id = models.BigIntegerField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'carrier'


@reversion.register()
class CarrierRestore(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    iata = models.CharField(max_length=2, blank=True, null=True, db_index=True)
    icao = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'carrier_restore'


@reversion.register()
class CodeShareFlight(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    marketing_flight_number = models.CharField(max_length=255, blank=True, null=True)
    operating_flight_id = models.BigIntegerField(blank=True, null=True)
    operating_flight_number = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'code_share_flight'


@reversion.register()
class Country(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    iso2 = models.CharField(max_length=2, blank=True, null=True)
    iso3 = models.CharField(max_length=3, blank=True, null=True, db_index=True)
    iso_numeric = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    origin_id = models.BigIntegerField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'country'


@reversion.register()
class CountryRestore(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    iso2 = models.CharField(max_length=2, blank=True, null=True)
    iso3 = models.CharField(max_length=3, blank=True, null=True, db_index=True)
    iso_numeric = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'country_restore'


@reversion.register()
class DwellTime(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    arrival_time = models.DateTimeField(blank=True, null=True)
    departure_at = models.DateTimeField(blank=True, null=True)
    dwell_time = models.FloatField(blank=True, null=True)
    flying_from = models.CharField(max_length=255, blank=True, null=True)
    flying_to = models.CharField(max_length=255, blank=True, null=True)
    arrival_airport = models.CharField(max_length=3, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'dwell_time'


@reversion.register()
class ErrorDetail(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    details = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'error_detail'


@reversion.register()
class FlightDirection(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=1)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'flight_direction'


@reversion.register()
class NoteType(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    nt_type = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                   related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'note_type'
