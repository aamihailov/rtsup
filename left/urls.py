from django.conf.urls import patterns, include, url

from tastypie.api import Api

from left.models import *

api = Api(api_name='left')
api.register(DetailCategoryHandler())
api.register(DetailModelHandler())
api.register(EquipmentCategoryHandler())
api.register(EquipmentModelHandler())
api.register(EquipmentHandler())
api.register(EquipmentOperationTypeHandler())
api.register(EquipmentOperationHandler())
api.register(TaskPriorityHandler())
api.register(TaskHandler())
api.register(RepairHandler())
api.register(TaskStateHandler())
api.register(TaskOperationHandler())
