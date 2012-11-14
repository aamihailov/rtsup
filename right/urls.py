from django.conf.urls import patterns, include, url
from tastypie.api import Api

from right.models import *

right_rest_api = Api(api_name='rest')
right_rest_api.register(DepartmentHandler())
right_rest_api.register(DepartmentActivitySphereHandler())
right_rest_api.register(EmployeeHandler())
right_rest_api.register(EmployeeRoleHandler())
right_rest_api.register(EmployeeOperationHandler())
right_rest_api.register(EmployeeOperationTypeHandler())
right_rest_api.register(AdminsHandler())
right_rest_api.register(TechnicsHandler())
right_rest_api.register(EquipmentOwnerHandler())

urlpatterns = patterns('',
    url(r'^', include(right_rest_api.urls)),
)
