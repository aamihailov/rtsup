from django.conf.urls import patterns, include, url

from tastypie.api import Api

from right.urls import api as right_api 
from left.urls import api as left_api 

urlpatterns = patterns('',
    url(r'rest/', include(right_api.urls)),
    url(r'rest/', include(left_api.urls)),
)
