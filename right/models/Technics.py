# -*- coding: utf-8 -*-

from django.db import models
from piston.handler import BaseHandler

# Техник
class Technics(models.Model):
    employee = models.ForeignKey('Employee', primary_key=True)
    
    class Meta:
        app_label = 'right'
        db_table = 'technics'
    


class Handler(BaseHandler):
    allowed_methods = ('PUSH','GET','PUT','DELETE')
    model  = Technics
    fields = ('id', 'employee')
