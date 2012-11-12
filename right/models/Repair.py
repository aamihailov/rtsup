# -*- coding: utf-8 -*-

from django.db import models

import settings as s

# Ремонт
class Repair(models.Model):
    comment              = models.CharField(max_length=s.EQ_ASS_NAME_LENGTH)
    datetime             = models.DateTimeField()
    detail_model         = models.ForeignKey('DetailModel')
    equipment_operation  = models.ForeignKey('EquipmentOperation')
    task                 = models.ForeignKey('Task')
    
    class Meta:
        app_label = 'right'
        db_table = 'v_repair'

    def save(self, *args, **kwargs):
        return
    
    def delete(self, *args, **kwargs):
        return
    