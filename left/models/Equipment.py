# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource

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



import EquipmentModel
from right.models import EmployeeHandler
class Handler( ModelResource ):
    equipment_model_url = fields.ForeignKey(EquipmentModel.Handler, 'equipment_model')
    equipment_model_id  = fields.IntegerField('equipment_model_id')
    
    owner_urls          = fields.ManyToManyField(EmployeeHandler, 'owner__employee')
    #owner_ids           = fields.IntegerField('equipment_model_id')
    
    class Meta:
        queryset = Equipment.objects.all()
        resource_name = 'equipment'
