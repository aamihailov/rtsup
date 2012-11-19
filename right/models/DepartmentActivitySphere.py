# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

import settings as s

# Сфера деятельности
class DepartmentActivitySphere(models.Model):
    name  = models.CharField(max_length=s.ACTIVITY_SPHERE_NAME_LENGTH, unique=True)

    class Meta:
        app_label = 'right'
        db_table = 'department_activity_sphere'



class Handler( ModelResource ):
    class Meta:
        queryset = DepartmentActivitySphere.objects.all()
        resource_name = 'department_activity_sphere'
        
    filtering = {
             'id'     : ALL,
             'name'   : ALL,
    }
        