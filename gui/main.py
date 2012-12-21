# -*- coding: utf-8 -*-
import datetime

from connection import Connection

import sys
from PySide import QtCore, QtGui
from main_window import Ui_MainWindow
from datetime import datetime

from excelSaver import ExcelSaver



class MyMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def afterRun(self):
        self._employeeListNextUrl = None
        self._employeeListPrevUrl = None
        self.ui.statusBar.showMessage(u'Устанавливается соединение...')
        self._c = Connection('amihailov.pro', '/rtsup/api')
        self.employee_list_get_first_page()
        self.ui.statusBar.showMessage(u'Приложение успешно инициализировано', 1000)
        self.connectSignalsToSlots()

    def connectSignalsToSlots(self):
        self.ui.employeeListForwardButton.clicked.connect(self.employee_list_get_next_page)
        self.ui.employeeListBackButton.clicked.connect(self.employee_list_get_prev_page)
        self.ui.employeeListExistCheckbox.stateChanged.connect(self.employee_list_exist_changed)
        self.ui.employeeListTable.cellClicked.connect(self.employee_list_cell_clicked)
        self.ui.equipmentExistCheckbox.stateChanged.connect(self.equipment_exist_changed)
        self.ui.equipmentListBox.currentIndexChanged.connect(self.equipment_details_update)
        self.ui.tasksListBox.currentIndexChanged.connect(self.tasks_details_update)
        self.ui.taskEquipmentBox.currentIndexChanged.connect(self.tasks_equipment_details_update)
        self.ui.taskEquipmentAttachBox.currentIndexChanged.connect(self.tasks_equipment_attach_update)
        self.ui.taskEquipmentAttachButton.clicked.connect(self.attach_equipment_to_task)
        self.ui.taskEquipmentDetachButton.clicked.connect(self.detach_equipment_from_task)
        self.ui.newTaskButton.clicked.connect(self.publish_new_task)
        self.ui.exportToExcel.clicked.connect(self.export_to_excel)

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

    def employee_list_update_buttons(self):
        self.ui.employeeListForwardButton.setEnabled(self._employeeListNextUrl is not None)
        self.ui.employeeListBackButton.setEnabled(self._employeeListPrevUrl is not None)

    def employee_list_get_first_page(self, onlyExist=True):
        self.ui.statusBar.showMessage(u'Запрашивается первая страница списка сотрудников...')
        self.reset_employee_list(self._c.get_employee_list(exist=(1 if onlyExist else 0)))
        self.employee_list_update_buttons()
        self.ui.statusBar.showMessage(u'Данные успешно получены', 1000)

    def employee_list_get_next_page(self):
        self.ui.statusBar.showMessage(u'Запрашивается следующая страница списка сотрудников...')
        self.reset_employee_list(self._c._sendrecv('GET', self._employeeListNextUrl))
        self.employee_list_update_buttons()
        self.ui.statusBar.showMessage(u'Данные успешно получены', 1000)

    def employee_list_get_prev_page(self):
        self.ui.statusBar.showMessage(u'Запрашивается предыдущая страница списка сотрудников...')
        self.reset_employee_list(self._c._sendrecv('GET', self._employeeListPrevUrl))
        self.employee_list_update_buttons()
        self.ui.statusBar.showMessage(u'Данные успешно получены', 1000)

    def employee_list_exist_changed(self, state):
        self.ui.statusBar.showMessage(u'Переключение режима отображения списка сотрудников...')
        self.employee_list_get_first_page(state is not 0)
        self.ui.statusBar.showMessage(u'Режим успешно переключен', 1000)

    def employee_list_cell_clicked(self, row, column):
        try:
            employee_id = self.ui.employeeListTable.verticalHeaderItem(row).text()
            employee_id_int = int(employee_id)
            self.get_employee_details(employee_id_int)
        except:
            self.ui.statusBar.showMessage(u'Ошибка при запросе информации о сотруднике #%s#' % employee_id, 1000)

    def get_employee_details(self, id):
        self.ui.statusBar.showMessage(u'Запрашивается информация о сотруднике %d...' % id)
        succeed, self._currentEmployee = self._c.get_employee(id)
        if succeed:
            self.employee_details_update()
            self.employee_operations_update()
            self.employee_equipment_update()
            self.employee_tasks_update()
            self.tasks_equipment_attach_update()
            self.ui.statusBar.showMessage(u'Данные о сотруднике #%d успешно получены' % id, 1000)
        else:
            self.ui.statusBar.showMessage(u'Неудача при получении данных о сотруднике #%d' % id, 1000)

    def employee_details_update(self):
        gData = self._currentEmployee['object']['general']
        self.ui.employeeTab.setCurrentIndex(0)
        self.ui.employeeDetailsName .setText(gData['name'])
        self.ui.employeeDetailsSnils.setText(gData['snils'])
        self.ui.employeeDetailsLogin.setText(gData['login'])
        self.ui.employeeDetailsPhone.setText(gData['phone'])
        self.ui.employeeDetailsAddr .setText(gData['addr'])
        self.ui.employeeDetailsRole .setText(gData['role'])

    def employee_operations_update(self):
        t = self.ui.employeeOperationsTable
        t.clearContents()
        t.setRowCount(0)
        opData = self._currentEmployee['object']['operations']
        size = len(opData)
        t.setRowCount(size)
        for i in xrange(size):
            e = opData[i]
            t.setVerticalHeaderItem(i, QtGui.QTableWidgetItem('%d' % e['id']))
            t.setItem(i, 0, QtGui.QTableWidgetItem(e['type']))
            t.setItem(i, 1, QtGui.QTableWidgetItem(e['date']))
        t.resizeColumnsToContents()

    def employee_equipment_update(self):
        t = self.ui.equipmentListBox
        t.clear()
        eqData = self._currentEmployee['object']['owner_of']

        if self.ui.equipmentExistCheckbox.isChecked():
            eq_names = [u'%s : %s' % (x['equipment']['id'], x['equipment']['name']) for x in eqData if x['actual']]
        else:
            eq_names = [u'%s : %s' % (x['equipment']['id'], x['equipment']['name']) for x in eqData]
        t.addItems(eq_names)
        self.ui.taskEquipmentAttachBox.clear()
        self.ui.taskEquipmentAttachBox.addItems(eq_names)

    def equipment_exist_changed(self, state):
        self.ui.statusBar.showMessage(u'Переключение режима отображения списка оборудования...')
        self.employee_equipment_update()
        self.ui.statusBar.showMessage(u'Режим успешно переключен', 1000)

    def equipment_details_update(self, index):
        self.ui.equipmentAddr.clear()
        self.ui.equipmentName.clear()
        self.ui.equipmentSN.clear()
        self.ui.equipmentModel.clear()
        self.ui.equipmentDateBegin.clear()
        self.ui.equipmentDateEnd.clear()
        self.ui.equipmentActual.clear()

        if index >= 0:
            if self.ui.equipmentExistCheckbox.isChecked():
                eqData = [x for x in self._currentEmployee['object']['owner_of'] if x['actual']][index]
            else:
                eqData = self._currentEmployee['object']['owner_of'][index]
            self.ui.equipmentAddr.setText(eqData['equipment']['addr'])
            self.ui.equipmentName.setText(eqData['equipment']['name'])
            self.ui.equipmentSN.setText(eqData['equipment']['serial_number'])
            self.ui.equipmentModel.setText(eqData['equipment']['model'])
            self.ui.equipmentDateBegin.setText(eqData['date_begin'])
            self.ui.equipmentDateEnd.setText(eqData['date_end'])
            self.ui.equipmentActual.setText(u'Правда' if eqData['actual'] else u'Неправда')

    def employee_tasks_update(self):
        t = self.ui.tasksListBox
        t.clear()
        tData = self._currentEmployee['object']['tasks']

        t_names = [u'%d : %s' % (x['id'], x['datetime']) for x in tData]
        t.addItems(t_names)

    def tasks_details_update(self, index):
        self.ui.taskDate.clear()
        self.ui.taskOwner.clear()
        self.ui.taskDescription.clear()
        self.ui.taskEquipmentBox.clear()

        if index >= 0:
            tData = self._currentEmployee['object']['tasks'][index]
            self.ui.taskDate.setText(tData['datetime'])
            if tData['owner']:
                self.ui.taskOwner.setText(tData['owner']['name'])
            self.ui.taskDescription.setPlainText(tData['name'])
            self.list_of_task_equipment_update(tData['id'])

        t = datetime.now().isoformat()
        self.ui.newTaskTime.setText(datetime.now().isoformat())
        self.ui.newTaskDescription.setPlainText('test:%s' % t)

    def list_of_task_equipment_update(self, task_id):
        self.ui.taskEquipmentBox.clear()
        self.ui.statusBar.showMessage(u'Запрашивается список оборудовани для задания%d...' % task_id)
        succeed, self._current_list_of_task_equipment = self._c.get_equipment_for_task(task_id)
        if succeed:
            c = self._current_list_of_task_equipment
            self.ui.taskEquipmentBox.addItems(['%d : %s' % (x['id'], x['name']) for x in c])
            self.ui.statusBar.showMessage(u'Список оборудования успешно принят')
        else:
            self.ui.statusBar.showMessage(u'Ошибка получения списка оборудования')

    def tasks_equipment_details_update(self, index):
        self.ui.taskEquipmentID.clear()
        self.ui.taskEquipmentAddr.clear()
        self.ui.taskEquipmentName.clear()
        self.ui.taskEquipmentSerial.clear()
        self.ui.taskEquipmentDetachButton.setDisabled(True)

        if index >= 0:
            self.ui.taskEquipmentDetachButton.setEnabled(True)
            tData = self._current_list_of_task_equipment[index]
            self.ui.taskEquipmentID.setText(u'%s' % tData['id'])
            self.ui.taskEquipmentAddr.setText(tData['addr'])
            self.ui.taskEquipmentName.setText(tData['name'])
            self.ui.taskEquipmentSerial.setText(tData['serial_number'])

    def attach_equipment_to_task(self):
        eqs = self.ui.taskEquipmentAttachBox
        tsk = self.ui.tasksListBox

        t_index = tsk.currentIndex()
        if t_index < 0:
            return
        ts_id = self._currentEmployee['object']['tasks'][t_index]['id']

        eq_index = eqs.currentIndex()
        if eq_index < 0:
            return
        eq_id = self._currentEmployee['object']['owner_of'][eq_index]['equipment']['id']

        self.ui.statusBar.showMessage(u'Прикрепляется оборудование %d к заданию %d...' % (eq_id, ts_id))
        succeed, data = self._c.add_equipment_to_task(ts_id, eq_id)
        if succeed:
            self.ui.statusBar.showMessage(u'Успешно прикреплено оборудование %d к заданию %d' % (eq_id, ts_id), 1000)
        else:
            self.ui.statusBar.showMessage(u'Неудача при прикреплении оборудования %d к заданию %d' % (eq_id, ts_id), 1000)

        self.tasks_details_update(t_index)

    def detach_equipment_from_task(self):
        eqs = self.ui.taskEquipmentBox
        tsk = self.ui.tasksListBox

        t_index = tsk.currentIndex()
        if t_index < 0:
            return
        ts_id = self._currentEmployee['object']['tasks'][t_index]['id']

        eq_id = int(self.ui.taskEquipmentID.text())

        self.ui.statusBar.showMessage(u'Открепляется оборудование %d от задания %d...' % (eq_id, ts_id))
        succeed, data = self._c.remove_equipment_from_task(ts_id, eq_id)
        if succeed:
            self.ui.statusBar.showMessage(u'Успешно откреплено оборудование %d от задания %d' % (eq_id, ts_id), 1000)
        else:
            self.ui.statusBar.showMessage(u'Неудача при откреплении оборудования %d от задания %d' % (eq_id, ts_id), 1000)

        self.tasks_details_update(t_index)

    def tasks_equipment_attach_update(self):
        self.ui.taskEquipmentAttachButton.setDisabled(True)
        if self.ui.taskEquipmentAttachBox.currentIndex() >= 0 and \
           self.ui.tasksListBox.currentIndex() >= 0:
            self.ui.taskEquipmentAttachButton.setEnabled(True)

    def publish_new_task(self):
        client_id = self._currentEmployee['object']['general']['id']
        name = self.ui.newTaskDescription.toPlainText()
        time = self.ui.newTaskTime.text()
        self._c.add_task(client_id, name, time)
        self.get_employee_details(client_id)

    def export_to_excel(self):
        w = ExcelSaver()
        self.ui.statusBar.showMessage(u'Загружается список всех сотрудников...')
        filename = 'report.xls'
        succeed, employees = self._c.get_employee_list(1000)
        if succeed:
            w.makeEmployeeList(employees)
            w.save(filename)
            self.ui.statusBar.showMessage(u'Информация была успешно сохранена в файле %s' % filename, 2000)
        else:
            self.ui.statusBar.showMessage(u'Не удалось сохранить информацию', 2000)





def uimain():
    app = QtGui.QApplication(sys.argv)
    myapp = MyMainWindow()
    myapp.show()
    myapp.afterRun()
    sys.exit(app.exec_())







def main():
    c = Connection('amihailov.pro', '/rtsup/api')
    succeed, employees = c.get_employee_list()
    if succeed:
        w = ExcelSaver()
        w.makeEmployeeList(employees)
        w.save('test.xls')





if __name__ == '__main__':
    uimain()
