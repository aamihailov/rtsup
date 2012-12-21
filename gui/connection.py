# -*- coding: utf-8 -*-

from httplib import HTTPConnection
import urllib
import json
import datetime
from dateutil import parser as checkdate

import base64
import string

class Connection:
    def __init__(self, host, prefix, proxy=None):
        self._host   = host
        self._prefix = prefix

        self._proxy  = proxy
        if self._proxy:
            self._proxy['auth'] = 'Basic ' + string.strip(base64.encodestring('%s:%s' % (self._proxy['username'], self._proxy['password'])))
        self._connhost = self._host if not self._proxy else '%s:%d' % (self._proxy['host'], self._proxy['port'])
        self._socket = HTTPConnection(self._connhost)

    def _checkAndReconnectIfNeed(self):
        try:
            self._socket.sock.settimeout(5.0)
            self._socket.request('GET', '/')
            self._socket.getresponse().read()
        except:
            print u'Обнаружен обрыв сокета... Пересоединение...'
            self._socket = HTTPConnection(self._connhost)

    def _sendrecv(self, method, resource, checkJSON=True):
        print method, resource
        try:
            self._checkAndReconnectIfNeed()

            url   = 'http://' + self._host + self._prefix + resource

            proxyAuth = None
            if self._proxy:
                proxyAuth = {'Proxy-Authorization' : self._proxy['auth'], 'Host' : self._host}

            self._socket.request(method, url, headers = proxyAuth if self._proxy else dict())
            resp  = self._socket.getresponse()
            ctype = resp.getheader('Content-Type', 'text/html')
            if resp.status >= 400:
                raise Exception, 'Server tells us smth about an error %d. So bad.' % resp.status
            elif checkJSON and 'application/json' not in ctype:
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
            succeed, data = self._sendrecv(method, resource, False)
            return succeed, data
        except Exception, e:
            print e
            return False, None

    def remove_equipment_from_task(self, task_id, equipment_id):
        try:
            method   = 'DELETE'
            resource = '/task/%d/equipment/%d/' % (task_id, equipment_id)
            succeed, data = self._sendrecv(method, resource, False)
            return succeed, data
        except Exception, e:
            print e
            return False, None

    def add_task(self, client_id, name, time=datetime.datetime.now().isoformat(), priority=3):
        try:
            #time = datetime.datetime.isoformat(time)
            method   = 'POST'
            params   = urllib.urlencode({'client_id' : '%d'   % client_id,
                                         'datetime'  : '%s'   % time,
                                         'name'      : '%s'   % name,
                                         'priority'  : '%d'   % priority})
            resource = '/task/?%s' % params
            succeed, data = self._sendrecv(method, resource, False)
            return succeed, data
        except Exception, e:
            print e
            return False, None

