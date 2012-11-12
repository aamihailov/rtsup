# -*- coding: utf-8 -*-

from django.db import models
from piston.handler import BaseHandler

import settings as s

# Типы операций с сотрудниками
class EmployeeOperationType(models.Model):
    name        = models.CharField(max_length=s.EMPL_OPER_TYPE_NAME_LENGTH, unique=True)
    
    class Meta:
        app_label = 'right'
        db_table = 'employee_operation_type'



class Handler(BaseHandler):
    allowed_methods = ('PUSH','GET','PUT','DELETE')
    model  = EmployeeOperationType
    fields = ('id', 'name')
