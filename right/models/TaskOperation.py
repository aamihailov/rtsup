# -*- coding: utf-8 -*-

from django.db import models

# Операции с заявкой
class TaskOperation(models.Model):
    work_price  = models.FloatField(null=True)
    datetime    = models.DateTimeField()
    task        = models.ForeignKey('Task')
    technic     = models.ForeignKey('Employee', related_name='technic_id')
    state       = models.ForeignKey('TaskState')
    
    class Meta:
        app_label = 'right'
        db_table  = 'v_task_operation'

    def save(self, *args, **kwargs):
        return
    
    def delete(self, *args, **kwargs):
        return
    