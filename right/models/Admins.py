# -*- coding: utf-8 -*-

from django.db import models
from piston.handler import BaseHandler

# Администратор
class Admins(models.Model):
    employee = models.ForeignKey('Employee', primary_key=True)
    
    class Meta:
        app_label = 'right'
        db_table = 'admins'
    
    
    
class Handler(BaseHandler):
    allowed_methods = ('PUSH','GET','PUT','DELETE')
    model  = Admins
    fields = ('employee')
