# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import MySQLdb




try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.conn = MySQLdb.connect(
            host='localhost',
            user='root',
            passwd='zdki',
            db='wenzhou',
            #
            charset='utf8',
        )
        self.cur = self.conn.cursor()
        self.sqlstring = "select * from tourist2 where "

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(877, 716)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 450, 831, 181))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.Tab = QtGui.QTabWidget(self.centralwidget)
        self.Tab.setGeometry(QtCore.QRect(20, 30, 521, 341))
        self.Tab.setObjectName(_fromUtf8("Tab"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(20, 80, 54, 12))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(20, 110, 54, 12))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(20, 140, 54, 12))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(20, 170, 54, 12))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(20, 200, 54, 12))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(20, 230, 54, 12))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(20, 260, 54, 12))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(20, 290, 54, 12))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(230, 20, 54, 12))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.graphicsView = QtGui.QGraphicsView(self.tab)
        self.graphicsView.setGeometry(QtCore.QRect(235, 81, 251, 221))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.textBrowser = QtGui.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(90, 20, 101, 21))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.tab)
        self.textBrowser_2.setGeometry(QtCore.QRect(90, 50, 101, 21))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.textBrowser_3 = QtGui.QTextBrowser(self.tab)
        self.textBrowser_3.setGeometry(QtCore.QRect(90, 80, 101, 21))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.textBrowser_4 = QtGui.QTextBrowser(self.tab)
        self.textBrowser_4.setGeometry(QtCore.QRect(90, 110, 101, 21))
        self.textBrowser_4.setObjectName(_fromUtf8("textBrowser_4"))
        self.textBrowser_5 = QtGui.QTextBrowser(self.tab)
        self.textBrowser_5.setGeometry(QtCore.QRect(90, 140, 101, 21))
        self.textBrowser_5.setObjectName(_fromUtf8("textBrowser_5"))
        self.textBrowser_6 = QtGui.QTextBrowser(self.tab)
        self.textBrowser_6.setGeometry(QtCore.QRect(90, 170, 101, 21))
        self.textBrowser_6.setObjectName(_fromUtf8("textBrowser_6"))
        self.textBrowser_7 = QtGui.QTextBrowser(self.tab)
        self.textBrowser_7.setGeometry(QtCore.QRect(90, 200, 101, 21))
        self.textBrowser_7.setObjectName(_fromUtf8("textBrowser_7"))
        self.textBrowser_8 = QtGui.QTextBrowser(self.tab)
        self.textBrowser_8.setGeometry(QtCore.QRect(90, 230, 101, 21))
        self.textBrowser_8.setObjectName(_fromUtf8("textBrowser_8"))
        self.textBrowser_9 = QtGui.QTextBrowser(self.tab)
        self.textBrowser_9.setGeometry(QtCore.QRect(90, 260, 101, 21))
        self.textBrowser_9.setObjectName(_fromUtf8("textBrowser_9"))
        self.textBrowser_10 = QtGui.QTextBrowser(self.tab)
        self.textBrowser_10.setGeometry(QtCore.QRect(90, 290, 101, 21))
        self.textBrowser_10.setObjectName(_fromUtf8("textBrowser_10"))
        self.textBrowser_11 = QtGui.QTextBrowser(self.tab)
        self.textBrowser_11.setGeometry(QtCore.QRect(290, 20, 101, 21))
        self.textBrowser_11.setObjectName(_fromUtf8("textBrowser_11"))
        self.Tab.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.checkBox = QtGui.QCheckBox(self.tab_2)
        self.checkBox.setGeometry(QtCore.QRect(20, 20, 47, 16))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.lineEdit = QtGui.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 112, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.checkBox_2 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 80, 61, 16))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 140, 61, 16))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_4 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_4.setGeometry(QtCore.QRect(260, 20, 61, 16))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_6 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_6.setGeometry(QtCore.QRect(260, 80, 61, 16))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 80, 112, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 140, 112, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_15 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_15.setGeometry(QtCore.QRect(350, 20, 112, 20))
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.lineEdit_16 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_16.setGeometry(QtCore.QRect(350, 80, 112, 20))
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.lineEdit_17 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_17.setGeometry(QtCore.QRect(350, 140, 112, 20))
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.checkBox_8 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_8.setGeometry(QtCore.QRect(260, 140, 61, 16))
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.Tab.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(570, 40, 291, 92))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.checkBox_5 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.gridLayout.addWidget(self.checkBox_5, 0, 0, 1, 1)
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.gridLayoutWidget)
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.gridLayout.addWidget(self.dateTimeEdit, 0, 2, 1, 1)
        self.dateTimeEdit_2 = QtGui.QDateTimeEdit(self.gridLayoutWidget)
        self.dateTimeEdit_2.setObjectName(_fromUtf8("dateTimeEdit_2"))
        self.gridLayout.addWidget(self.dateTimeEdit_2, 2, 2, 1, 1)
        self.checkBox_7 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.gridLayout.addWidget(self.checkBox_7, 3, 0, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_3, 3, 2, 1, 1)
        self.label_17 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout.addWidget(self.label_17, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(709, 390, 151, 51))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)
        self.gridLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(540, 390, 151, 51))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_16 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_3.addWidget(self.label_16, 0, 0, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.comboBox_2, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(570, 20, 54, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(570, 150, 91, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.tableWidget_2 = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(575, 170, 271, 211))
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(6)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(410, 390, 91, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 390, 91, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 390, 101, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 390, 101, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 877, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Tab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "编号", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "证件号", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "航班号", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "航班日期", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "座位号", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "登机口", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "序号", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "始发站", None))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "目的站", None))
        self.label_2.setText(_translate("MainWindow", "姓名", None))
        self.label_3.setText(_translate("MainWindow", "证件号", None))
        self.label_7.setText(_translate("MainWindow", "航班号", None))
        self.label_8.setText(_translate("MainWindow", "航班日期", None))
        self.label_9.setText(_translate("MainWindow", "座位号", None))
        self.label_10.setText(_translate("MainWindow", "登机口", None))
        self.label_11.setText(_translate("MainWindow", "序号", None))
        self.label_12.setText(_translate("MainWindow", "始发站", None))
        self.label_13.setText(_translate("MainWindow", "目的站", None))
        self.label_14.setText(_translate("MainWindow", "起飞时间", None))
        self.label_15.setText(_translate("MainWindow", "住址", None))
        self.Tab.setTabText(self.Tab.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.checkBox.setText(_translate("MainWindow", "姓名", None))
        self.checkBox_2.setText(_translate("MainWindow", "证件号", None))
        self.checkBox_3.setText(_translate("MainWindow", "航班号", None))
        self.checkBox_4.setText(_translate("MainWindow", "座位号", None))
        self.checkBox_6.setText(_translate("MainWindow", "登机口", None))
        self.checkBox_8.setText(_translate("MainWindow", "序号", None))
        self.Tab.setTabText(self.Tab.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.checkBox_5.setText(_translate("MainWindow", "时间段", None))
        self.checkBox_7.setText(_translate("MainWindow", "安检柜台", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "柜台1", None))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "柜台2", None))
        self.label_17.setText(_translate("MainWindow", "到", None))
        self.label_6.setText(_translate("MainWindow", "从", None))
        self.label.setText(_translate("MainWindow", "参数设置", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "1140*900", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "1280*1024", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "1280*960", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "1280*800", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "1280*768", None))
        self.comboBox.setItemText(5, _translate("MainWindow", "1280*720", None))
        self.comboBox.setItemText(6, _translate("MainWindow", "1152*864", None))
        self.comboBox.setItemText(7, _translate("MainWindow", "1152*864", None))
        self.comboBox.setItemText(8, _translate("MainWindow", "1024*768", None))
        self.comboBox.setItemText(9, _translate("MainWindow", "800*600", None))
        self.label_16.setText(_translate("MainWindow", "数据操作", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "迁出", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "编辑", None))
        self.label_4.setText(_translate("MainWindow", "查询条件", None))
        self.label_5.setText(_translate("MainWindow", "查询统计信息", None))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "总计乘客", None))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "女性", None))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "男性", None))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "布控人员", None))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "特殊人员", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "人数", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "备注", None))
        self.pushButton_5.setText(_translate("MainWindow", "退出", None))
        self.pushButton.setText(_translate("MainWindow", "查询", None))
        self.pushButton_3.setText(_translate("MainWindow", "下一个", None))
        self.pushButton_2.setText(_translate("MainWindow", "上一个", None))

    def buttonExit(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        self.close()

    def showTest1(self):
        name=u'张三'
        license=u'123456789'
        flightnumber=u'cz213A'
        flightdata = u'20181212'
        seat = u'12B'
        port = u'150'
        no = u'120'
        dep = u'上海(shx)'
        des = u'北京(bjx)'

        self.textBrowser.setText(name)
        self.textBrowser_2.setText(license)
        self.textBrowser_3.setText(flightnumber)
        self.textBrowser_4.setText(flightdata)
        self.textBrowser_5.setText(seat)
        self.textBrowser_6.setText(port)
        self.textBrowser_7.setText(no)
        self.textBrowser_8.setText(dep)
        self.textBrowser_9.setText(des)

        pixmap.load('6.jpg')
        self.scene = QGraphicsScene(self)
        item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)
        self.graphicsView.setScene(self.scene)


    def showTest2(self):
        name=u'李四'
        license=u'987654321'
        flightnumber=u'cz112A'
        flightdata = u'20180408'
        seat = u'13'
        port = u'210'
        no = u'105'
        dep = u'北京(bjx)'
        des = u'上海(shx)'

        self.textBrowser.setText(name)
        self.textBrowser_2.setText(license)
        self.textBrowser_3.setText(flightnumber)
        self.textBrowser_4.setText(flightdata)
        self.textBrowser_5.setText(seat)
        self.textBrowser_6.setText(port)
        self.textBrowser_7.setText(no)
        self.textBrowser_8.setText(dep)
        self.textBrowser_9.setText(des)

        pixmap.load('5.jpg')
        self.scene = QGraphicsScene(self)
        item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)
        self.graphicsView.setScene(self.scene)

    def keyPressEvent(self, e):  # 不懂这个函数用在哪里？
        # 重写控件centralwidget的键盘按下事件
        if e.key() == QtCore.Qt.Key_Escape:
            # 如果按下了ESC键则执行buttonExit函数
            self.buttonExit()

    def buttonTest(self):
            temp_sqlstring = self.sqlstring
            if  self.checkBox_2.isChecked():
                 temp_sqlstring += 'license=%s' % self.lineEdit_2.text()






            self.tableWidget.clearContents()  # 每一次查询时清除表格中信息





