# -*- coding: utf-8 -*-

from django.db import models
from piston.handler import BaseHandler

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



class Handler(BaseHandler):
    allowed_methods = ('PUSH','GET','PUT','DELETE')
    model  = Repair
    fields = ('id', 'name', 'datetime', 'priority', 'client', 'owner', 'equipment')
    