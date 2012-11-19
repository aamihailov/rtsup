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
    type = fields.ForeignKey(EmployeeOperationType.Handler, 'type')
    type_id  = fields.IntegerField('type_id')

    employee = fields.ForeignKey(Employee.Handler, 'employee')
    employee_id  = fields.IntegerField('employee_id')
    
    department = fields.ForeignKey(Department.Handler, 'department')
    department_id  = fields.IntegerField('department_id')

    class Meta:
        queryset = EmployeeOperation.objects.all()
        resource_name = 'employee_operation'
        
        filtering = {
             'id'         : ALL,
             'date'       : ALL,
             'type'       : ALL_WITH_RELATIONS,
             'employee'   : ALL_WITH_RELATIONS,
             'department' : ALL_WITH_RELATIONS,
        }
            