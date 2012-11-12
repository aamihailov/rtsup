# -*- coding: utf-8 -*-

from django.db import models
from piston.handler import BaseHandler

import settings as s

# Сфера деятельности
class DepartmentActivitySphere(models.Model):
    name  = models.CharField(max_length=s.ACTIVITY_SPHERE_NAME_LENGTH, unique=True)

    class Meta:
        app_label = 'right'
        db_table = 'department_activity_sphere'



class Handler(BaseHandler):
    allowed_methods = ('PUSH','GET','PUT','DELETE')
    model  = DepartmentActivitySphere
    fields = ('id', 'name')
