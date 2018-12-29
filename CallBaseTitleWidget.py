#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年12月26日
@author: Yiluo
@file: CallBaseTitleWidget
@description:弹框显示公式
"""
import sys
from PyQt5.QtCore import pyqtSignal, QPoint, Qt
from PyQt5.QtWidgets import QWidget,  QApplication
from Log import readData
from Ui_BaseTitleWidget import Ui_BaseTitleWidget


__Author__ = """By: Yiluo
QQ: 786129166
Email: 786129166@qq.com"""
__Copyright__ = "Copyright (c) 2018 Yiluo"
__Version__ = "Version 1.0"


class BaseTitleWidget(QWidget, Ui_BaseTitleWidget):

    windowMoved = pyqtSignal(QPoint)
    windowClosed = pyqtSignal()

    def __init__(self,  icon ='' ,title='', *args, **kwargs):
        super(BaseTitleWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)
        #隐藏原窗体标题栏
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        # 关闭按钮传递关闭信号
        #self.buttonClose.clicked.connect(self.windowClosed.emit)
        #self.windowMoved.connect(lambda pos: self.move(self.x() + pos.x(), self.y() + pos.y()))
        self.setIcon(icon).setTitle(title)
        self.buttonClose.clicked.connect(self.close)
        
        #self.setStyleSheet(readData('Default.qss'))
        self.prePos = None

    def setTitle(self, title):
        """设置标题文字
        :param title: 标题
        """
        self.labelTitle.setText(title)
        return self
    def setIcon(self, icon):
        """设置标题文字
        :param title: 标题
        """
        self.labelIcon.setText(icon)
        return self

    def mousePressEvent(self, event):
        super(BaseTitleWidget, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.prePos = event.pos()

    def mouseReleaseEvent(self, event):
        super(BaseTitleWidget, self).mouseReleaseEvent(event)
        self.prePos = None

    def mouseMoveEvent(self, event):
        super(BaseTitleWidget, self).mouseMoveEvent(event)
        if not self.prePos:
            return
        pos = event.pos() - self.prePos
        self.windowMoved.emit(pos)
    
    def doMoveWindow(self, pos):
        if self.isMaximized() or self.isFullScreen():
            return
        # 移动窗口
        self.move(self.x() + pos.x(), self.y() + pos.y())
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(readData('Default.qss'))
    w = BaseTitleWidget('T+0可用金额', '当前金额-冻结金额+解冻金额+Min{T+1变化,0}')
    #本窗口测试使用
    w.windowMoved.connect(lambda pos: w.move(w.x() + pos.x(), w.y() + pos.y()))
   
    w.show()
    sys.exit(app.exec_())
