# -*- coding: utf-8 -*-

from django.db import models

import settings as s

# Приоритет заявки
class TaskPriority(models.Model):
    name  = models.CharField(max_length=s.TASK_PRIORITY_NAME_LENGTH, unique=True)
    
    class Meta:
        app_label = 'right'
        db_table = 'v_task_priority'

    def save(self, *args, **kwargs):
        return
    
    def delete(self, *args, **kwargs):
        return
    