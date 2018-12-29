# -*- coding: utf-8 -*-

"""
Created on 2018年12月26日
@author: Yiluo
@file: menu
@description:主窗体
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QStyleFactory
from Ui_menu import Ui_MainWindow
from CallEnableTest import CallEnableTool
from CallShareTrade import CallShareTrade
from CallBondPledge import CallBondPledge
from CallBondHG import CallBondHG
from CallUiAbout import CallUiAbout
import os
from CallCalcLog import CallCalcLog
from Callgongshi import Callgongshi
from Log import readData
from PyQt5 import  QtGui


class MainWindowUi(QMainWindow, Ui_MainWindow):
    
    
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindowUi, self).__init__(parent)
        self.setupUi(self)
       
        
    @pyqtSlot()
    def on_MShareTrade_triggered(self):
        """
        Slot documentation goes here.
        股票买卖菜单
        """
        self.demo = CallShareTrade()
         #计算页面显示数
        self.countTab= self.tabWidget.count()
        print('总页数：%d'%self.countTab)
        print('当前索引：%d'%self.tabWidget.currentIndex())
        self.index = self.tabWidget.indexOf(self.demo)
        print('是否存在：%d'%self.index)
        
        if  self.index== -1 and self.countTab != 1:
            self.tabWidget.setCurrentIndex(self.index)
        else:
            if self.countTab == 1:
                #插入窗体显示
                self.tabWidget.insertTab(self.countTab, self.demo,  '股票买卖')
            else:
                self.countTab = self.countTab +1
                self.tabWidget.insertTab(self.countTab, self.demo,  '股票买卖')
                #设置窗体成为当前窗体
            self.tabWidget.setCurrentWidget(self.demo)
            
            self.tabWidget.show()
            self.index = self.tabWidget.indexOf(self.demo)
            print('是否存在2：%d'%self.index)
        
        
    @pyqtSlot()
    def on_action1_2_triggered(self):
        '''债券交易菜单'''
        self.demo = CallEnableTool()
         #计算页面显示数
        self.countTab= self.tabWidget.count()
        if self.countTab == 1:
            self.tabWidget.insertTab(self.countTab, self.demo, '债券交易')
        
        else:
            self.countTab = self.countTab +1
            self.tabWidget.insertTab(self.countTab, self.demo, '债券交易')
        #设置窗体成为当前窗体
        self.tabWidget.setCurrentWidget(self.demo)
        self.tabWidget.show()
        
    @pyqtSlot()
    def on_action2_2_triggered(self):
        """
        Slot documentation goes here.
        债券质押菜单
        """
        self.demo = CallBondPledge()
        self.countTab= self.tabWidget.count()
        if self.countTab == 1:
            self.tabWidget.insertTab(1, self.demo, '债券质押')
        else:
            self.tabWidget.insertTab(self.countTab, self.demo, '债券质押')
        self.tabWidget.setCurrentWidget(self.demo)
        self.tabWidget.show()
#        #日志记录
#        # 创建一个logger
#        logger = logging.getLogger('mylogger')
#        #设置日志级别
#        logger.setLevel(logging.DEBUG)
#        # 创建一个文件handler，用于写入日志文件
#        fh = logging.FileHandler('coder.log')
#        fh.setLevel(logging.DEBUG)
#        # 定义handler的输出格式
#        formatter = logging.Formatter('%(asctime)s:%(message)s')
#        
#        fh.setFormatter(formatter)
#        # 给logger添加handler
#        logger.addHandler(fh)
#        logger.info('当前打开的菜单是债券质押')
       
    @pyqtSlot()
    def on_actionaa_triggered(self):
        """
        Slot documentation goes here.
        债券回购菜单
        """
        # TODO: not implemented yet
        self.demo = CallBondHG()
        self.countTab = self.tabWidget.count()
        if self.countTab == 1:
            self.tabWidget.insertTab(1, self.demo, '债券回购')
        else:
            self.tabWidget.insertTab(self.countTab,self.demo, '债券回购')
        self.tabWidget.setCurrentWidget(self.demo)
        self.tabWidget.show()
        
    @pyqtSlot()
    def on_calcLog_triggered(self):
        """
        计算日志信息显示.
        """
        # TODO: not implemented yet
        self.demo = CallCalcLog()
        self.countTab = self.tabWidget.count()
        if self.countTab == 1:
            self.tabWidget.insertTab(1, self.demo, '计算日志')
        else:
            self.tabWidget.insertTab(self.countTab,self.demo, '计算日志')
        self.tabWidget.setCurrentWidget(self.demo)
        #获取当前路径
        abspath = os.path.dirname(os.path.abspath(__file__))
        #将当前路径和log文件夹进行拼接
        directory = os.path.join(abspath, 'log')
        #将文件夹和文件名进行拼接
        filename = os.path.join(directory, 'coder.log')
        f=open(filename,'r') #默认打开模式就为r
        data = f.readlines()
        
        for res in data:
            #print(res)
            # 获取文本框中文本的游标
            cursor = self.demo.textEdit.textCursor()
            # 将游标位置移动到当前文本的结束处
            cursor.movePosition(QtGui.QTextCursor.End)
            # 写入文本
            cursor.insertText(res)
            # 设置文本的游标为创建了cursor
            self.demo.textEdit.setTextCursor(cursor)
            #文字滚动显示
            self.demo.textEdit.ensureCursorVisible()
    
    @pyqtSlot()
    def on_actionAbout_triggered(self):
        """
        系统介绍
        """
        # TODO: not implemented yet
        self.uiAbout = CallUiAbout()
        self.uiAbout.show()
    
    @pyqtSlot()
    def on_gongshi_triggered(self):
        """
        公式显示.
        """
        # TODO: not implemented yet
        self.demo = Callgongshi()
        self.countTab = self.tabWidget.count()
        if self.countTab == 1:
            self.tabWidget.insertTab(1, self.demo, '公式显示')
        else:
            self.tabWidget.insertTab(self.countTab,self.demo, '公式显示')
        self.tabWidget.setCurrentWidget(self.demo)
        self.tabWidget.show()

        
    @pyqtSlot(int)
    def on_tabWidget_tabBarDoubleClicked(self, index):
        """
        双击tab页，关闭页面.
        
        @param index DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
        self.tabWidget.removeTab(index)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    app.setStyleSheet(readData('Default.qss'))
    app.setStyle(QStyleFactory.create("Fusion"))
    ui = MainWindowUi()
    ui.show()
    sys.exit(app.exec_())
    
