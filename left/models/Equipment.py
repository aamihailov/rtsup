# -*- coding: utf-8 -*-

from django.db import models
from piston.handler import BaseHandler

import settings as s

# Оборудование
class Equipment(models.Model):
    name             = models.CharField(max_length=s.EQ_NAME_LENGTH)
    serial_number    = models.CharField(max_length=s.SN_NAME_LENGTH, unique=True)
    addr             = models.CharField(max_length=s.EQ_ADDR_LENGTH, null=True)
    equipment_model  = models.ForeignKey('EquipmentModel')
    owner            = models.ManyToManyField('right.Employee', through='right.EquipmentOwner')
     
    class Meta:
        app_label = 'left'
        db_table = 'equipment'



class DetailModel(BaseHandler):
    allowed_methods = ('PUSH','GET','PUT','DELETE')
    model  = Equipment
    fields = ('id', 'name', 'serial_number', 'addr', 'equipment_model', 'owner')
