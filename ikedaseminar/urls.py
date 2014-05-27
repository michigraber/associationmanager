from django.conf.urls import patterns, include, url

from django.views.generic import RedirectView

from events.views import RegistrationWizard
from events.models import Event

from ikedaseminar import views

# THE EVENT WE DEAL HERE WITH
EVENT = Event.objects.get(pk=1)

urlpatterns = patterns('ikedaseminar.views',
    url(r'^$', RedirectView.as_view(url='/de/')),
    url(r'(?P<language>en|de)/*$', 'welcome', {}, name='welcome'),
    
    #url(r'(?P<lang>en|de)/registration/*$', 'registration', {}, name='registration'),
)

INITIAL_DICT = { 
        '0' : {'event': EVENT},
        '1': {},
        '2': {},
        }

urlpatterns += patterns('events.views',
    url(r'(?P<language>en|de)/registration/*$',
        RegistrationWizard.as_view(initial_dict=INITIAL_DICT),
        name='registration'),
)
