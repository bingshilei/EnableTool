# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\开发启蒙\可用工具开发\EnableTools\BaseTitleWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BaseTitleWidget(object):
    def setupUi(self, BaseTitleWidget):
        BaseTitleWidget.setObjectName("BaseTitleWidget")
        BaseTitleWidget.resize(379, 84)
        BaseTitleWidget.setMinimumSize(QtCore.QSize(0, 0))
        BaseTitleWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        BaseTitleWidget.setStyleSheet("")
        self.layoutWidget = QtWidgets.QWidget(BaseTitleWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 381, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelNotice = QtWidgets.QLabel(self.layoutWidget)
        self.labelNotice.setMinimumSize(QtCore.QSize(14, 0))
        self.labelNotice.setStyleSheet("")
        self.labelNotice.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNotice.setObjectName("labelNotice")
        self.horizontalLayout.addWidget(self.labelNotice)
        self.labelIcon = QtWidgets.QLabel(self.layoutWidget)
        self.labelIcon.setMinimumSize(QtCore.QSize(90, 0))
        self.labelIcon.setMaximumSize(QtCore.QSize(34, 16777215))
        self.labelIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.labelIcon.setObjectName("labelIcon")
        self.horizontalLayout.addWidget(self.labelIcon)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonClose = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonClose.setMinimumSize(QtCore.QSize(28, 28))
        self.buttonClose.setMaximumSize(QtCore.QSize(28, 28))
        self.buttonClose.setStyleSheet("")
        self.buttonClose.setObjectName("buttonClose")
        self.horizontalLayout.addWidget(self.buttonClose)
        self.layoutWidget1 = QtWidgets.QWidget(BaseTitleWidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 30, 448, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.labelTitle = QtWidgets.QLabel(self.layoutWidget1)
        self.labelTitle.setWordWrap(True)
        self.labelTitle.setObjectName("labelTitle")
        self.horizontalLayout_2.addWidget(self.labelTitle)

        self.retranslateUi(BaseTitleWidget)
        QtCore.QMetaObject.connectSlotsByName(BaseTitleWidget)

    def retranslateUi(self, BaseTitleWidget):
        _translate = QtCore.QCoreApplication.translate
        BaseTitleWidget.setWindowTitle(_translate("BaseTitleWidget", "BaseTitleWidget"))
        self.labelNotice.setText(_translate("BaseTitleWidget", "i"))
        self.labelIcon.setText(_translate("BaseTitleWidget", "T+0可用金额"))
        self.buttonClose.setText(_translate("BaseTitleWidget", "r"))
        self.labelTitle.setText(_translate("BaseTitleWidget", "当前金额-冻结金额+解冻金额+Min{T+1变化,0}"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BaseTitleWidget = QtWidgets.QWidget()
    ui = Ui_BaseTitleWidget()
    ui.setupUi(BaseTitleWidget)
    BaseTitleWidget.show()
    sys.exit(app.exec_())

