# -*- coding: utf-8 -*-

class LeftRightRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'left':
            return 'local51_pg'
        elif model._meta.app_label == 'right':
            return 'local52_pg'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'left':
            return 'local51_pg'
        elif model._meta.app_label == 'right':
            return 'local52_pg'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_syncdb(self, db, model):
        "Make sure the myapp app only appears on the 'other' db"
        if db == 'local51_pg':
            return model._meta.app_label == 'left'
        elif db == 'local52_pg':
            return model._meta.app_label == 'right'
        elif model._meta.app_label == 'left':
            return False
        elif model._meta.app_label == 'right':
            return False
        return None