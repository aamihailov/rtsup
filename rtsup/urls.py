from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^left/', include('left.urls')),
    url(r'^right/', include('right.urls')),
)
