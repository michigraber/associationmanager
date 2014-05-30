from django import forms
from django.forms.extras.widgets import SelectDateWidget

from .models import Associate

BIRTH_YEAR_CHOICES = tuple([int(i) for i in range(1910, 2014)])

class AssociateForm_de(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AssociateForm_de, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['date_of_birth'].required = True
        self.fields['street_and_nr'].required = True
        self.fields['postal_code'].required = True
        self.fields['city'].required = True
        self.fields['country'].required = True
        self.fields['email_address'].required = True

    class Meta:
        model = Associate
        fields = (
                'first_name', 'last_name', 'date_of_birth', 'organization',
                'street_and_nr', 'postal_code', 'city', 'country',
                'email_address',
                )

        widgets = {
            'first_name': forms.widgets.TextInput(attrs={'size': 40,}),
            'last_name': forms.widgets.TextInput(attrs={'size': 40,}),
            'organization': forms.widgets.TextInput(attrs={'size': 40,}),
            'date_of_birth': SelectDateWidget(years=BIRTH_YEAR_CHOICES),
            'street_and_nr': forms.widgets.TextInput(attrs={'size': 40,}),
            'city': forms.widgets.TextInput(attrs={'size': 40,}),
            'country': forms.widgets.TextInput(attrs={'size': 40,}),
            'email_address': forms.widgets.TextInput(attrs={'size': 40,}),
            }


        labels = {
                'first_name': 'Vorname',
                'last_name': 'Nachname',
                'organization': 'Dojo',
                'date_of_birth': 'Geburtsdatum',
                'street_and_nr': 'Strasse und Nummer',
                'postal_code': 'Postleitzahl',
                'city': 'Ort', 
                'country': 'Land', 
                'email_address': 'Email Adresse',
                }


class EmergencyContactForm_de(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmergencyContactForm_de, self).__init__(*args, **kwargs)
        self.fields['emergency_contact_first_name'].required = True
        self.fields['emergency_contact_last_name'].required = True
        self.fields['emergency_contact_phone_number'].required = True

    class Meta:
        model = Associate
        fields = (
                'emergency_contact_first_name',
                'emergency_contact_last_name',
                'emergency_contact_phone_number',
                'emergency_contact_relationship',
                )

        widgets = {
            'emergency_contact_first_name':
                forms.widgets.TextInput(attrs={'size': 40,}),
            'emergency_contact_last_name':
                forms.widgets.TextInput(attrs={'size': 40,}),
            'emergency_contact_relationship':
                forms.widgets.TextInput(attrs={'size': 40,}),
            'emergency_contact_phone_number':
                forms.widgets.TextInput(attrs={'size': 40,}),
            }

        labels = {
                'emergency_contact_first_name': 'Vorname',
                'emergency_contact_last_name': 'Nachname',
                'emergency_contact_phone_number': 'Telefonnummer',
                'emergency_contact_relationship': 'Beziehung',
                }


class AssociateForm_en(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AssociateForm_en, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['date_of_birth'].required = True
        self.fields['street_and_nr'].required = True
        self.fields['postal_code'].required = True
        self.fields['city'].required = True
        self.fields['country'].required = True
        self.fields['email_address'].required = True

    class Meta:
        model = Associate
        fields = (
                'first_name', 'last_name', 'date_of_birth', 'organization',
                'street_and_nr', 'postal_code', 'city', 'country', 
                'email_address',
                )

        widgets = {
            'first_name': forms.widgets.TextInput(attrs={'size': 40,}),
            'last_name': forms.widgets.TextInput(attrs={'size': 40,}),
            'organization': forms.widgets.TextInput(attrs={'size': 40,}),
            'date_of_birth': SelectDateWidget(years=BIRTH_YEAR_CHOICES),
            'street_and_nr': forms.widgets.TextInput(attrs={'size': 40,}),
            'city': forms.widgets.TextInput(attrs={'size': 40,}),
            'country': forms.widgets.TextInput(attrs={'size': 40,}),
            'email_address': forms.widgets.TextInput(attrs={'size': 40,}),
            }


        labels = {
                'first_name': 'Firstname',
                'last_name': 'Lastname',
                'organization': 'Dojo',
                'date_of_birth': 'Birthdate',
                'street_and_nr': 'Address',
                'postal_code': 'Postal Code',
                'city': 'City', 
                'country': 'Country', 
                'email_address': 'E-mail Address',
                }


class EmergencyContactForm_en(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmergencyContactForm_en, self).__init__(*args, **kwargs)
        self.fields['emergency_contact_first_name'].required = True
        self.fields['emergency_contact_last_name'].required = True
        self.fields['emergency_contact_phone_number'].required = True

    class Meta:
        model = Associate
        fields = (
                'emergency_contact_first_name',
                'emergency_contact_last_name',
                'emergency_contact_phone_number',
                'emergency_contact_relationship',
                )

        widgets = {
            'emergency_contact_first_name':
                forms.widgets.TextInput(attrs={'size': 40,}),
            'emergency_contact_last_name':
                forms.widgets.TextInput(attrs={'size': 40,}),
            'emergency_contact_relationship':
                forms.widgets.TextInput(attrs={'size': 40,}),
            'emergency_contact_phone_number':
                forms.widgets.TextInput(attrs={'size': 40,}),
            }

        labels = {
                'emergency_contact_first_name': 'First Name',
                'emergency_contact_last_name': 'Last Name',
                'emergency_contact_phone_number': 'Phone Number',
                'emergency_contact_relationship': 'Relationship',
                }
