# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

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



import DepartmentActivitySphere
class Handler( ModelResource ):
    activity_sphere     = fields.ForeignKey(DepartmentActivitySphere.Handler, 'activity_sphere')
    activity_sphere_id  = fields.IntegerField('activity_sphere_id')
    
    class Meta:
        queryset = Department.objects.all()
        resource_name = 'department'
        
    filtering = {
             'id'                : ALL,
             'name'              : ALL,
             'phone'             : ALL,
             'idemail'           : ALL,
             'addr'              : ALL,
             'exists_now'        : ALL,
             'activity_sphere'   : ALL_WITH_RELATIONS,
    }
