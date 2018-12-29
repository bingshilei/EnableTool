# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\开发启蒙\可用工具开发\EnableTools\CalcLog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CalcLog(object):
    def setupUi(self, CalcLog):
        CalcLog.setObjectName("CalcLog")
        CalcLog.resize(1284, 549)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/En/En.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CalcLog.setWindowIcon(icon)
        CalcLog.setStyleSheet("QPushButton{\n"
"        border-radius: 4px;\n"
"        border: none;\n"
"        width: 75px;\n"
"        height: 25px;\n"
"}\n"
"QPushButton:enabled {\n"
"        background: rgb(120, 170, 220);\n"
"        color: white;\n"
"}\n"
"\n"
"QPushButton:enabled:hover{\n"
"        background: red;\n"
"}\n"
"QPushButton:enabled:pressed{\n"
"        background: rgb(0, 78, 161);\n"
"}\n"
"/*表格QSS样式开始*/\n"
"QTableView {\n"
"    font: 10pt;\n"
"    color:#000000;\n"
"    border: 1px solid #76797C;\n"
"    gridline-color: #31363b;\n"
"    background-color: #ffffff;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: skyblue;\n"
"    color:rgb(102,102,102);\n"
"     border: 1px solid #76797C;\n"
"    padding: 5px; \n"
"    font-size:14px  \n"
"}\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one {\n"
"    border-top: 1px solid #76797C;\n"
"}\n"
"QHeaderView::section::vertical {\n"
"    border-top: transparent;\n"
"}\n"
"QTableCornerButton::section {\n"
"    background-color: #f3f3f3;\n"
"}\n"
"/*表格样式结束*/\n"
"/*QComBox样式开始*/\n"
"QComboBox {  \n"
"    height: 25px;\n"
"    border: 1px solid rgb(111, 156, 207);\n"
"    background: white;\n"
"}\n"
"/*QComBox样式结束*/\n"
"/*QSpinBox样式开始*/\n"
"QSpinBox,QDoubleSpinBox{\n"
"        height: 24px;\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: white;\n"
"}\n"
"\n"
"QSpinBox:enabled:hover, QSpinBox:enabled:focus {\n"
"        color: rgb(51, 51, 51);\n"
"}\n"
"/*QSpinBox样式结束*/\n"
"\n"
"/*20180814增加样式*/\n"
"QHeaderView::section::first{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"/*修复下拉框的项显示不全*/\n"
"QComboBox:enabled {\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QSpinBox::up-button ,QSpinBox::down-button{\n"
"\n"
"width: 20px; \n"
"}\n"
"/*QDoubleSpinBox显示右边图标，且控制大小*/\n"
"QDoubleSpinBox::up-button ,QDoubleSpinBox::down-button{\n"
"\n"
"width: 20px; \n"
"}\n"
"")
        CalcLog.setTabShape(QtWidgets.QTabWidget.Triangular)
        CalcLog.setDockNestingEnabled(False)
        CalcLog.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtWidgets.QWidget(CalcLog)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        CalcLog.setCentralWidget(self.centralWidget)

        self.retranslateUi(CalcLog)
        QtCore.QMetaObject.connectSlotsByName(CalcLog)

    def retranslateUi(self, CalcLog):
        _translate = QtCore.QCoreApplication.translate
        CalcLog.setWindowTitle(_translate("CalcLog", "计算日志"))
        self.textEdit.setHtml(_translate("CalcLog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">此处显示系统运算过程的日志输出：</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))

import ICON_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CalcLog = QtWidgets.QMainWindow()
    ui = Ui_CalcLog()
    ui.setupUi(CalcLog)
    CalcLog.show()
    sys.exit(app.exec_())

