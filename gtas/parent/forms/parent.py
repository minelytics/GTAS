from django import forms


class AirportForm(forms.Form):
    city = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter city...',
            'id': 'city'
        }),
        required=False
    )
    country = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter country...',
            'id': 'country'
        }),
        required=False
    )
    iata = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter iata...',
            'id': 'iata'
        }),
        required=False
    )
    icao = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter icao...',
            'id': 'icao'
        }),
        required=False
    )
    latitude = forms.DecimalField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter latitude...',
            'id': 'latitude'
        }),
        required=False
    )
    longitude = forms.DecimalField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter longitude...',
            'id': 'longitude'
        }),
        required=False
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter name...',
            'id': 'name'
        }),
        required=False
    )
    origin_id = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter origin_id...',
            'id': 'origin_id'
        }),
        required=True
    )
    timezone = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter timezone...',
            'id': 'timezone'
        }),
        required=False
    )
    utc_offset = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter utc_offset...',
            'id': 'utc_offset'
        }),
        required=True
    )
