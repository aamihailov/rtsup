# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

import settings as s

# Типы операций с оборудованием
class EquipmentOperationType(models.Model):
    name  = models.CharField(max_length=s.EQ_OPER_TYPE_NAME_LENGTH, unique=True)
    
    class Meta:
        app_label = 'left'
        db_table = 'equipment_operation_type'



class Handler( ModelResource ):
    class Meta:
        queryset = EquipmentOperationType.objects.all()
        resource_name = 'equipment_operation_type'

    filtering = {
        'id'        : ALL,
        'name'      : ALL,
    }
    