from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import ikedaseminar.urls

urlpatterns = patterns('',

    url(r'^$', include(ikedaseminar.urls)),

    url(r'^admin/', include(admin.site.urls)),

)
