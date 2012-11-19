# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

import settings as s

# Сотрудник
class Employee(models.Model):
    snils       = models.CharField(max_length=s.SNILS_LENGTH, unique=True)
    name        = models.CharField(max_length=s.EMPLOYEE_NAME_LENGTH)
    phone       = models.CharField(max_length=s.EMPLOYEE_PHONE_LENGTH)
    addr        = models.CharField(max_length=s.EMPLOYEE_ADDR_LENGTH)
    login       = models.CharField(max_length=s.EMPLOYEE_LOGIN_LENGTH, null=True, unique=True)    
    password    = models.CharField(max_length=s.EMPLOYEE_PASSWORD_LENGTH, null=True)
    role        = models.ForeignKey('EmployeeRole')
         
    class Meta:
        app_label = 'right'
        db_table = 'employee'
        
    def __str__(self):
        format = '[%d : %s : %s : %s : %s]'
        return format % (self.id, self.name, self.snils, self.phone, self.login)
    
    def __unicode__(self):
        return self.__str__()
    

import EmployeeRole
class Handler( ModelResource ):
    role     = fields.ForeignKey  (EmployeeRole.Handler, 'role')
    role_id  = fields.IntegerField('role_id')
    
    class Meta:
        queryset = Employee.objects.all()
        resource_name = 'employee'

        filtering = {
             'id'     : ALL,
             'snils'  : ALL,
             'name'   : ALL,
             'phone'  : ALL,
             'addr'   : ALL,
             'login'  : ALL,
             'date'   : ALL,
             'role'   : ALL_WITH_RELATIONS,
        }