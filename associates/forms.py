from django import forms
from models import Associate

class AssociateForm(form.ModelForm):

    class Meta:
        model = Associate
        fields = ('organization', 'street_and_nr', 'city', )
