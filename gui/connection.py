from httplib import HTTPConnection
import json
import datetime
from dateutil import parser as checkdate

class Connection:
    def __init__(self, host, prefix):
        self._host   = host
        self._prefix = prefix
        self._socket = HTTPConnection(self._host)
    
    def _sendrecv(self, method, resource):
        try:
            url   = self._prefix + resource
            self._socket.request(method, url)
            resp  = self._socket.getresponse()
            ctype = resp.getheader('Content-Type', 'text/html')
            if resp.status >= 400:
                raise Exception, 'Server tells us smth about an error %d. So bad.' % resp.status
            elif 'application/json' not in ctype:
                raise Exception, 'Server doesn\'t sent us application/json, but %s' % ctype
            else:
                body = resp.read()
                obj  = {}
                if len(body) != 0:
                    obj  = json.loads(body)
                return True, obj                 
        except Exception, e:
            print e
            return False, None
    
    def get_employee_list(self, limit=20, offset=0, exist=1):
        try:
            method   = 'GET'
            resource = '/employee/?limit=%d&offset=%d&exist=%d' % (limit, offset, exist)
            succeed, data = self._sendrecv(method, resource)
            return succeed, data
        except Exception, e:
            print e
            return False, None
            
    def get_employee(self, employee_id):
        try:
            method   = 'GET'
            resource = '/employee/%d/' % employee_id
            succeed, data = self._sendrecv(method, resource)
            return succeed, data
        except Exception, e:
            print e
            return False, None

    def get_equipment(self, equipment_id):
        try:
            method   = 'GET'
            resource = '/equipment/%d/' % equipment_id
            succeed, data = self._sendrecv(method, resource)
            return succeed, data
        except Exception, e:
            print e
            return False, None

    def get_equipment_for_task(self, task_id):
        try:
            method   = 'GET'
            resource = '/task/%d/equipment/' % task_id
            succeed, data = self._sendrecv(method, resource)
            return succeed, data
        except Exception, e:
            print e
            return False, None

    def add_equipment_to_task(self, task_id, equipment_id):
        try:
            method   = 'POST'
            resource = '/task/%d/equipment/%d/' % (task_id, equipment_id)
            succeed, data = self._sendrecv(method, resource)
            return succeed, data
        except Exception, e:
            print e
            return False, None

    def remove_equipment_from_task(self, task_id, equipment_id):
        try:
            method   = 'DELETE'
            resource = '/task/%d/equipment/%d/' % (task_id, equipment_id)
            succeed, data = self._sendrecv(method, resource)
            return succeed, data
        except Exception, e:
            print e
            return False, None

    def add_task(self, client_id, name, time=datetime.datetime.now(), priority=3):
        try:
            time = datetime.datetime.isoformat(time)
            method   = 'DELETE'
            resource = '/task/?client_id=%d&datetime="%s"&name="%s"&priority=%d' % (
                                        client_id,
                                        name,
                                        time,
                                        priority)
            succeed, data = self._sendrecv(method, resource)
            return succeed, data
        except Exception, e:
            print e
            return False, None

