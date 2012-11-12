from django.conf.urls import patterns, include, url
from piston.resource import Resource
from left.handlers import SBTHandler
from left.handlers import EmployeeHandler


urlpatterns = patterns('',
    url( r'^sbt/(?P<snils>\d{3}-\d{3}-\d{3}\ \d{2})$', Resource(handler=SBTHandler) ),
    url( r'^sbt/all/$', Resource(handler=SBTHandler), {'snils':'%'} ),
)
