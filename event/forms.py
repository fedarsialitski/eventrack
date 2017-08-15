from django import forms

from .models import Artist, Event, Venue


class ArtistForm(forms.ModelForm):
    name = forms.CharField(required=True)
    image_url = forms.URLField(required=False, help_text='Optional')
    thumb_url = forms.URLField(required=False, help_text='Optional')

    class Meta:
        model = Artist

        fields = [
            'name',
            'image_url',
            'thumb_url',
        ]


class EventForm(forms.ModelForm):
    title = forms.CharField(required=True)
    venue = forms.ModelChoiceField(required=True, queryset=Venue.objects.all(), empty_label='')
    datetime = forms.DateTimeField(required=True, input_formats=['%Y-%m-%dT%H:%M'])
    artists  = forms.ModelMultipleChoiceField(required=True, queryset=Artist.objects.all())

    class Meta:
        model = Event

        fields = [
            'title',
            'venue',
            'datetime',
        ]


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
