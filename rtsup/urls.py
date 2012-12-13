# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

import views

# проверка соответствия регекспа урла и обработчика
urlpatterns = patterns('',
    url(r'^api/employee/$', views.rest_employee_all),
    url(r'^employee/$', views.html_employee_all),

    url(r'^api/employee/(?P<id>\d+)/$', views.rest_employee),
    url(r'^employee/(?P<id>\d+)/$', views.html_employee),
    
    url(r'^api/equipment/(?P<id>\d+)/$', views.rest_equipment),
    url(r'^api/task/(?P<task_id>\d+)/equipment/$', views.get_equipment_by_task),
    
    url(r'^api/task/(?P<task_id>\d+)/equipment/(?P<equipment_id>\d+)/$', views.set_equipment_for_task),

    url(r'^api/task/$', views.post_new_task),
)
