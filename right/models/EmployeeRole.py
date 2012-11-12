# -*- coding: utf-8 -*-

from django.db import models
from piston.handler import BaseHandler

import settings as s

# Должность сотрудника
class EmployeeRole(models.Model):
    name = models.CharField(max_length=s.EMPLOYEE_ROLE_NAME_LENGTH, unique=True)

    class Meta:
        app_label = 'right'
        db_table = 'employee_role'



class Handler(BaseHandler):
    allowed_methods = ('PUSH','GET','PUT','DELETE')
    model  = EmployeeRole
    fields = ('id', 'name')
   