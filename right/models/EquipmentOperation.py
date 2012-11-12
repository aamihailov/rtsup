# -*- coding: utf-8 -*-

from django.db import models

# Операции с оборудованием
class EquipmentOperation(models.Model):
    detail_price = models.FloatField(null=True)
    datetime     = models.DateTimeField()
    equipment    = models.ForeignKey('Equipment')
    eq_oper_type = models.ForeignKey('EquipmentOperationType')
    
    class Meta:
        app_label = 'right'
        db_table = 'v_equipment_operation'

    def save(self, *args, **kwargs):
        return
    
    def delete(self, *args, **kwargs):
        return
    