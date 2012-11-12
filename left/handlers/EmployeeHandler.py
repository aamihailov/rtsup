from piston.handler import BaseHandler
from left.models import Employee



class EmployeeHandler(BaseHandler):
    allowed_methods = ('PUSH','GET','PUT','DELETE')
    model  = Employee
    fields = ('id', 'snils', 'name', 'phone', 'addr', 'login', 'password', 'role')
