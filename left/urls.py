from django.conf.urls import patterns, include, url

from piston.resource import Resource

from tastypie.api import Api

from left.models import *

left_rest_api = Api(api_name='rest')
left_rest_api.register(DetailCategoryHandler())
left_rest_api.register(DetailModelHandler())
left_rest_api.register(EquipmentCategoryHandler())
left_rest_api.register(EquipmentModelHandler())
left_rest_api.register(EquipmentHandler())
left_rest_api.register(EquipmentOperationTypeHandler())
left_rest_api.register(EquipmentOperationHandler())
left_rest_api.register(TaskPriorityHandler())
left_rest_api.register(TaskHandler())
left_rest_api.register(RepairHandler())
left_rest_api.register(TaskStateHandler())
left_rest_api.register(TaskOperationHandler())

urlpatterns = patterns('',
    url(r'^', include(left_rest_api.urls)),
)
