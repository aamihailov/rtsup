# -*- coding: utf-8 -*-

from django.db import models

import settings as s

# Подразделение
class Department(models.Model):
    name            = models.CharField(max_length=s.DEPARTMENT_NAME_LENGTH, unique=True)
    phone           = models.CharField(max_length=s.DEPARTMENT_PHONE_LENGTH, null=True)
    email           = models.EmailField()
    addr            = models.CharField(max_length=s.DEPARTMENT_ADDR_LENGTH)
    exists_now      = models.BooleanField()
    activity_sphere = models.ForeignKey('DepartmentActivitySphere')
    
    class Meta:
        app_label = 'right'
        db_table = 'department'
