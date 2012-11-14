# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource

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
    detail_category_url = fields.ForeignKey(DetailCategory.Handler, 'detail_category')
    detail_category_id  = fields.IntegerField('detail_category_id')
    class Meta:
        queryset = DetailModel.objects.all()
        resource_name = 'detail_model'
