# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource

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
    equipment_category_url = fields.ForeignKey(EquipmentCategory.Handler, 'equipment_category')
    equipment_category_id  = fields.IntegerField('equipment_category_id')
    
    class Meta:
        queryset = EquipmentModel.objects.all()
        resource_name = 'equipment_model'
