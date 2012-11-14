# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource

import settings as s

# Типы операций с сотрудниками
class EmployeeOperationType(models.Model):
    name        = models.CharField(max_length=s.EMPL_OPER_TYPE_NAME_LENGTH, unique=True)
    
    class Meta:
        app_label = 'right'
        db_table = 'employee_operation_type'



class Handler( ModelResource ):
    class Meta:
        queryset = EmployeeOperationType.objects.all()
        resource_name = 'employee_operation_type'
