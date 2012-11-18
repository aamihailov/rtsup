from django.conf.urls import patterns, include, url
from tastypie.api import Api

from right.models import *

api = Api(api_name='right')
api.register(DepartmentHandler())
api.register(DepartmentActivitySphereHandler())
api.register(EmployeeHandler())
api.register(EmployeeRoleHandler())
api.register(EmployeeOperationHandler())
api.register(EmployeeOperationTypeHandler())
api.register(AdminsHandler())
api.register(TechnicsHandler())
api.register(EquipmentOwnerHandler())
