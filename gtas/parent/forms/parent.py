from django import forms


class AirportForm(forms.Form):
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter city...",
                "id": "city",
            }
        ),
        required=False,
    )
    country = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter country...",
                "id": "country",
            }
        ),
        required=False,
    )
    iata = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter iata...",
                "id": "iata",
            }
        ),
        required=False,
    )
    icao = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter icao...",
                "id": "icao",
            }
        ),
        required=False,
    )
    latitude = forms.DecimalField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter latitude...",
                "id": "latitude",
            }
        ),
        required=False,
    )
    longitude = forms.DecimalField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter longitude...",
                "id": "longitude",
            }
        ),
        required=False,
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter name...",
                "id": "name",
            }
        ),
        required=False,
    )
    origin_id = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter origin_id...",
                "id": "origin_id",
            }
        ),
        required=True,
    )
    timezone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter timezone...",
                "id": "timezone",
            }
        ),
        required=False,
    )
    utc_offset = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter utc_offset...",
                "id": "utc_offset",
            }
        ),
        required=True,
    )


class AirportRestoreForm(forms.Form):
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter city...",
                "id": "city",
            }
        ),
        required=False,
    )
    country = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter country...",
                "id": "country",
            }
        ),
        required=False,
    )
    iata = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter iata...",
                "id": "iata",
            }
        ),
        required=False,
    )
    icao = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter icao...",
                "id": "icao",
            }
        ),
        required=False,
    )
    latitude = forms.DecimalField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter latitude...",
                "id": "latitude",
            }
        ),
        required=False,
    )
    longitude = forms.DecimalField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter longitude...",
                "id": "longitude",
            }
        ),
        required=False,
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter name...",
                "id": "name",
            }
        ),
        required=False,
    )
    timezone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter timezone...",
                "id": "timezone",
            }
        ),
        required=False,
    )
    utc_offset = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter utc_offset...",
                "id": "utc_offset",
            }
        ),
        required=False,
    )


class ApiAccessForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter email...",
                "id": "email",
            }
        ),
        required=False,
    )
    organization = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter organization...",
                "id": "organization",
            }
        ),
        required=False,
    )
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter password...",
                "id": "password",
            }
        ),
        required=False,
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter username...",
                "id": "username",
            }
        ),
        required=False,
    )


class AppConfigurationForm(forms.Form):
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter description...",
                "id": "description",
            }
        ),
        required=False,
    )
    opt = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter opt...", "id": "opt"}
        ),
        required=False,
    )
    val = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter val...", "id": "val"}
        ),
        required=False,
    )


class AuditLogForm(forms.Form):
    action_data = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter action_data...",
                "id": "action_data",
            }
        ),
        required=False,
    )
    action_status = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter action_status...",
                "id": "action_status",
            }
        ),
        required=False,
    )
    action_type = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter action_type...",
                "id": "action_type",
            }
        ),
        required=False,
    )
    action_message = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter action_message...",
                "id": "action_message",
            }
        ),
        required=False,
    )
    action_target = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter action_target...",
                "id": "action_target",
            }
        ),
        required=False,
    )


class CarrierForm(forms.Form):
    iata = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter iata...",
                "id": "iata",
            }
        ),
        required=False,
    )
    icao = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter icao...",
                "id": "icao",
            }
        ),
        required=False,
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter name...",
                "id": "name",
            }
        ),
        required=False,
    )
    origin_id = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter origin_id...",
                "id": "origin_id",
            }
        ),
        required=False,
    )


class CarrierRestoreForm(forms.Form):
    iata = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter iata...",
                "id": "iata",
            }
        ),
        required=False,
    )
    icao = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter icao...",
                "id": "icao",
            }
        ),
        required=False,
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter name...",
                "id": "name",
            }
        ),
        required=False,
    )


class CodeShareFlightForm(forms.Form):
    marketing_flight_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter marketing_flight_number...",
                "id": "marketing_flight_number",
            }
        ),
        required=False,
    )
    operating_flight_id = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter operating_flight_id...",
                "id": "operating_flight_id",
            }
        ),
        required=False,
    )
    operating_flight_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter operating_flight_number...",
                "id": "operating_flight_number",
            }
        ),
        required=False,
    )


class CountryForm(forms.Form):
    iso2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter iso2...",
                "id": "iso2",
            }
        ),
        required=False,
    )
    iso3 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter iso3...",
                "id": "iso3",
            }
        ),
        required=False,
    )
    iso_numeric = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter iso_numeric...",
                "id": "iso_numeric",
            }
        ),
        required=False,
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter name...",
                "id": "name",
            }
        ),
        required=False,
    )
    origin_id = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter origin_id...",
                "id": "origin_id",
            }
        ),
        required=False,
    )


class CountryRestoreForm(forms.Form):
    iso2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter iso2...",
                "id": "iso2",
            }
        ),
        required=False,
    )
    iso3 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter iso3...",
                "id": "iso3",
            }
        ),
        required=False,
    )
    iso_numeric = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter iso_numeric...",
                "id": "iso_numeric",
            }
        ),
        required=False,
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter name...",
                "id": "name",
            }
        ),
        required=False,
    )


class DwellTimeForm(forms.Form):
    arrival_time = forms.DateTimeField(
        input_formats=["%Y-%m-%d %H:%M"],
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter arrival_time...",
                "id": "arrival_time",
            }
        ),
        required=False,
    )
    departure_at = forms.DateTimeField(
        input_formats=["%Y-%m-%d %H:%M"],
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter departure_at...",
                "id": "departure_at",
            }
        ),
        required=False,
    )
    dwell_time = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter dwell_time...",
                "id": "dwell_time",
            }
        ),
        required=False,
    )
    flying_from = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter flying_from...",
                "id": "flying_from",
            }
        ),
        required=False,
    )
    flying_to = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter flying_to...",
                "id": "flying_to",
            }
        ),
        required=False,
    )
    arrival_airport = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter arrival_airport...",
                "id": "arrival_airport",
            }
        ),
        required=False,
    )


class ErrorDetailForm(forms.Form):
    code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter code...",
                "id": "code",
            }
        ),
        required=False,
    )
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter description...",
                "id": "description",
            }
        ),
        required=False,
    )
    details = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter details...",
                "id": "details",
            }
        ),
        required=False,
    )


class FlightDirectionForm(forms.Form):
    code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter code...",
                "id": "code",
            }
        ),
        required=False,
    )
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter description...",
                "id": "description",
            }
        ),
        required=False,
    )


class NoteTypeForm(forms.Form):
    nt_type = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter nt_type...",
                "id": "nt_type",
            }
        ),
        required=False,
    )
