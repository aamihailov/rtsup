# -*- coding: utf-8 -*-

from django.db import models
from piston.handler import BaseHandler

import settings as s

# Модель детали
class DetailModel(models.Model):
    name      = models.CharField(max_length=s.DETAIL_MODEL_NAME_LENGTH, unique=True)
    category  = models.ForeignKey('DetailCategory')
    
    class Meta:
        app_label = 'left'
        db_table  = 'detail_model'



class DetailModel(BaseHandler):
    allowed_methods = ('PUSH','GET','PUT','DELETE')
    model  = DetailModel
    fields = ('id', 'name', 'category')
