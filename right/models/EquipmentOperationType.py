# -*- coding: utf-8 -*-

from django.db import models

import settings as s

# Типы операций с оборудованием
class EquipmentOperationType(models.Model):
    name  = models.CharField(max_length=s.EQ_OPER_TYPE_NAME_LENGTH, unique=True)
    
    class Meta:
        app_label = 'right'
        db_table = 'v_equipment_operation_type'

    def save(self, *args, **kwargs):
        return
    
    def delete(self, *args, **kwargs):
        return
    