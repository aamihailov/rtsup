# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

import settings as s

# Заявка
class Task(models.Model):
    name      = models.CharField(max_length=s.TASK_NAME_LENGTH)
    datetime  = models.DateTimeField()
    priority  = models.ForeignKey('TaskPriority')
    client    = models.ForeignKey('right.Employee', related_name='client_id')
    owner     = models.ForeignKey('right.Employee', related_name='owner_id', null=True)
    equipment = models.ManyToManyField('Equipment')
        
    class Meta:
        app_label = 'left'
        db_table = 'task'



import TaskPriority
from right.models import EmployeeHandler
import Equipment
class Handler( ModelResource ):
    priority      = fields.ForeignKey(TaskPriority.Handler, 'priority')
    priority_id   = fields.IntegerField('priority_id')

    client        = fields.ForeignKey(EmployeeHandler, 'client')
    client_id     = fields.IntegerField('client_id')
    
    owner         = fields.ForeignKey(EmployeeHandler, 'owner')
    owner_id      = fields.IntegerField('owner_id')
    
    equipment     = fields.ManyToManyField(Equipment.Handler, 'equipment')
    equipment_ids = fields.IntegerField('owner_id')
    
    class Meta:
        queryset = Task.objects.all()
        resource_name = 'task'

    filtering = {
        'id'        : ALL,
        'name'      : ALL,
        'datetime'  : ALL,
        'priority'  : ALL_WITH_RELATIONS,
        'client'    : ALL_WITH_RELATIONS,
        'owner'     : ALL_WITH_RELATIONS,
        'equipment' : ALL_WITH_RELATIONS,
    }
