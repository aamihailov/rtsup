# -*- coding: utf-8 -*-

from django.db import models

import settings as s

from right.models import EquipmentOwner

# Оборудование
class Equipment(models.Model):
    name             = models.CharField(max_length=s.EQ_NAME_LENGTH)
    serial_number    = models.CharField(max_length=s.SN_NAME_LENGTH, unique=True)
    addr             = models.CharField(max_length=s.EQ_ADDR_LENGTH, null=True)
    equipment_model  = models.ForeignKey('EquipmentModel')
    owner            = models.ManyToManyField('right.Employee', through='right.EquipmentOwner')
     
    class Meta:
        app_label = 'left'
        db_table = 'equipment'
        
    def __str__(self):
        format = '[%d : %s : %s : %s : %d]'
        return format % (self.id, self.name, self.serial_number, self.addr, self.equipment_model_id)
    
    def __unicode__(self):
        return self.__str__()
    
    def get_general(self):
        return ({'id'               : self.id,
                 'name'             : self.name,
                 'serial_number'    : self.serial_number,
                 'addr'             : self.addr,
                 'model'            : self.equipment_model.name,
                 'resource_uri'     : ( '/equipment/%d/' % self.id ),
               })
        
    def get_owners(self):
        ans = []
        eos = EquipmentOwner.objects.filter(equipment_id=self.id)\
                                    .select_related('employee', 'employee__role')\
                                    .order_by('start_datetime','finish_datetime')
        none_or_str = lambda x: None if not x else '%s' % x
        for eo in eos:
            ans.append({'employee'      : eo.employee.get_general(),
                        'date_begin'    : none_or_str(eo.start_datetime),
                        'date_end'      : none_or_str(eo.finish_datetime),
                        'actual'        : (eo.finish_datetime == None)
                        })
        return ans

    def get_operations(self):
        ans = []
        ops = self.equipmentoperation_set.select_related("eq_oper_type").all()
        for op in ops:
            ans.append({'id'       : op.id,
                        'type'     : op.eq_oper_type.name, 
                        'datetime' : ('%s' % op.datetime) })
        return ans
    
    def get_tasks(self):
        ans = []
        ts  = self.task_set.all().select_related('owner', 
                                                 'owner__role', 
                                                 'client', 
                                                 'client__role').order_by('datetime')
        for t in ts:
            ans.append({'id'       : t.id,
                        'name'     : t.name,
                        'owner'    : t.owner.get_general(),
                        'client'   : t.client.get_general(),
                        'datetime' : ( '%s' % t.datetime )})
        return ans