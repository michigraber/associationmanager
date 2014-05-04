from django.conf.urls import patterns, include, url

from django.views.generic import RedirectView

from ikedaseminar import views

urlpatterns = patterns('ikedaseminar.views',
    url(r'^$', RedirectView.as_view(url='/de/')),
    url(r'(?P<lang>en|de)/*$', 'welcome', {}, name='welcome'),
    
    url(r'(?P<lang>en|de)/registration/*$', 'registration', {}, name='registration'),
)
