# -*- coding: utf-8 -*-

from django.db import models
from piston.handler import BaseHandler

query = open('common_data/requests/r02.sql').read()

class LastTasksManager(models.Manager):
    def all(self):
        return super(LastTasksManager, self).raw(query)

    def filter(self):
        return super(LastTasksManager, self).raw(query)

class LastTasks(models.Model):
    task_id  = models.IntegerField(primary_key=True)
    priority = models.CharField()
    task     = models.CharField()
    technic  = models.CharField()
    state    = models.CharField()
    datetime = models.DateTimeField()
    
    objects  = LastTasksManager()
    
    class Meta:
        abstract = True
        app_label = 'left'
        db_table = None
        
    def __str__(self):
        format = '[%d : %s : %s : %s : %s : %s]'
        return format % (self.task_id, self.priority, self.task, 
                         self.technic, self.state, self.datetime)
    
    def __unicode__(self):
        return self.__str__()
    
    
    
class Handler(BaseHandler):
    allowed_methods = ('GET')
    model  = LastTasks
    fields = ('task_id', 'priority', 'task', 'technic', 'state', 'datetime')
    
    def read(self, request):
        return list( self.model.objects.all() )
