# -*- coding: utf-8 -*-

from django.db import models

import settings as s
from EmployeeOperationType import EmployeeOperationType
from EquipmentOwner import EquipmentOwner

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
    
    def get_general(self):
        return ({'id'       : self.id,
                 'name'     : self.name,
                 'login'    : self.login,
                 'snils'    : self.snils,
                 'phone'    : self.phone,
                 'addr'     : self.addr,
                 'role'     : self.role.name,
                 'resource_uri' : ( '/employee/%d/' % self.id )
               })
    
    def get_operations(self):
        ans = []
        ops = self.employeeoperation_set.select_related("type").all()
        for op in ops:
            ans.append({'id'   : op.id,
                        'type' : op.type.name, 
                        'date' : ('%s' % op.date) })
        return ans
    
    def get_equipment(self):
        ans = []
        eos = EquipmentOwner.objects.filter(employee_id=self.id)\
                                    .select_related('equipment', 'equipment__equipment_model')\
                                    .order_by('start_datetime','finish_datetime')
        none_or_str = lambda x: None if not x else '%s' % x
        for eo in eos:
            ans.append({'equipment'     : eo.equipment.get_general(),
                        'date_begin'    : none_or_str(eo.start_datetime),
                        'date_end'      : none_or_str(eo.finish_datetime),
                        'actual'        : (eo.finish_datetime == None)
                        })
        return ans
        
    def get_tasks(self):
        ans = []
        ts  = self.as_client_set.all().select_related('owner').order_by('datetime')
        for t in ts:
            ans.append({'id'       : t.id,
                        'name'     : t.name,
                        'owner'    : t.owner.get_general() if t.owner else None,
                        'datetime' : ( '%s' % t.datetime )})
        return ans
    
    def have_admin_rights(self):
        return self.admins_set.exists()
    
    def have_technic_rights(self):
        return self.technics_set.exists()
    