from django.forms import ModelForm, DateInput
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from .models import *


class SickForm(ModelForm):
    class Meta:
        model = Quarintine
        fields = '__all__'
        labels = {
            'last_bhs': _('Last BHS Appointment'),
            'next_bhs': _('Next BHS Appointment'),
            'full_duty': _('Full Duty Date'),
            'last_name': _('Last Name'),
            'first_name': _('First Name'),
        }
        widgets = {
            'last_bhs': forms.DateInput(attrs={'type': 'date'}),
            'next_bhs': forms.DateInput(attrs={'type': 'date'}),
            'full_duty': forms.DateInput(attrs={'type': 'date'}),

        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1',
                  'password2', 'first_name', 'last_name']


class AddMemberProfile(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        labels = {
            'oda': _('City Start Date'),
            'ted': _('Title Entry Date'),
            'lastfive': _('Last 5 of SS'),
            'statenumber': _('State Certification Number'),
            'stateexp': _('State Expiration'),
            'macexp': _('REMAC Expiration'),
            'streetaddress': _('Street Address'),
            'zipcode': _('Zip Code'),
            'contact_name': _('Contact Name'),
            'contact_phone': _('Contact Phone Number'),
            'contact_street_address': _('Contact Street Address'),
            'contact_city': _('Contact City'),
            'contact_state': _('Contact State'),
            'contact_zipcode': _('Contact Zip Code'),
            'cert': _('Certification Type'),
        }

        widgets = {
            'oda': forms.DateInput(attrs={'type': 'date'}),
            'ted': forms.DateInput(attrs={'type': 'date'}),
            'stateexp': forms.DateInput(attrs={'type': 'date'}),
            'macexp': forms.DateInput(attrs={'type': 'date'}),
        }
