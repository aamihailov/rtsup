# -*- coding: utf-8 -*-

from django.db import models

import settings as s

# Модель оборудования
class EquipmentModel(models.Model):
    name      = models.CharField(max_length=s.EQ_MODEL_NAME_LENGTH, unique=True)
    category  = models.ForeignKey('EquipmentCategory')
    
    class Meta:
        app_label = 'right'
        db_table = 'v_equipment_model'

    def save(self, *args, **kwargs):
        return
    
    def delete(self, *args, **kwargs):
        return
