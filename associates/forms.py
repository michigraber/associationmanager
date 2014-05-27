from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.utils.translation import ugettext_lazy as _

from .models import Associate

class AssociateForm(forms.ModelForm):
    class Meta:
        model = Associate
        fields = (
                'first_name', 'last_name', 'date_of_birth',
                'street_and_nr', 'postal_code', 'city', 'country', 
                'email_address', 'emergency_contact_first_name',
                'emergency_contact_last_name',
                'emergency_contact_phone_number',
                'emergency_contact_relationship',
                )

BIRTH_YEAR_CHOICES = tuple([int(i) for i in range(1910, 2014)])

class AssociateForm_de(forms.ModelForm):

    class Meta:
        model = Associate
        fields = (
                'first_name', 'last_name', 'date_of_birth',
                'street_and_nr', 'postal_code', 'city', 'country', 
                'email_address', 'emergency_contact_first_name',
                'emergency_contact_last_name',
                'emergency_contact_phone_number',
                'emergency_contact_relationship',
                )

        widgets = {
            'first_name': forms.widgets.TextInput(attrs={'size': 40,}),
            'last_name': forms.widgets.TextInput(attrs={'size': 40,}),
            'date_of_birth': SelectDateWidget(years=BIRTH_YEAR_CHOICES),
            'street_and_nr': forms.widgets.TextInput(attrs={'size': 40,}),
            'city': forms.widgets.TextInput(attrs={'size': 40,}),
            'country': forms.widgets.TextInput(attrs={'size': 40,}),
            'email_address': forms.widgets.TextInput(attrs={'size': 40,}),
            }


        labels = {
                'first_name': _('Vorname'),
                'last_name': _('Nachname'),
                'date_of_birth': _('Geburtsdatum'),
                'street_and_nr': _('Strasse und Nummer'),
                'postal_code': _('Postleitzahl'),
                'city': _('Ort'), 
                'country': _('Land'), 
                'email_address': _('Email Adresse'),
                'emergency_contact_first_name': _('Vorname'),
                'emergency_contact_last_name': _('Nachname'),
                'emergency_contact_phone_number': _('Telefonnummer'),
                'emergency_contact_relationship': _('Beziehung'),
                }

#       help_texts = {
#           'name': _('Some useful help text.'),
#       }
#       error_messages = {
#           'name': {
#               'max_length': _("This writer's name is too long."),
#           },
#       }
            

