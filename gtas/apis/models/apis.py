from django.db import models
from gtas.apis.models.delete import SoftDeletionModel
import reversion

from gtas.users.models import User

from gtas.users.models.users import UserGroup
from gtas.parent.models.parent import CodeShareFlight
from gtas.parent.models.parent import DwellTime
from gtas.parent.models import NoteType
from gtas.watch.models import HitMaker


@reversion.register()
class Flight(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    carrier = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    destination_country = models.CharField(max_length=3, blank=True, null=True)
    direction = models.CharField(max_length=1)
    etd_date = models.DateField(blank=True, null=True)
    flight_number = models.CharField(max_length=4)
    full_flight_number = models.CharField(max_length=255, blank=True, null=True)
    id_tag = models.CharField(max_length=255, blank=True, null=True)
    origin = models.CharField(max_length=255)
    origin_country = models.CharField(max_length=3, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'flight'


@reversion.register()
class Passenger(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'passenger'


@reversion.register()
class Message(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    create_date = models.DateTimeField()
    error = models.CharField(max_length=4000, blank=True, null=True)
    file_path = models.CharField(max_length=255)
    hash_code = models.CharField(max_length=255, blank=True, null=True)
    passenger_count = models.IntegerField(blank=True, null=True)
    raw = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'message'


@reversion.register()
class ReportingParty(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    party_name = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'reporting_party'


@reversion.register()
class Address(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    flight = models.ForeignKey(Flight, models.DO_NOTHING, blank=True, null=True)
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255, blank=True, null=True)
    line3 = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'address'


@reversion.register()
class Agency(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'agency'


@reversion.register()
class FlightPax(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    average_bag_weight = models.FloatField(blank=True, null=True)
    bag_count = models.IntegerField(blank=True, null=True)
    bag_weight = models.FloatField(blank=True, null=True)
    debarkation = models.CharField(max_length=255, blank=True, null=True)
    deb_country = models.CharField(max_length=255, blank=True, null=True)
    embarkation = models.CharField(max_length=255, blank=True, null=True)
    emb_country = models.CharField(max_length=255, blank=True, null=True)
    flight = models.ForeignKey(Flight, models.DO_NOTHING, blank=True, null=True)
    head_of_pool = models.CharField(max_length=1, blank=True, null=True)
    msg_source = models.CharField(max_length=255, blank=True, null=True)
    passenger = models.ForeignKey(Passenger, models.DO_NOTHING, blank=True, null=True)
    first_arrival_port = models.CharField(max_length=255, blank=True, null=True)
    ref_number = models.CharField(max_length=255, blank=True, null=True)
    residence_country = models.CharField(max_length=255, blank=True, null=True)
    traveler_type = models.CharField(max_length=255, blank=True, null=True)
    install_address = models.ForeignKey(Address, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'flight_pax'


@reversion.register()
class ApisMessage(SoftDeletionModel):
    id = models.OneToOneField(Message, models.DO_NOTHING, primary_key=True)
    message_type = models.CharField(max_length=10, blank=True, null=True)
    transmission_date = models.DateTimeField(blank=True, null=True)
    transmission_source = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=10, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'apis_message'


@reversion.register()
class ApisMessageFlight(SoftDeletionModel):
    apis_message = models.OneToOneField(ApisMessage, models.DO_NOTHING)
    flight = models.ForeignKey(Flight, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'apis_message_flight'
        constraints = [models.UniqueConstraint(fields=['apis_message', 'flight'],
                                               name='unique_apis_message_flight')]


@reversion.register()
class ApisMessageFlightPax(SoftDeletionModel):
    apis_message = models.OneToOneField(ApisMessage, models.DO_NOTHING)
    flight_pax = models.ForeignKey(FlightPax, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'apis_message_flight_pax'
        constraints = [models.UniqueConstraint(fields=['apis_message', 'flight_pax'],
                                               name='unique_apis_message_flight_pax')]


@reversion.register()
class ApisMessagePassenger(SoftDeletionModel):
    apis_message = models.OneToOneField(ApisMessage, models.DO_NOTHING)
    passenger = models.ForeignKey(Passenger, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'apis_message_passenger'
        constraints = [models.UniqueConstraint(fields=['apis_message', 'passenger'],
                                               name='unique_apis_message_passenger')]


@reversion.register()
class ApisMessageReportingParty(SoftDeletionModel):
    apis_message = models.OneToOneField(ApisMessage, models.DO_NOTHING)
    reporting_party = models.ForeignKey(ReportingParty, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'apis_message_reporting_party'
        constraints = [models.UniqueConstraint(fields=['apis_message', 'reporting_party'],
                                               name='unique_apis_message_reporting_party')]


@reversion.register()
class ApisPhone(SoftDeletionModel):
    apis_message = models.OneToOneField(ApisMessage, models.DO_NOTHING)
    phone = models.ForeignKey('Phone', models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'apis_phone'
        constraints = [models.UniqueConstraint(fields=['apis_message', 'phone'],
                                               name='unique_apis_message_phone')]


@reversion.register()
class Attachment(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    content = models.BinaryField(blank=True, null=True)
    content_type = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    passenger = models.ForeignKey(Passenger, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'attachment'


@reversion.register()
class BagMeasurements(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    bag_count = models.IntegerField(blank=True, null=True)
    initial_measurement_in = models.CharField(max_length=255, blank=True, null=True)
    raw_weight_from_message = models.FloatField(blank=True, null=True)
    bag_weight_in_kilos = models.FloatField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'bag_measurements'


@reversion.register()
class Bag(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    airline = models.CharField(max_length=255, blank=True, null=True)
    bag_identification = models.CharField(max_length=255)
    bag_serial_count = models.CharField(max_length=255, blank=True, null=True)
    destination_country = models.CharField(max_length=255, blank=True, null=True)
    data_source = models.CharField(max_length=255, blank=True, null=True)
    destination_city = models.CharField(max_length=255, blank=True, null=True)
    destination_airport = models.CharField(max_length=255, blank=True, null=True)
    flight = models.ForeignKey(Flight, models.DO_NOTHING, blank=True, null=True)
    head_pool = models.CharField(max_length=1, blank=True, null=True)
    member_pool = models.CharField(max_length=1, blank=True, null=True)
    passenger = models.ForeignKey(Passenger, models.DO_NOTHING, blank=True, null=True)
    prime_flight = models.CharField(max_length=1, blank=True, null=True)
    bag_measurements = models.ForeignKey(BagMeasurements, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'bag'

@reversion.register()
class BookingDetail(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    destination = models.CharField(max_length=255)
    destination_country = models.CharField(max_length=3, blank=True, null=True)
    eta = models.DateTimeField(blank=True, null=True)
    eta_date = models.DateField(blank=True, null=True)
    etd = models.DateTimeField(blank=True, null=True)
    etd_date = models.DateField(blank=True, null=True)
    flight = models.ForeignKey(Flight, models.DO_NOTHING, blank=True, null=True)
    flight_number = models.CharField(max_length=4)
    full_flight_number = models.CharField(max_length=255, blank=True, null=True)
    local_eta = models.DateTimeField(blank=True, null=True)
    local_etd = models.DateTimeField(blank=True, null=True)
    origin = models.CharField(max_length=255)
    origin_country = models.CharField(max_length=3, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'booking_detail'


@reversion.register()
class BagBdJoin(SoftDeletionModel):
    bag = models.OneToOneField(Bag, models.DO_NOTHING)
    bd = models.ForeignKey(BookingDetail, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'bag_bd_join'
        constraints = [models.UniqueConstraint(fields=['bag', 'bd'],
                                               name='unique_bag_bd')]



@reversion.register()
class CreditCard(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    account_holder = models.CharField(max_length=255, blank=True, null=True)
    account_holder_address = models.CharField(max_length=255, blank=True, null=True)
    account_holder_phone = models.CharField(max_length=255, blank=True, null=True)
    card_type = models.CharField(max_length=255, blank=True, null=True)
    expiration = models.DateField(blank=True, null=True)
    flight = models.ForeignKey(Flight, models.DO_NOTHING, blank=True, null=True)
    number = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'credit_card'


@reversion.register()
class Document(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    document_number = models.CharField(max_length=255, blank=True, null=True)
    document_type = models.CharField(max_length=3, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    issuance_country = models.CharField(max_length=255, blank=True, null=True)
    issuance_date = models.DateField(blank=True, null=True)
    days_valid = models.IntegerField(blank=True, null=True)
    passenger = models.ForeignKey(Passenger, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'document'


@reversion.register()
class Email(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255)
    domain = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'email'


@reversion.register()
class FlightHitFuzzy(SoftDeletionModel):
    fhf_flight = models.OneToOneField(Flight, models.DO_NOTHING, primary_key=True)
    fhf_hit_count = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'flight_hit_fuzzy'


@reversion.register()
class FlightHitGraph(SoftDeletionModel):
    fhg_flight = models.OneToOneField(Flight, models.DO_NOTHING, primary_key=True)
    fhg_hit_count = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'flight_hit_graph'


@reversion.register()
class FlightHitRule(SoftDeletionModel):
    fhr_flight = models.OneToOneField(Flight, models.DO_NOTHING, primary_key=True)
    fhr_hit_count = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'flight_hit_rule'


@reversion.register()
class FlightHitWatchlist(SoftDeletionModel):
    fhw_flight = models.OneToOneField(Flight, models.DO_NOTHING, primary_key=True)
    fhw_hit_count = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'flight_hit_watchlist'


@reversion.register()
class FlightLeg(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    leg_number = models.IntegerField()
    booking_detail = models.ForeignKey(BookingDetail, models.DO_NOTHING, blank=True, null=True)
    flight = models.ForeignKey(Flight, models.DO_NOTHING, blank=True, null=True)
    message = models.ForeignKey(Message, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'flight_leg'


@reversion.register()
class FlightPassenger(SoftDeletionModel):
    flight = models.ForeignKey(Flight, models.DO_NOTHING)
    passenger = models.OneToOneField(Passenger, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'flight_passenger'
        constraints = [models.UniqueConstraint(fields=['flight', 'passenger'],
                                               name='unique_flight_passenger')]


@reversion.register()
class FlightPassengerCount(SoftDeletionModel):
    fp_flight = models.OneToOneField(Flight, models.DO_NOTHING, primary_key=True)
    fp_count = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'flight_passenger_count'


@reversion.register()
class FrequentFlyer(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    carrier = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'frequent_flyer'


@reversion.register()
class HitDetail(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    flight = models.ForeignKey(Flight, models.DO_NOTHING)
    hit_enum = models.CharField(max_length=255, blank=True, null=True)
    hm = models.ForeignKey(HitMaker, models.DO_NOTHING)
    hit_type = models.CharField(max_length=3)
    passenger = models.ForeignKey(Passenger, models.DO_NOTHING, blank=True, null=True)
    percentage_match = models.FloatField(blank=True, null=True)
    cond_text = models.TextField(blank=True, null=True)
    rule_id = models.BigIntegerField()
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'hit_detail'


@reversion.register()
class HitsSummary(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    flight = models.ForeignKey(Flight, models.DO_NOTHING, blank=True, null=True)
    hs_graph_count = models.IntegerField(blank=True, null=True)
    hs_manual_count = models.IntegerField(blank=True, null=True)
    hs_partial_count = models.IntegerField(blank=True, null=True)
    hs_passenger = models.ForeignKey(Passenger, models.DO_NOTHING, blank=True, null=True)
    hs_rule_count = models.IntegerField(blank=True, null=True)
    hs_wl_count = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'hits_summary'


@reversion.register()
class HitViewStatus(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    hv_status = models.CharField(max_length=255)
    hv_hit_detail = models.OneToOneField(HitDetail, models.DO_NOTHING)
    hv_passenger = models.ForeignKey(Passenger, models.DO_NOTHING)
    hv_user_group = models.ForeignKey(UserGroup, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'hit_view_status'
        constraints = [models.UniqueConstraint(fields=['hv_hit_detail', 'hv_user_group'],
                                               name='unique_hv_hit_detail_hv_user_group')]


@reversion.register()
class MessageBooking(SoftDeletionModel):
    message = models.OneToOneField(Message, models.DO_NOTHING)
    booking_detail = models.ForeignKey(BookingDetail, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'message_booking'
        constraints = [models.UniqueConstraint(fields=['message', 'booking_detail'],
                                               name='unique_message_booking_detail')]


@reversion.register()
class MessageStatus(SoftDeletionModel):
    ms_message = models.OneToOneField(Message, models.DO_NOTHING, primary_key=True)
    ms_analyzed_timestamp = models.DateTimeField(blank=True, null=True)
    flight = models.ForeignKey(Flight, models.DO_NOTHING, blank=True, null=True)
    ms_status = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'message_status'


@reversion.register()
class MutableFlightDetails(SoftDeletionModel):
    flight = models.OneToOneField(Flight, models.DO_NOTHING, primary_key=True)
    full_utc_eta_timestamp = models.DateTimeField(blank=True, null=True, db_index=True)
    eta_date = models.DateField(blank=True, null=True)
    full_utc_etd_timestamp = models.DateTimeField(blank=True, null=True)
    full_eta_timestamp = models.DateTimeField(blank=True, null=True)
    full_etd_timestamp = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'mutable_flight_details'


@reversion.register()
class Notes(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    note_plain_text = models.CharField(max_length=10000)
    note_rtf_text = models.CharField(max_length=10000)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'notes'


@reversion.register()
class NoteAttachment(SoftDeletionModel):
    comment = models.OneToOneField(Notes, models.DO_NOTHING)
    attachment = models.ForeignKey(Attachment, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'note_attachment'
        constraints = [models.UniqueConstraint(fields=['comment', 'attachment'],
                                               name='unique_comment_attachment')]


@reversion.register()
class NoteTypeJoin(SoftDeletionModel):
    nt = models.OneToOneField(Notes, models.DO_NOTHING)
    n = models.ForeignKey(NoteType, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'note_type_join'
        constraints = [models.UniqueConstraint(fields=['nt', 'n'],
                                               name='unique_nt_n')]


@reversion.register()
class Notification(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    n_send_when = models.CharField(max_length=255)
    n_status = models.CharField(max_length=255)
    n_type = models.CharField(max_length=255)
    n_passenger = models.ForeignKey('Passenger', models.DO_NOTHING)
    n_user = models.ForeignKey(User, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'notification'


@reversion.register()
class PassengerDetails(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    pd_age = models.IntegerField(blank=True, null=True)
    pd_dob = models.DateField(blank=True, null=True)
    pd_first_name = models.CharField(max_length=255, blank=True, null=True)
    pd_gender = models.CharField(max_length=2, blank=True, null=True)
    pd_last_name = models.CharField(max_length=255, blank=True, null=True)
    pd_middle_name = models.CharField(max_length=255, blank=True, null=True)
    pd_nationality = models.CharField(max_length=255, blank=True, null=True)
    pd_passenger = models.OneToOneField(Passenger, models.DO_NOTHING, blank=True, null=True)
    pd_passenger_type = models.CharField(max_length=3)
    pd_residency_country = models.CharField(max_length=255, blank=True, null=True)
    pd_suffix = models.CharField(max_length=255, blank=True, null=True)
    pd_title = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'passenger_details'


@reversion.register()
class PassengerIdTag(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    doc_hash_id = models.CharField(max_length=255, blank=True, null=True)
    id_tag = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    pax = models.OneToOneField(Passenger, models.DO_NOTHING, blank=True, null=True)
    tamr_id = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'passenger_id_tag'


@reversion.register()
class PassengerNotes(SoftDeletionModel):
    cmt_passenger = models.ForeignKey(Passenger, models.DO_NOTHING, blank=True, null=True)
    id = models.OneToOneField(Notes, models.DO_NOTHING, primary_key=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'passenger_notes'


@reversion.register()
class PassengerTripDetails(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    apis_co_traveler_count = models.IntegerField(blank=True, null=True)
    debark_country = models.CharField(max_length=255, blank=True, null=True)
    debarkation = models.CharField(max_length=255, blank=True, null=True)
    embark_country = models.CharField(max_length=255, blank=True, null=True)
    embarkation = models.CharField(max_length=255, blank=True, null=True)
    hours_before_takeoff = models.IntegerField(blank=True, null=True)
    days_visa_valid = models.IntegerField(blank=True, null=True)
    ptd = models.ForeignKey(Passenger, models.DO_NOTHING, blank=True, null=True)
    pnr_ref_number = models.CharField(max_length=255, blank=True, null=True)
    ref_number = models.CharField(max_length=255, blank=True, null=True)
    travel_frequency = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'passenger_trip_details'


@reversion.register()
class PassengerWlTimestamp(SoftDeletionModel):
    pwlt = models.OneToOneField(Passenger, models.DO_NOTHING, primary_key=True)
    pwlt_watchlist_check_timestamp = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'passenger_wl_timestamp'


@reversion.register()
class PaxBooking(SoftDeletionModel):
    pax = models.OneToOneField(Passenger, models.DO_NOTHING)
    booking_detail = models.ForeignKey(BookingDetail, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'pax_booking'
        constraints = [models.UniqueConstraint(fields=['pax', 'booking_details'],
                                               name='unique_pax_booking_details')]


@reversion.register()
class Pnr(SoftDeletionModel):
    id = models.OneToOneField(Message, models.DO_NOTHING, primary_key=True)
    bag_count = models.IntegerField(blank=True, null=True)
    baggage_unit = models.CharField(max_length=255, blank=True, null=True)
    baggage_weight = models.FloatField(blank=True, null=True)
    carrier = models.CharField(max_length=255, blank=True, null=True)
    date_booked = models.DateField(blank=True, null=True)
    date_received = models.DateField(blank=True, null=True)
    days_booked_before_travel = models.IntegerField(blank=True, null=True)
    departure_date = models.DateField(blank=True, null=True)
    message_type = models.CharField(max_length=10, blank=True, null=True)
    transmission_date = models.DateTimeField(blank=True, null=True)
    transmission_source = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=10, blank=True, null=True)
    form_of_payment = models.CharField(max_length=255, blank=True, null=True)
    origin = models.CharField(max_length=255, blank=True, null=True)
    origin_country = models.CharField(max_length=3, blank=True, null=True)
    record_locator = models.CharField(max_length=20, blank=True, null=True)
    reservation_create_date = models.DateTimeField(blank=True, null=True)
    total_bag_count = models.IntegerField(blank=True, null=True)
    total_bag_weight = models.FloatField(blank=True, null=True)
    trip_duration = models.FloatField(blank=True, null=True)
    trip_type = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'pnr'


@reversion.register()
class PaymentForm(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    payment_amount = models.CharField(max_length=255, blank=True, null=True)
    payment_type = models.CharField(max_length=255, blank=True, null=True)
    pnr = models.ForeignKey(Pnr, models.DO_NOTHING, blank=True, null=True)
    payment_whole_dollar = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'payment_form'


@reversion.register()
class PendingHitDetail(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    flight = models.ForeignKey(Flight, models.DO_NOTHING)
    hit_enum = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    hm = models.ForeignKey(HitMaker, models.DO_NOTHING)
    hit_type = models.CharField(max_length=3)
    passenger = models.ForeignKey(Passenger, models.DO_NOTHING, blank=True, null=True)
    percentage_match = models.FloatField(blank=True, null=True)
    cond_text = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'pending_hit_detail'


@reversion.register()
class Phone(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    flight = models.ForeignKey(Flight, models.DO_NOTHING, blank=True, null=True)
    number = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'phone'


@reversion.register()
class PnrAddress(SoftDeletionModel):
    pnr = models.OneToOneField(Pnr, models.DO_NOTHING)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'pnr_address'
        constraints = [models.UniqueConstraint(fields=['pnr', 'address'],
                                               name='unique_pnr_address')]


@reversion.register()
class PnrAgency(SoftDeletionModel):
    pnr = models.OneToOneField(Pnr, models.DO_NOTHING)
    agency = models.ForeignKey(Agency, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'pnr_agency'
        constraints = [models.UniqueConstraint(fields=['pnr', 'agency'],
                                               name='unique_pnr_agency')]


@reversion.register()
class PnrCodeshares(SoftDeletionModel):
    pnr = models.OneToOneField(Pnr, models.DO_NOTHING)
    codeshare = models.ForeignKey(CodeShareFlight, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'pnr_codeshares'
        constraints = [models.UniqueConstraint(fields=['pnr', 'codeshare'],
                                               name='unique_pnr_codeshare')]


@reversion.register()
class PnrCreditCard(SoftDeletionModel):
    pnr = models.OneToOneField(Pnr, models.DO_NOTHING)
    credit_card = models.ForeignKey(CreditCard, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'pnr_credit_card'
        constraints = [models.UniqueConstraint(fields=['pnr', 'credit_card'],
                                               name='unique_pnr_credit_card')]


@reversion.register()
class PnrDwelltime(SoftDeletionModel):
    pnr = models.OneToOneField(Pnr, models.DO_NOTHING)
    dwell = models.ForeignKey(DwellTime, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'pnr_dwelltime'
        constraints = [models.UniqueConstraint(fields=['pnr', 'dwell'],
                                               name='unique_pnr_dwell')]


@reversion.register()
class PnrEmail(SoftDeletionModel):
    pnr = models.OneToOneField(Pnr, models.DO_NOTHING)
    email = models.ForeignKey(Email, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'pnr_email'
        constraints = [models.UniqueConstraint(fields=['pnr', 'email'],
                                               name='unique_pnr_email')]


@reversion.register()
class PnrFlight(SoftDeletionModel):
    pnr = models.OneToOneField(Pnr, models.DO_NOTHING)
    flight = models.ForeignKey(Flight, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'pnr_flight'
        constraints = [models.UniqueConstraint(fields=['pnr', 'flight'],
                                               name='unique_pnr_flight')]


@reversion.register()
class PnrFrequentFlyer(SoftDeletionModel):
    pnr = models.OneToOneField(Pnr, models.DO_NOTHING)
    ff = models.ForeignKey(FrequentFlyer, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'pnr_frequent_flyer'
        constraints = [models.UniqueConstraint(fields=['pnr', 'ff'],
                                               name='unique_pnr_ff')]


@reversion.register()
class PnrPassenger(SoftDeletionModel):
    pnr = models.OneToOneField(Pnr, models.DO_NOTHING)
    passenger = models.ForeignKey(Passenger, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'pnr_passenger'
        constraints = [models.UniqueConstraint(fields=['pnr', 'passenger'],
                                               name='unique_pnr_passenger')]


@reversion.register()
class PnrPhone(SoftDeletionModel):
    pnr = models.OneToOneField(Pnr, models.DO_NOTHING)
    phone = models.ForeignKey(Phone, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'pnr_phone'
        constraints = [models.UniqueConstraint(fields=['pnr', 'phone'],
                                               name='unique_pnr_phone')]


@reversion.register()
class Seat(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    apis = models.CharField(max_length=1, blank=True, null=True)
    flight = models.ForeignKey(Flight, models.DO_NOTHING, blank=True, null=True)
    number = models.CharField(max_length=255)
    passenger = models.ForeignKey(Passenger, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'seat'


@reversion.register()
class TicketFare(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    currency_code = models.CharField(max_length=255, blank=True, null=True)
    number_booklets = models.CharField(max_length=255, blank=True, null=True)
    payment_amount = models.CharField(max_length=255, blank=True, null=True)
    ticket_number = models.CharField(max_length=255, blank=True, null=True)
    ticket_type = models.CharField(max_length=255, blank=True, null=True)
    ticketless = models.CharField(max_length=1, blank=True, null=True)
    passenger = models.ForeignKey(Passenger, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'ticket_fare'


@reversion.register()
class UserGroupNotifications(SoftDeletionModel):
    id = models.OneToOneField(Notification, models.DO_NOTHING, primary_key=True)
    ug = models.ForeignKey(UserGroup, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    # a better name of the hm_id field is ug_id
    # added a virtual field to maintain convention of GTAS
    def _get_hm_id(self):
        return self.ug

    hm_id = property(_get_hm_id)

    class Meta:
        managed = True
        db_table = 'user_group_notifications'


@reversion.register()
class UserNotification(SoftDeletionModel):
    id = models.OneToOneField(Notification, models.DO_NOTHING, primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'user_notification'
