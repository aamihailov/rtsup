# -*- coding: utf-8 -*-

from django.db import models
from piston.handler import BaseHandler

import settings as s

# Модель оборудования
class EquipmentModel(models.Model):
    name      = models.CharField(max_length=s.EQ_MODEL_NAME_LENGTH, unique=True)
    category  = models.ForeignKey('EquipmentCategory')
    
    class Meta:
        app_label = 'left'
        db_table = 'equipment_model'



class DetailModel(BaseHandler):
    allowed_methods = ('PUSH','GET','PUT','DELETE')
    model  = EquipmentModel
    fields = ('id', 'name', 'category')
