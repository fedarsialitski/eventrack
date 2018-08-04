from django import forms

from artist.models import Artist
from event.models import Event
from venue.models import Venue


class EventForm(forms.ModelForm):
    title = forms.CharField(required=True)
    venue = forms.ModelChoiceField(required=True, queryset=Venue.objects.all(), empty_label='')
    datetime = forms.DateTimeField(required=True, input_formats=['%Y-%m-%dT%H:%M'])
    artists = forms.ModelMultipleChoiceField(required=True, queryset=Artist.objects.all())

    class Meta:
        model = Event

        fields = [
            'title',
            'venue',
            'datetime',
        ]


class SearchForm(forms.Form):
    keyword = forms.CharField(required=False)
