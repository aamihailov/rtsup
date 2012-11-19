# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

import settings as s

# Модель детали
class DetailModel(models.Model):
    name      = models.CharField(max_length=s.DETAIL_MODEL_NAME_LENGTH, unique=True)
    category  = models.ForeignKey('DetailCategory')
    
    class Meta:
        app_label = 'left'
        db_table  = 'detail_model'



import DetailCategory
class Handler( ModelResource ):
    category     = fields.ForeignKey(DetailCategory.Handler, 'category')
    category_id  = fields.IntegerField('category_id')
    class Meta:
        queryset = DetailModel.objects.all()
        resource_name = 'detail_model'

    filtering = {
        'id'        : ALL,
        'name'      : ALL,
        'category'  : ALL_WITH_RELATIONS,
    }
