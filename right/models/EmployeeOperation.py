# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

# Операции с сотрудниками
class EmployeeOperation(models.Model):
    date        = models.DateField()
    type        = models.ForeignKey('EmployeeOperationType')
    employee    = models.ForeignKey('Employee')
    department  = models.ForeignKey('Department')
        
    class Meta:
        app_label = 'right'
        db_table  = 'employee_operation'
    


import EmployeeOperationType
import Employee
import Department
class Handler( ModelResource ):
    employee_operation_type_url = fields.ForeignKey(EmployeeOperationType.Handler, 'type')
    employee_operation_type_id  = fields.IntegerField('type_id')

    employee_url = fields.ForeignKey(Employee.Handler, 'employee')
    employee_id  = fields.IntegerField('employee_id')
    
    department_url = fields.ForeignKey(Department.Handler, 'department')
    department_id  = fields.IntegerField('department_id')

    class Meta:
        queryset = EmployeeOperation.objects.all()
        resource_name = 'employee_operation'
        
        filtering = {
             'date' : ALL,
        }
            