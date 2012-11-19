# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

# Операции с заявкой
class TaskOperation(models.Model):
    work_price  = models.FloatField(null=True)
    datetime    = models.DateTimeField()
    task        = models.ForeignKey('Task')
    technic     = models.ForeignKey('right.Employee', related_name='technic_id')
    state       = models.ForeignKey('TaskState')
    
    class Meta:
        app_label = 'left'
        db_table  = 'task_operation'



import Task
from right.models import EmployeeHandler
import TaskState
class Handler( ModelResource ):
    task     = fields.ForeignKey(Task.Handler, 'task')
    task_id  = fields.IntegerField('task_id')

    technic     = fields.ForeignKey(EmployeeHandler, 'technic')
    technic_id  = fields.IntegerField('technic_id')
    
    state     = fields.ForeignKey(TaskState.Handler, 'state')
    state_id  = fields.IntegerField('state_id')
    
    class Meta:
        queryset = TaskOperation.objects.all()
        resource_name = 'task_operation'

    filtering = {
        'id'        : ALL,
        'work_price': ALL,
        'datetime'  : ALL,
        'task'      : ALL_WITH_RELATIONS,
        'technic'   : ALL_WITH_RELATIONS,
        'state'     : ALL_WITH_RELATIONS,
    }
