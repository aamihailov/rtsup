# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource

# Связь сотрудника и оборудования
class EquipmentOwner(models.Model):
    start_datetime  = models.DateTimeField()
    finish_datetime = models.DateTimeField(null=True)
    equipment       = models.ForeignKey('left.Equipment')
    employee        = models.ForeignKey('Employee')
     
    class Meta:
        app_label = 'right'
        db_table  = 'equipment_owner'
#       unique_together = ('equipment', 'employee')

    def __str__(self):
        format = '[%d : %s : %s : %d : %d]'
        return format % (self.id, self.start_datetime, self.finish_datetime, self.equipment.id, self.employee.id)
    
    def __unicode__(self):
        return self.__str__()
    
    
    
import Employee
#from left.models import EquipmentHandler
class Handler( ModelResource ):
    employee_url  = fields.ForeignKey(Employee.Handler, 'employee')
    employee_id   = fields.IntegerField('employee_id')
#    equipment_url = fields.ForeignKey(EquipmentHandler, 'equipment')
#    equipment_id  = fields.IntegerField('equipment_id')

    class Meta:
        queryset = EquipmentOwner.objects.all()
        resource_name = 'equipment_owner'
     