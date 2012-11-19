# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

import settings as s

# Модель оборудования
class EquipmentModel(models.Model):
    name      = models.CharField(max_length=s.EQ_MODEL_NAME_LENGTH, unique=True)
    category  = models.ForeignKey('EquipmentCategory')
    
    class Meta:
        app_label = 'left'
        db_table = 'equipment_model'



import EquipmentCategory
class Handler( ModelResource ):
    category     = fields.ForeignKey(EquipmentCategory.Handler, 'category')
    category_id  = fields.IntegerField('category_id')
    
    class Meta:
        queryset = EquipmentModel.objects.all()
        resource_name = 'equipment_model'

    filtering = {
        'id'        : ALL,
        'name'      : ALL,
        'category'  : ALL_WITH_RELATIONS,
    }
