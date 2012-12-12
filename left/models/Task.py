# -*- coding: utf-8 -*-

from django.db import models

import settings as s

# Заявка
class Task(models.Model):
    name      = models.CharField(max_length=s.TASK_NAME_LENGTH)
    datetime  = models.DateTimeField()
    priority  = models.ForeignKey('TaskPriority')
    client    = models.ForeignKey('right.Employee', related_name='as_client_set')
    owner     = models.ForeignKey('right.Employee', related_name='as_owner_set', null=True)
    equipment = models.ManyToManyField('Equipment')
        
    class Meta:
        app_label = 'left'
        db_table = 'task'

    def get_attached_equipment(self):
        return [ eq.get_general() for eq in self.equipment.all() ]
        