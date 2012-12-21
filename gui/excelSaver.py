# -*- coding: utf-8 -*-

import xlwt

class ExcelSaver(object):
    def __init__(self):
        self._wb = xlwt.Workbook()

    def makeEmployeeList(self, data):
        ws = self._wb.add_sheet(u'EmployeeList (%d of %d)' % (data['meta']['page'], data['meta']['total_pages']))

        hfont       = xlwt.Font()
        hfont.bold  = True
        hstyle      = xlwt.XFStyle()
        hstyle.font = hfont

        ws.write(0, 0, u'id',        hstyle)
        ws.write(0, 1, u'ФИО',       hstyle)
        ws.write(0, 2, u'Должность', hstyle)
        ws.write(0, 3, u'Логин',     hstyle)
        ws.write(0, 4, u'СНИЛС',     hstyle)
        ws.write(0, 5, u'Адрес',     hstyle)
        ws.write(0, 6, u'Телефон',   hstyle)

        size = len(data['objects'])
        for i in xrange(size):
            obj = data['objects'][i]
            ws.write(i+1, 0, obj['id'])
            ws.write(i+1, 1, obj['name'])
            ws.write(i+1, 2, obj['role'])
            ws.write(i+1, 3, obj['login'])
            ws.write(i+1, 4, obj['snils'])
            ws.write(i+1, 5, obj['addr'])
            ws.write(i+1, 6, obj['phone'])


    def save(self, filename):
        self._wb.save(filename)
