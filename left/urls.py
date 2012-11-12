from django.conf.urls import patterns, include, url
from piston.resource import Resource
from left.handlers import SBTHandler

from left.models import *


urlpatterns = patterns('',
    url( r'^sbt/(?P<snils>\d{3}-\d{3}-\d{3}\ \d{2})$', Resource(handler=SBTHandler) ),
    url( r'^sbt/all/$', Resource(handler=SBTHandler), {'snils':'%'} ),

    url( r'^detail_category/$', Resource(handler=DetailCategoryHandler) ),
    url( r'^detail_category/(?P<id>\d*)$', Resource(handler=DetailCategoryHandler) ),

    url( r'^detail_model/$', Resource(handler=DetailModelHandler) ),
    url( r'^detail_model/(?P<id>\d*)$', Resource(handler=DetailModelHandler) ),

    url( r'^equipment_category/$', Resource(handler=EquipmentCategoryHandler) ),
    url( r'^equipment_category/(?P<id>\d*)$', Resource(handler=EquipmentCategoryHandler) ),

    url( r'^equipment_model/$', Resource(handler=EquipmentModelHandler) ),
    url( r'^equipment_model/(?P<id>\d*)$', Resource(handler=EquipmentModelHandler) ),

    url( r'^equipment/$', Resource(handler=EquipmentHandler) ),
    url( r'^equipment/(?P<id>\d*)$', Resource(handler=EquipmentHandler) ),

    url( r'^equipment_operation_type/$', Resource(handler=EquipmentOperationTypeHandler) ),
    url( r'^equipment_operation_type/(?P<id>\d*)$', Resource(handler=EquipmentOperationTypeHandler) ),

    url( r'^equipment_operation/$', Resource(handler=EquipmentOperationHandler) ),
    url( r'^equipment_operation/(?P<id>\d*)$', Resource(handler=EquipmentOperationHandler) ),

    url( r'^task_priority/$', Resource(handler=TaskPriorityHandler) ),
    url( r'^task_priority/(?P<id>\d*)$', Resource(handler=TaskPriorityHandler) ),

    url( r'^task/$', Resource(handler=TaskHandler) ),
    url( r'^task/(?P<id>\d*)$', Resource(handler=TaskHandler) ),

    url( r'^repair/$', Resource(handler=RepairHandler) ),
    url( r'^repair/(?P<id>\d*)$', Resource(handler=RepairHandler) ),
    
    url( r'^task_state/$', Resource(handler=TaskStateHandler) ),
    url( r'^task_state/(?P<id>\d*)$', Resource(handler=TaskStateHandler) ),

    url( r'^task_operation/$', Resource(handler=TaskOperationHandler) ),
    url( r'^task_operation/(?P<id>\d*)$', Resource(handler=TaskOperationHandler) ),
)
