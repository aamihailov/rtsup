# -*- coding: utf-8 -*-

from django.db import models
from piston.handler import BaseHandler

# Операции с оборудованием
class EquipmentOperation(models.Model):
    detail_price = models.FloatField(null=True)
    datetime     = models.DateTimeField()
    equipment    = models.ForeignKey('Equipment')
    eq_oper_type = models.ForeignKey('EquipmentOperationType')
    
    class Meta:
        app_label = 'left'
        db_table = 'equipment_operation'



class Handler(BaseHandler):
    allowed_methods = ('PUSH','GET','PUT','DELETE')
    model  = EquipmentOperation
    fields = ('id', 'detail_price', 'datetime', 'equipment', 'eq_oper_type')
    