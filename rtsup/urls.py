# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from tastypie.api import Api

from right.urls import api as right_api 
from left.urls import api as left_api 

import views

# проверка соответствия регекспа урла и обработчика
urlpatterns = patterns('',
    url(r'^rest/', include(right_api.urls)),
    url(r'^rest/', include(left_api.urls)),
    
    url(r'^employee/all/$', views.employee_list_all),

    url(r'^employee/(?P<snils>\d{3}-\d{3}-\d{3}\ \d{2})/$', views.employee_card),
)

urlpatterns += staticfiles_urlpatterns()