# -*- coding: utf-8 -*-

from django.db import models

import settings as s

# Должность сотрудника
class EmployeeRole(models.Model):
    name = models.CharField(max_length=s.EMPLOYEE_ROLE_NAME_LENGTH, unique=True)

    class Meta:
        app_label = 'left'
        db_table = 'v_employee_role'
    
    def save(self, *args, **kwargs):
        return
    
    def delete(self, *args, **kwargs):
        return
    