# -*- coding: utf-8 -*-

from django.db import models
from piston.handler import BaseHandler

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
    
    

class Handler(BaseHandler):
    allowed_methods = ('PUSH','GET','PUT','DELETE')
    model  = EquipmentOwner
    fields = ('id', 'start_datetime', 'finish_datetime', 'equipment', 'employee')
     