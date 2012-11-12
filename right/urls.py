from django.conf.urls import patterns, include, url
from piston.resource import Resource
from right.handlers import EmployeeHandler



urlpatterns = patterns('',
    url( r'^employee/$', Resource(handler=EmployeeHandler) ),
    url( r'^employee/(?P<id>\d*)$', Resource(handler=EmployeeHandler) ),
)
