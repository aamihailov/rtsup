from django.conf.urls import patterns, include, url

from piston.resource import Resource
from left.models import *

urlpatterns = patterns('',
    url(r'^rest/', include('right.rest')),

    url( r'^statistics_by_technic/$', 
         Resource(handler=StatisticsByTechnicHandler), {'snils':'%'} ),
    url( r'^statistics_by_technic/(?P<snils>\d{3}-\d{3}-\d{3}\ \d{2})$', 
         Resource(handler=StatisticsByTechnicHandler) ),

    url( r'^last_tasks/$', Resource(handler=LastTasksHandler) ),
)
