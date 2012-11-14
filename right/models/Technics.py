# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource

# Техник
class Technics(models.Model):
    employee = models.ForeignKey('Employee', primary_key=True)
    
    class Meta:
        app_label = 'right'
        db_table = 'technics'
    


import Employee
class Handler( ModelResource ):
    employee_url = fields.ForeignKey(Employee.Handler, 'employee')
    employee_id  = fields.IntegerField('employee_id')

    class Meta:
        queryset = Technics.objects.all()
        resource_name = 'technics'
