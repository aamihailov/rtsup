# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

import settings as s

# Ремонт
class Repair(models.Model):
    comment              = models.CharField(max_length=s.EQ_ASS_NAME_LENGTH)
    datetime             = models.DateTimeField()
    detail_model         = models.ForeignKey('DetailModel')
    equipment_operation  = models.ForeignKey('EquipmentOperation')
    task                 = models.ForeignKey('Task')
    
    class Meta:
        app_label = 'left'
        db_table = 'repair'



import DetailModel
import EquipmentOperation
import Task
class Handler( ModelResource ):
    detail_model     = fields.ForeignKey(DetailModel.Handler, 'detail_model')
    detail_model_id  = fields.IntegerField('detail_model_id')

    equipment_operation     = fields.ForeignKey(EquipmentOperation.Handler, 'equipment_operation')
    equipment_operation_id  = fields.IntegerField('equipment_operation_id')

    task     = fields.ForeignKey(Task.Handler, 'task')
    task_id  = fields.IntegerField('task_id')
    
    class Meta:
        queryset = Repair.objects.all()
        resource_name = 'repair'

    filtering = {
        'id'                    : ALL,
        'comment'               : ALL,
        'datetime'              : ALL,
        'detail_model'          : ALL_WITH_RELATIONS,
        'equipment_operation'   : ALL_WITH_RELATIONS,
        'task'                  : ALL_WITH_RELATIONS,
    }
