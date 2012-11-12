# -*- coding: utf-8 -*-

from django.db import models

# Администратор
class Admins(models.Model):
    employee = models.ForeignKey('Employee', primary_key=True)
    
    class Meta:
        app_label = 'left'
        db_table = 'v_admins'
    
    def save(self, *args, **kwargs):
        return
    
    def delete(self, *args, **kwargs):
        return
    
    