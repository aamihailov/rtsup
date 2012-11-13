from django.conf.urls import patterns, include, url
from piston.resource import Resource
from right.models import *


urlpatterns = patterns('',
    url( r'^department/$', Resource(handler=DepartmentHandler) ),
    url( r'^department/(?P<id>\d*)$', Resource(handler=DepartmentHandler) ),
    
    url( r'^department_activity_sphere/$', Resource(handler=DepartmentActivitySphereHandler) ),
    url( r'^department_activity_sphere/(?P<id>\d*)$', Resource(handler=DepartmentActivitySphereHandler) ),
    
    url( r'^employee/$', Resource(handler=EmployeeHandler) ),
    url( r'^employee/(?P<id>\d*)$', Resource(handler=EmployeeHandler) ),
    
    url( r'^employee_role/$', Resource(handler=EmployeeRoleHandler) ),
    url( r'^employee_role/(?P<id>\d*)$', Resource(handler=EmployeeRoleHandler) ),
    
    url( r'^employee_operation/$', Resource(handler=EmployeeOperationHandler) ),
    url( r'^employee_operation/(?P<id>\d*)$', Resource(handler=EmployeeOperationHandler) ),
    
    url( r'^employee_operation_type/$', Resource(handler=EmployeeOperationTypeHandler) ),
    url( r'^employee_operation_type/(?P<id>\d*)$', Resource(handler=EmployeeOperationTypeHandler) ),
    
    url( r'^admins/$', Resource(handler=AdminsHandler) ),
    url( r'^admins/(?P<id>\d*)$', Resource(handler=AdminsHandler) ),
    
    url( r'^technics/$', Resource(handler=TechnicsHandler) ),
    url( r'^technics/(?P<id>\d*)$', Resource(handler=TechnicsHandler) ),
    
    url( r'^equipment_owner/$', Resource(handler=EquipmentOwnerHandler) ),
    url( r'^equipment_owner/(?P<id>\d*)$', Resource(handler=EquipmentOwnerHandler) ),
)
