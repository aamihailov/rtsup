from piston.handler import BaseHandler
from left.models import StatisticsByTechnic



class SBTHandler(BaseHandler):
    allowed_methods = ('GET',)
    model  = StatisticsByTechnic
    fields = ('id', 'name', 'priority', 'count')
    
    def read(self, request, snils):
        return list( self.model.objects.filter(snils) )
