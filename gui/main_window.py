# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Sat Dec 22 02:52:22 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1151, 809)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.employeeListTab = QtGui.QGroupBox(self.centralWidget)
        self.employeeListTab.setObjectName("employeeListTab")
        self.gridLayout_2 = QtGui.QGridLayout(self.employeeListTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.employeeListBackButton = QtGui.QPushButton(self.employeeListTab)
        self.employeeListBackButton.setObjectName("employeeListBackButton")
        self.horizontalLayout_2.addWidget(self.employeeListBackButton)
        self.label = QtGui.QLabel(self.employeeListTab)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.employeeListPageIndicator = QtGui.QLabel(self.employeeListTab)
        self.employeeListPageIndicator.setObjectName("employeeListPageIndicator")
        self.horizontalLayout_2.addWidget(self.employeeListPageIndicator)
        self.employeeListForwardButton = QtGui.QPushButton(self.employeeListTab)
        self.employeeListForwardButton.setObjectName("employeeListForwardButton")
        self.horizontalLayout_2.addWidget(self.employeeListForwardButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.employeeListTable = QtGui.QTableWidget(self.employeeListTab)
        self.employeeListTable.setMidLineWidth(-15)
        self.employeeListTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.employeeListTable.setRowCount(2)
        self.employeeListTable.setColumnCount(2)
        self.employeeListTable.setObjectName("employeeListTable")
        self.employeeListTable.setColumnCount(2)
        self.employeeListTable.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.employeeListTable.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.employeeListTable.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.employeeListTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.employeeListTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.employeeListTable.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.employeeListTable.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.employeeListTable.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.employeeListTable.setItem(1, 1, item)
        self.verticalLayout.addWidget(self.employeeListTable)
        self.employeeListExistCheckbox = QtGui.QCheckBox(self.employeeListTab)
        self.employeeListExistCheckbox.setChecked(True)
        self.employeeListExistCheckbox.setObjectName("employeeListExistCheckbox")
        self.verticalLayout.addWidget(self.employeeListExistCheckbox)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.employeeListTab)
        self.employeeInfoTab = QtGui.QGroupBox(self.centralWidget)
        self.employeeInfoTab.setObjectName("employeeInfoTab")
        self.gridLayout_3 = QtGui.QGridLayout(self.employeeInfoTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.employeeTab = QtGui.QTabWidget(self.employeeInfoTab)
        self.employeeTab.setObjectName("employeeTab")
        self.employeeTabDetails = QtGui.QWidget()
        self.employeeTabDetails.setObjectName("employeeTabDetails")
        self.gridLayout_4 = QtGui.QGridLayout(self.employeeTabDetails)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtGui.QLabel(self.employeeTabDetails)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.employeeDetailsName = QtGui.QLineEdit(self.employeeTabDetails)
        self.employeeDetailsName.setObjectName("employeeDetailsName")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.employeeDetailsName)
        self.label_3 = QtGui.QLabel(self.employeeTabDetails)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.employeeTabDetails)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(self.employeeTabDetails)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(self.employeeTabDetails)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtGui.QLabel(self.employeeTabDetails)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_7)
        self.employeeDetailsSnils = QtGui.QLineEdit(self.employeeTabDetails)
        self.employeeDetailsSnils.setObjectName("employeeDetailsSnils")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.employeeDetailsSnils)
        self.employeeDetailsLogin = QtGui.QLineEdit(self.employeeTabDetails)
        self.employeeDetailsLogin.setObjectName("employeeDetailsLogin")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.employeeDetailsLogin)
        self.employeeDetailsPhone = QtGui.QLineEdit(self.employeeTabDetails)
        self.employeeDetailsPhone.setObjectName("employeeDetailsPhone")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.employeeDetailsPhone)
        self.employeeDetailsAddr = QtGui.QLineEdit(self.employeeTabDetails)
        self.employeeDetailsAddr.setObjectName("employeeDetailsAddr")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.employeeDetailsAddr)
        self.employeeDetailsRole = QtGui.QLineEdit(self.employeeTabDetails)
        self.employeeDetailsRole.setObjectName("employeeDetailsRole")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.employeeDetailsRole)
        self.gridLayout_4.addLayout(self.formLayout, 0, 0, 1, 1)
        self.employeeTab.addTab(self.employeeTabDetails, "")
        self.employeeTabOperations = QtGui.QWidget()
        self.employeeTabOperations.setObjectName("employeeTabOperations")
        self.gridLayout_5 = QtGui.QGridLayout(self.employeeTabOperations)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.employeeOperationsTable = QtGui.QTableWidget(self.employeeTabOperations)
        self.employeeOperationsTable.setObjectName("employeeOperationsTable")
        self.employeeOperationsTable.setColumnCount(2)
        self.employeeOperationsTable.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.employeeOperationsTable.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.employeeOperationsTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.employeeOperationsTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.employeeOperationsTable.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.employeeOperationsTable.setItem(0, 1, item)
        self.gridLayout_5.addWidget(self.employeeOperationsTable, 0, 1, 1, 1)
        self.employeeTab.addTab(self.employeeTabOperations, "")
        self.employeeTabEquipment = QtGui.QWidget()
        self.employeeTabEquipment.setObjectName("employeeTabEquipment")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.employeeTabEquipment)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.equipmentListBox = QtGui.QComboBox(self.employeeTabEquipment)
        self.equipmentListBox.setObjectName("equipmentListBox")
        self.verticalLayout_4.addWidget(self.equipmentListBox)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtGui.QLabel(self.employeeTabEquipment)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)
        self.equipmentAddr = QtGui.QLineEdit(self.employeeTabEquipment)
        self.equipmentAddr.setObjectName("equipmentAddr")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.equipmentAddr)
        self.equipmentName = QtGui.QLineEdit(self.employeeTabEquipment)
        self.equipmentName.setObjectName("equipmentName")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.equipmentName)
        self.equipmentSN = QtGui.QLineEdit(self.employeeTabEquipment)
        self.equipmentSN.setObjectName("equipmentSN")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.equipmentSN)
        self.equipmentModel = QtGui.QLineEdit(self.employeeTabEquipment)
        self.equipmentModel.setObjectName("equipmentModel")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.equipmentModel)
        self.equipmentDateBegin = QtGui.QLineEdit(self.employeeTabEquipment)
        self.equipmentDateBegin.setObjectName("equipmentDateBegin")
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.equipmentDateBegin)
        self.equipmentDateEnd = QtGui.QLineEdit(self.employeeTabEquipment)
        self.equipmentDateEnd.setObjectName("equipmentDateEnd")
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.equipmentDateEnd)
        self.equipmentActual = QtGui.QLineEdit(self.employeeTabEquipment)
        self.equipmentActual.setObjectName("equipmentActual")
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.equipmentActual)
        self.label_9 = QtGui.QLabel(self.employeeTabEquipment)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtGui.QLabel(self.employeeTabEquipment)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtGui.QLabel(self.employeeTabEquipment)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtGui.QLabel(self.employeeTabEquipment)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_12)
        self.label_13 = QtGui.QLabel(self.employeeTabEquipment)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_13)
        self.label_14 = QtGui.QLabel(self.employeeTabEquipment)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_14)
        self.verticalLayout_4.addLayout(self.formLayout_2)
        self.equipmentExistCheckbox = QtGui.QCheckBox(self.employeeTabEquipment)
        self.equipmentExistCheckbox.setObjectName("equipmentExistCheckbox")
        self.verticalLayout_4.addWidget(self.equipmentExistCheckbox)
        self.employeeTab.addTab(self.employeeTabEquipment, "")
        self.employeeTabTasks = QtGui.QWidget()
        self.employeeTabTasks.setObjectName("employeeTabTasks")
        self.gridLayout_8 = QtGui.QGridLayout(self.employeeTabTasks)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tasksListBox = QtGui.QComboBox(self.employeeTabTasks)
        self.tasksListBox.setObjectName("tasksListBox")
        self.gridLayout_8.addWidget(self.tasksListBox, 0, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(self.employeeTabTasks)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 512, 645))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_9 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_15 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName("label_15")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_15)
        self.taskDate = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.taskDate.setObjectName("taskDate")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.taskDate)
        self.label_16 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName("label_16")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_16)
        self.taskOwner = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.taskOwner.setObjectName("taskOwner")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.taskOwner)
        self.label_17 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName("label_17")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_17)
        self.taskDescription = QtGui.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.taskDescription.setObjectName("taskDescription")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.taskDescription)
        self.gridLayout_9.addLayout(self.formLayout_3, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.taskEquipmentDetachButton = QtGui.QPushButton(self.groupBox)
        self.taskEquipmentDetachButton.setEnabled(False)
        self.taskEquipmentDetachButton.setBaseSize(QtCore.QSize(30, 0))
        self.taskEquipmentDetachButton.setObjectName("taskEquipmentDetachButton")
        self.horizontalLayout_3.addWidget(self.taskEquipmentDetachButton)
        self.taskEquipmentBox = QtGui.QComboBox(self.groupBox)
        self.taskEquipmentBox.setObjectName("taskEquipmentBox")
        self.horizontalLayout_3.addWidget(self.taskEquipmentBox)
        self.gridLayout_7.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName("formLayout_4")
        self.taskEquipmentID = QtGui.QLineEdit(self.groupBox)
        self.taskEquipmentID.setObjectName("taskEquipmentID")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.taskEquipmentID)
        self.label_18 = QtGui.QLabel(self.groupBox)
        self.label_18.setObjectName("label_18")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_18)
        self.label_19 = QtGui.QLabel(self.groupBox)
        self.label_19.setObjectName("label_19")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_19)
        self.label_20 = QtGui.QLabel(self.groupBox)
        self.label_20.setObjectName("label_20")
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_20)
        self.taskEquipmentName = QtGui.QLineEdit(self.groupBox)
        self.taskEquipmentName.setObjectName("taskEquipmentName")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.taskEquipmentName)
        self.taskEquipmentAddr = QtGui.QLineEdit(self.groupBox)
        self.taskEquipmentAddr.setObjectName("taskEquipmentAddr")
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.FieldRole, self.taskEquipmentAddr)
        self.label_21 = QtGui.QLabel(self.groupBox)
        self.label_21.setObjectName("label_21")
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_21)
        self.taskEquipmentSerial = QtGui.QLineEdit(self.groupBox)
        self.taskEquipmentSerial.setObjectName("taskEquipmentSerial")
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.taskEquipmentSerial)
        self.gridLayout_7.addLayout(self.formLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.taskEquipmentAttachButton = QtGui.QPushButton(self.groupBox)
        self.taskEquipmentAttachButton.setEnabled(False)
        self.taskEquipmentAttachButton.setBaseSize(QtCore.QSize(30, 0))
        self.taskEquipmentAttachButton.setObjectName("taskEquipmentAttachButton")
        self.horizontalLayout_4.addWidget(self.taskEquipmentAttachButton)
        self.taskEquipmentAttachBox = QtGui.QComboBox(self.groupBox)
        self.taskEquipmentAttachBox.setObjectName("taskEquipmentAttachBox")
        self.horizontalLayout_4.addWidget(self.taskEquipmentAttachBox)
        self.gridLayout_7.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.formLayout_5 = QtGui.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_22 = QtGui.QLabel(self.groupBox_2)
        self.label_22.setObjectName("label_22")
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_22)
        self.newTaskTime = QtGui.QLineEdit(self.groupBox_2)
        self.newTaskTime.setObjectName("newTaskTime")
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.newTaskTime)
        self.label_23 = QtGui.QLabel(self.groupBox_2)
        self.label_23.setObjectName("label_23")
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_23)
        self.newTaskDescription = QtGui.QPlainTextEdit(self.groupBox_2)
        self.newTaskDescription.setObjectName("newTaskDescription")
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.FieldRole, self.newTaskDescription)
        self.newTaskButton = QtGui.QPushButton(self.groupBox_2)
        self.newTaskButton.setObjectName("newTaskButton")
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.SpanningRole, self.newTaskButton)
        self.gridLayout_6.addLayout(self.formLayout_5, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_8.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.employeeTab.addTab(self.employeeTabTasks, "")
        self.gridLayout_3.addWidget(self.employeeTab, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.employeeInfoTab)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.employeeTab.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.employeeListTable, self.employeeListBackButton)
        MainWindow.setTabOrder(self.employeeListBackButton, self.employeeDetailsLogin)
        MainWindow.setTabOrder(self.employeeDetailsLogin, self.employeeTab)
        MainWindow.setTabOrder(self.employeeTab, self.employeeDetailsName)
        MainWindow.setTabOrder(self.employeeDetailsName, self.employeeDetailsPhone)
        MainWindow.setTabOrder(self.employeeDetailsPhone, self.employeeDetailsAddr)
        MainWindow.setTabOrder(self.employeeDetailsAddr, self.employeeDetailsRole)
        MainWindow.setTabOrder(self.employeeDetailsRole, self.employeeDetailsSnils)
        MainWindow.setTabOrder(self.employeeDetailsSnils, self.employeeListForwardButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Лабораторная работа №3", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeListTab.setTitle(QtGui.QApplication.translate("MainWindow", "Список сотрудников", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeListBackButton.setText(QtGui.QApplication.translate("MainWindow", "Назад", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Отображается страница: ", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeListPageIndicator.setText(QtGui.QApplication.translate("MainWindow", "## из ##", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeListForwardButton.setText(QtGui.QApplication.translate("MainWindow", "Вперёд", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeListTable.verticalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Возможно", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeListTable.verticalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "С", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeListTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "СНИЛС", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeListTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "ФИО", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.employeeListTable.isSortingEnabled()
        self.employeeListTable.setSortingEnabled(False)
        self.employeeListTable.item(0, 0).setText(QtGui.QApplication.translate("MainWindow", "возникли", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeListTable.item(0, 1).setText(QtGui.QApplication.translate("MainWindow", "проблемы", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeListTable.item(1, 0).setText(QtGui.QApplication.translate("MainWindow", "установлением", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeListTable.item(1, 1).setText(QtGui.QApplication.translate("MainWindow", "соединения", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeListTable.setSortingEnabled(__sortingEnabled)
        self.employeeListExistCheckbox.setText(QtGui.QApplication.translate("MainWindow", "Отображать только работающих сейчас", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeInfoTab.setTitle(QtGui.QApplication.translate("MainWindow", "Информация о сотруднике", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Полное имя", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "СНИЛС", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Логин", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Телефон", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Адрес", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Должность", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeTab.setTabText(self.employeeTab.indexOf(self.employeeTabDetails), QtGui.QApplication.translate("MainWindow", "Анкета", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeOperationsTable.verticalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Сначала", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeOperationsTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Тип операции", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeOperationsTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Дата", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.employeeOperationsTable.isSortingEnabled()
        self.employeeOperationsTable.setSortingEnabled(False)
        self.employeeOperationsTable.item(0, 0).setText(QtGui.QApplication.translate("MainWindow", "Выберите", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeOperationsTable.item(0, 1).setText(QtGui.QApplication.translate("MainWindow", "сотрудника", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeOperationsTable.setSortingEnabled(__sortingEnabled)
        self.employeeTab.setTabText(self.employeeTab.indexOf(self.employeeTabOperations), QtGui.QApplication.translate("MainWindow", "Список операций", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Адрес", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Наименование", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Серийный номер", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Модель", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Владение по", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "Владение с", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "Владение сейчас", None, QtGui.QApplication.UnicodeUTF8))
        self.equipmentExistCheckbox.setText(QtGui.QApplication.translate("MainWindow", "Отображать только активное сейчас", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeTab.setTabText(self.employeeTab.indexOf(self.employeeTabEquipment), QtGui.QApplication.translate("MainWindow", "Оборудование", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "Дата открытия", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "Ответственный", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("MainWindow", "Описание задачи", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Работа с оборудованием", None, QtGui.QApplication.UnicodeUTF8))
        self.taskEquipmentDetachButton.setText(QtGui.QApplication.translate("MainWindow", "Открепить от задачи", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainWindow", "ID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("MainWindow", "Название", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("MainWindow", "Адрес", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainWindow", "Серийный номер", None, QtGui.QApplication.UnicodeUTF8))
        self.taskEquipmentAttachButton.setText(QtGui.QApplication.translate("MainWindow", "Прикрепить к задаче", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Новая задача", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("MainWindow", "Время", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("MainWindow", "Описание", None, QtGui.QApplication.UnicodeUTF8))
        self.newTaskButton.setText(QtGui.QApplication.translate("MainWindow", "Разместить", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeTab.setTabText(self.employeeTab.indexOf(self.employeeTabTasks), QtGui.QApplication.translate("MainWindow", "Задачи", None, QtGui.QApplication.UnicodeUTF8))

