from django import forms

from .models import *

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = RestaurantModel
        fields = ['name', 'slug', 'specialization', 'address', 'site', 'phone']





