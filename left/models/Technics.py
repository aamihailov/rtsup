# -*- coding: utf-8 -*-

from django.db import models

# Техник
class Technics(models.Model):
    employee = models.ForeignKey('Employee', primary_key=True)
    
    class Meta:
        app_label = 'left'
        db_table = 'v_technics'
    
    def save(self, *args, **kwargs):
        return
    
    def delete(self, *args, **kwargs):
        return

