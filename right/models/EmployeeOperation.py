# -*- coding: utf-8 -*-

from django.db import models
from piston.handler import BaseHandler

# Операции с сотрудниками
class EmployeeOperation(models.Model):
    date        = models.DateField()
    type        = models.ForeignKey('EmployeeOperationType')
    employee    = models.ForeignKey('Employee')
    department  = models.ForeignKey('Department')
        
    class Meta:
        app_label = 'right'
        db_table  = 'employee_operation'
    


class Handler(BaseHandler):
    allowed_methods = ('PUSH','GET','PUT','DELETE')
    model  = EmployeeOperation
    fields = ('id', 'date', 'type', 'employee', 'department')
            