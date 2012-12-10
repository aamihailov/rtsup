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
    
    def date_in(self):
        ops = list(self.employeeoperation_set.filter(type__id=1))
        if len(ops) > 0:
            return ops[0].date
        else:
            return None
    
    def date_out(self):
        ops = list(self.employeeoperation_set.filter(type__id=2))
        if len(ops) > 0:
            return ops[0].date
        else:
            return None
        
    def vacations(self):
        dates_beg = list(self.employeeoperation_set.filter(type__id=3))
        dates_end = list(self.employeeoperation_set.filter(type__id=4))
        result = []
        for i in xrange(len(dates_end)):
            result.append((dates_beg[i].date, dates_end[i].date))
        return result
    
    def my_equipment(self):
        return list(self.equipment_set.all())
    
    

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
             'role'   : ALL_WITH_RELATIONS,
        }