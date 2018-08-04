from django import forms

from artist.models import Artist


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
