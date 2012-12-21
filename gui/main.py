# -*- coding: utf-8 -*-

from connection import Connection

def main():
    c = Connection('amihailov.pro', '/rtsup/api')
    succeed, employees = c.get_employee_list()
    print employees
    if succeed:
        print employees['objects'][0]['addr'].encode('utf-8')


import sys
from PySide import QtCore, QtGui
from main_window import Ui_MainWindow

class MyMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._c = Connection('amihailov.pro', '/rtsup/api')
        self._employeeListNextUrl = None
        self._employeeListPrevUrl = None
        self.reset_employee_list(self._c.get_employee_list())

    def reset_employee_list(self, data):
        succeed, employees = data
        if succeed:
            t = self.ui.employeeListTable
            t.clearContents()
            t.setRowCount(0)
            size = len(employees['objects'])
            t.setRowCount(size)
            for i in xrange(size):
                e = employees['objects'][i]
                t.setVerticalHeaderItem(i, QtGui.QTableWidgetItem('%d' % e['id']))
                t.setItem(i, 0, QtGui.QTableWidgetItem(e['snils']))
                t.setItem(i, 1, QtGui.QTableWidgetItem(e['name'] ))
            t.resizeColumnsToContents()
            legend = self.ui.employeeListPageIndicator
            legend.setText(u'%d из %d' % (employees['meta']['page'], employees['meta']['total_pages']))
            self._employeeListNextUrl = employees['meta']['uri_next']
            self._employeeListPrevUrl = employees['meta']['uri_previous']
        else:
            print 'Cannot receive data'



def uimain():
    app = QtGui.QApplication(sys.argv)
    myapp = MyMainWindow()
    myapp.show()
    myapp.reset_employee_list(None)
    sys.exit(app.exec_())

if __name__ == '__main__':
    uimain()