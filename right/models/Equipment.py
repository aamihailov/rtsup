# -*- coding: utf-8 -*-

from django.db import models

import settings as s

# Оборудование
class Equipment(models.Model):
    name             = models.CharField(max_length=s.EQ_NAME_LENGTH)
    serial_number    = models.CharField(max_length=s.SN_NAME_LENGTH, unique=True)
    addr             = models.CharField(max_length=s.EQ_ADDR_LENGTH, null=True)
    equipment_model  = models.ForeignKey('EquipmentModel')
    owner            = models.ManyToManyField('Employee', through='EquipmentOwner')
     
    class Meta:
        app_label = 'right'
        db_table = 'v_equipment'

    def save(self, *args, **kwargs):
        return
    
    def delete(self, *args, **kwargs):
        return
