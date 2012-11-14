# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource

# Операции с оборудованием
class EquipmentOperation(models.Model):
    detail_price = models.FloatField(null=True)
    datetime     = models.DateTimeField()
    equipment    = models.ForeignKey('Equipment')
    eq_oper_type = models.ForeignKey('EquipmentOperationType')
    
    class Meta:
        app_label = 'left'
        db_table = 'equipment_operation'



import Equipment
import EquipmentOperationType
class Handler( ModelResource ):
    equipment_url = fields.ForeignKey(Equipment.Handler, 'equipment')
    equipment_id  = fields.IntegerField('equipment_id')
    equipment_operation_type_url = fields.ForeignKey(EquipmentOperationType.Handler, 'equipment_operation_type')
    equipment_operation_type_id  = fields.IntegerField('equipment_operation_type_id')
    
    class Meta:
        queryset = EquipmentOperation.objects.all()
        resource_name = 'equipment_operation'
    