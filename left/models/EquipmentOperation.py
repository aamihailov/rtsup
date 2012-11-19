# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

# Операции с оборудованием
class EquipmentOperation(models.Model):
    detail_price = models.FloatField(null=True)
    datetime     = models.DateTimeField()
    equipment    = models.ForeignKey('Equipment')
    type         = models.ForeignKey('EquipmentOperationType')
    
    class Meta:
        app_label = 'left'
        db_table = 'equipment_operation'



import Equipment
import EquipmentOperationType
class Handler( ModelResource ):
    equipment     = fields.ForeignKey(Equipment.Handler, 'equipment')
    equipment_id  = fields.IntegerField('equipment_id')
    type          = fields.ForeignKey(EquipmentOperationType.Handler, 'type')
    type_id       = fields.IntegerField('type_id')
    
    class Meta:
        queryset = EquipmentOperation.objects.all()
        resource_name = 'equipment_operation'

    filtering = {
        'id'          : ALL,
        'detail_price': ALL,
        'datetime'    : ALL,
        'equipment'   : ALL_WITH_RELATIONS,
        'type'        : ALL_WITH_RELATIONS,
    }
    