
from django import forms
from .modules import Rental

class BookRentForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['who', 'what']
