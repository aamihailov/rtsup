# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource

import settings as s

# Категория узла
class EquipmentCategory(models.Model):
    name  = models.CharField(max_length=s.NODE_CATEGORY_NAME_LENGTH, unique=True)
    
    class Meta:
        app_label = 'left'
        db_table  = 'equipment_category'



class Handler( ModelResource ):
    class Meta:
        queryset = EquipmentCategory.objects.all()
        resource_name = 'equipment_category'
