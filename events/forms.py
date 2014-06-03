from django.forms import forms
from django.forms.fields import BooleanField, CharField

from associates.models import Associate


class RegistrationMessageForm_de(forms.Form):
    
    message = CharField(widget=forms.Textarea, required=False)

    labels = {
            'message': 'Nachricht',
            }


class RegistrationMessageForm_en(forms.Form):
    
    message = CharField(widget=forms.Textarea, required=False)

    labels = {
            'message': 'Message',
            }


class SelectPurchaseItemsForm(forms.Form):

    def __init__(self, *args, **kwargs):
        language = kwargs.pop('language', 'en')
        event = kwargs.pop('event', None)
        super(SelectPurchaseItemsForm, self).__init__(*args, **kwargs)

        for ep in event.eventpart_set.all():
            if ep.still_available() and ep.is_bookable:
                if language == 'en':
                    self.fields[ep.short_description_en] = BooleanField(
                            required=False)
                    self.fields[ep.short_description_en].label =\
                            ep.short_description_en
                elif language == 'de':
                    self.fields[ep.short_description_de] = BooleanField(
                            required=False)
                    self.fields[ep.short_description_de].label =\
                            ep.short_description_de

        for art in event.article_set.all():
            if art.still_available() and art.is_sold:
                if language == 'en':
                    self.fields[art.name_en] = BooleanField(required=False)
                    self.fields[art.name_en].label = art.name_en
                elif language == 'de':
                    self.fields[art.name_de] = BooleanField(required=False)
                    self.fields[art.name_de].label = art.name_de

