from django import forms

from venue.models import Venue


class VenueForm(forms.ModelForm):
    name = forms.CharField(required=True)
    city = forms.CharField(required=False, help_text='Optional')
    country = forms.CharField(required=False, help_text='Optional')

    class Meta:
        model = Venue

        fields = [
            'name',
            'city',
            'country',
        ]