class MyWindow(QtGui.QMainWindow, Ui_MainWindow):  # PyQt生产的是一个叫做Ui_MainWindow的类，只需要放在一个框架下画出来即可；
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.connect(self.pushButton_5, QtCore.SIGNAL('clicked()'), self.buttonExit)
        self.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.buttonTest)
        self.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'), self.showTest1)
        self.connect(self.pushButton_3, QtCore.SIGNAL('clicked()'), self.showTest2)


class LoginDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setWindowTitle('login')
        self.user = QtGui.QLineEdit(self)
        self.user.move(10, 20)
        self.user.setText('')
        self.pwd = QtGui.QLineEdit(self)
        self.pwd.move(10, 60)
        self.pwd.setText('')
        self.pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.loginBtn = QtGui.QPushButton('Login', self)
        self.loginBtn.move(100, 90)
        self.loginBtn.clicked.connect(self.login)  # 绑定方法判断用户名和密码

    def login(self):
        if self.user.text() == 'admin' and self.pwd.text() == 'admin':
            # 如果用户名和密码正确，关闭对话框，accept()关闭后，如果增加一个取消按钮调用reject()
            self.accept()
        else:
            QtGui.QMessageBox.critical(self, 'Error', 'User name or password error')


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)  # 建立一个app，把框架放在这个app中执行
    app.aboutToQuit.connect(app.deleteLater)
    pixmap = QtGui.QPixmap()
    dialog = LoginDialog()
    if dialog.exec_():
        myshow = MyWindow()
        myshow.show()
        sys.exit(app.exec_())
      # 也可以写成app.exec_() sys.exit(0)，前者是循环整个界面，后者是退出app