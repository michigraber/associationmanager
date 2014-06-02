
from django.conf import settings
from django.conf.urls import patterns, include, url

from django.views.generic import RedirectView

from events.views import PaypalIPNEndpoint
from events.models import Event

from ikedaseminar import views

# THE EVENT WE DEAL HERE WITH
try:
    EVENT = Event.objects.get(pk=settings.IKEDASEMINAR_EVENT_PK)
except:
    EVENT = None

urlpatterns = patterns('ikedaseminar.views',
    url(r'^$', RedirectView.as_view(url='/de/')),
    url(r'(?P<language>en|de)/*$', 'welcome', {}, name='welcome'),
)

urlpatterns += patterns('events.views',
    url(r'(?P<language>en|de)/registration/aiki-kai/*$',
        'registration_configuration', name='preregistration'),
#   url(r'(?P<language>en|de)/registration/paypal/*$', PaypalIPNEndpoint()),
    url(r'(?P<language>en|de)/registration/paypal/*$',
        'paypal_ipn', name='paypal_ipn'),
    url(r'(?P<language>en|de)/registration/*$',
        'registration_comingsoon',
        name='registration'),
    url(r'(?P<language>en|de)/registration/(?P<status>cancel|success)/*$',
        'registration_paypal_return', name='registration_paypal_return'),
)
