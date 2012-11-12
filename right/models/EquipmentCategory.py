# -*- coding: utf-8 -*-

from django.db import models

import settings as s

# Категория узла
class EquipmentCategory(models.Model):
    name  = models.CharField(max_length=s.NODE_CATEGORY_NAME_LENGTH, unique=True)
    
    class Meta:
        app_label = 'right'
        db_table  = 'v_equipment_category'

    def save(self, *args, **kwargs):
        return
    
    def delete(self, *args, **kwargs):
        return
    