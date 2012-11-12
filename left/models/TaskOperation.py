# -*- coding: utf-8 -*-

from django.db import models
from piston.handler import BaseHandler

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



class Handler(BaseHandler):
    allowed_methods = ('PUSH','GET','PUT','DELETE')
    model  = TaskOperation
    fields = ('id', 'work_price', 'datetime', 'task', 'technic', 'state')
    