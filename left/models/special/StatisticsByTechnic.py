# -*- coding: utf-8 -*-

from django.db import models
from piston.handler import BaseHandler

query = open('common_data/requests/r01.sql').read()

class SBTManager(models.Manager):
    def all(self):
        return super(SBTManager, self).raw(query,['%'])
    
    def filter(self, snils):
        return super(SBTManager, self).raw(query,[snils])

class StatisticsByTechnic(models.Model):
    id       = models.IntegerField(primary_key=True)
    name     = models.CharField()
    priority = models.CharField()
    count    = models.IntegerField()
    
    objects = SBTManager()
    
    class Meta:
        abstract = True
        app_label = 'left'
        db_table = None
        
    def __str__(self):
        format = '[%d : %s : %s : %d]'
        return format % (self.id, self.name, self.priority, self.count)
    
    def __unicode__(self):
        return self.__str__()   
    

    
class Handler(BaseHandler):
    allowed_methods = ('GET',)
    model  = StatisticsByTechnic
    fields = ('id', 'name', 'priority', 'count')
    
    def read(self, request, snils):
        return list( self.model.objects.filter(snils) )
