# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource

import settings as s

# Должность сотрудника
class EmployeeRole(models.Model):
    name = models.CharField(max_length=s.EMPLOYEE_ROLE_NAME_LENGTH, unique=True)

    class Meta:
        app_label = 'right'
        db_table = 'employee_role'



class Handler( ModelResource ):
    class Meta:
        queryset = EmployeeRole.objects.all()
        resource_name = 'employee_role'
   