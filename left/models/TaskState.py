# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

import settings as s

# Статус заявки
class TaskState(models.Model):
    name  = models.CharField(max_length=s.TASK_STATE_NAME_LENGTH, unique=True)
    
    class Meta:
        app_label = 'left'
        db_table = 'task_state'
    


class Handler( ModelResource ):
    class Meta:
        queryset = TaskState.objects.all()
        resource_name = 'task_state'

    filtering = {
        'id'        : ALL,
        'name'      : ALL,
    }
