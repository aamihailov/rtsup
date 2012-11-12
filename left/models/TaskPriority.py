# -*- coding: utf-8 -*-

from django.db import models
from piston.handler import BaseHandler

import settings as s

# Приоритет заявки
class TaskPriority(models.Model):
    name  = models.CharField(max_length=s.TASK_PRIORITY_NAME_LENGTH, unique=True)
    
    class Meta:
        app_label = 'left'
        db_table = 'task_priority'



class Handler(BaseHandler):
    allowed_methods = ('PUSH','GET','PUT','DELETE')
    model  = TaskPriority
    fields = ('id', 'name')
    