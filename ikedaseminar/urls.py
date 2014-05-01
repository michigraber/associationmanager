from django.conf.urls import patterns, include, url

from ikedaseminar import views

urlpatterns = patterns('ikedaseminar.views',
    url(r'^$', 'welcome', {}, name='welcome'),
)
