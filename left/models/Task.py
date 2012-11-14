# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource

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
    task_priority_url = fields.ForeignKey(TaskPriority.Handler, 'task_priority')
    task_priority_id  = fields.IntegerField('task_priority_id')

    client_url = fields.ForeignKey(EmployeeHandler, 'client')
    client_id  = fields.IntegerField('client_id')
    
    owner_url = fields.ForeignKey(EmployeeHandler, 'owner')
    owner_id  = fields.IntegerField('owner_id')
    
    owner_urls = fields.ManyToManyField(Equipment.Handler, 'equipment')
    owner_ids  = fields.IntegerField('owner_id')
    
    class Meta:
        queryset = Task.objects.all()
        resource_name = 'task'
