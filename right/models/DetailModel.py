# -*- coding: utf-8 -*-

from django.db import models

import settings as s

# Модель детали
class DetailModel(models.Model):
    name      = models.CharField(max_length=s.DETAIL_MODEL_NAME_LENGTH, unique=True)
    category  = models.ForeignKey('DetailCategory')
    
    class Meta:
        app_label = 'right'
        db_table  = 'v_detail_model'

    def save(self, *args, **kwargs):
        return
    
    def delete(self, *args, **kwargs):
        return
