# -*- coding: utf-8 -*-

from django.db import models
from piston.handler import BaseHandler

import settings as s

# Категория узла
class DetailCategory(models.Model):
    name  = models.CharField(max_length=s.NODE_CATEGORY_NAME_LENGTH, unique=True)
    
    class Meta:
        app_label = 'left'
        db_table = 'detail_category'
    


class Handler(BaseHandler):
    allowed_methods = ('PUSH','GET','PUT','DELETE')
    model  = DetailCategory
    fields = ('id', 'name')
