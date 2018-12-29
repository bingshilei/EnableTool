#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年12月26日
@author: Yiluo
@file: CallBondPledge
@description:质押回购计算
"""

from PyQt5.QtCore import pyqtSlot, QEvent, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QHeaderView, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QBrush, QColor
from Ui_BondPledge import Ui_EnableTool
from Log import Loggers

__Author__ = """
By: Yiluo 
QQ: 786129166
Email: 786129166@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Yiluo'
__Version__ = 1.0

class CallBondPledge(QMainWindow, Ui_EnableTool):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(CallBondPledge, self).__init__(parent)
        self.setupUi(self)
        self.log = Loggers(level='debug')
        self.initUI()
    def initUI(self):
        
        # 设置表格第一行第一列的字体颜色和背景颜色
        for i in range(3):
            self.tableWidgetCurrent.item(i ,0).setForeground(QBrush(QColor(102,102,102)))
            self.tableWidgetCurrent.item(i, 0).setBackground(QBrush(QColor(243, 243, 243)))
            
            self.tableWidgetStock.item(i ,0).setForeground(QBrush(QColor(102,102,102)))
            self.tableWidgetStock.item(i, 0).setBackground(QBrush(QColor(243, 243, 243)))
        

#        self.tableWidgetStock.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 获取初始持仓数据
        self.InitCurrentBond = []
        # 获取初始标准券数据
        self.InitStandardTicket = []
        for j in range(6, 14):
            demo = self.tableWidgetCurrent.item(0, j).text()
            self.InitCurrentBond.append(float(demo))
        for k in range(6, 13):
            demo = self.tableWidgetStock.item(0, k).text()
            self.InitStandardTicket.append(float(demo))
        # 获取计算后的持仓数据
        self.FirstCurrentBond = self.InitCurrentBond[:]
        
        # 获取计算后的标准券数据
        self.FirstStockList = self.InitStandardTicket[:]


    '''监控窗体最大化事件'''
    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if self.windowState() == Qt.WindowMaximized:
                #print('最大化')
                #列自适应
                self.tableWidgetCurrent.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                #表格列自适应内容
                self.tableWidgetCurrent.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
                self.tableWidgetCurrent.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeToContents)
                self.tableWidgetCurrent.horizontalHeader().setSectionResizeMode(13, QHeaderView.ResizeToContents)
                #行自适应
                self.tableWidgetCurrent.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
                
    @pyqtSlot()
    def on_btnClear_clicked(self):
        """
        Slot documentation goes here.
        定义清空函数
        """
        '''清空资金变化'''
        for i in range(1, 3):
            for j in range(1, 14):
                newItem = QTableWidgetItem('')
                self.tableWidgetCurrent.setItem(i, j, newItem)
        '''清空证券变化'''
        for i in range(1, 3):
            for j in range(1, 13):
                newItem = QTableWidgetItem('')
                self.tableWidgetStock.setItem(i, j, newItem)
        
        self.log.logger.info('开始清除数据，请稍等...')
        # 获取计算后的持仓数据
        self.FirstCurrentBond = self.InitCurrentBond[:]
        # 获取计算后的标准券数据
        self.FirstStockList = self.InitStandardTicket[:]
        self.log.logger.info('数据已重置，请开始操作')
    
    @pyqtSlot()
    def on_btnInit_clicked(self):
        """
        Slot documentation goes here.
        定义日初始化函数
        """
        # 获得业务品种
        en_stock_type = self.c_stock_type.currentText()
        newItem = QTableWidgetItem('%s' % en_stock_type)
        self.tableWidgetCurrent.setItem(2, 1, newItem)
        newItem = QTableWidgetItem('%s' % en_stock_type)
        self.tableWidgetStock.setItem(2, 1, newItem)
        # 获得委托方向
        en_entrust_direction = self.c_entrust_direction.currentText()
        newItem = QTableWidgetItem('%s' % en_entrust_direction)
        self.tableWidgetCurrent.setItem(2, 2, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_direction)
        self.tableWidgetStock.setItem(2, 2, newItem)
        # 获得委托状态
        en_entrust_status = self.c_entrust_status.currentText()
        newItem = QTableWidgetItem('%s' % en_entrust_status)
        self.tableWidgetCurrent.setItem(2, 5, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_status)
        self.tableWidgetStock.setItem(2, 5, newItem)
        # 获得委托数量
        en_entrust_amount = float(self.c_entrust_amount.text())
        newItem = QTableWidgetItem('%d' % en_entrust_amount)
        self.tableWidgetCurrent.setItem(2, 3, newItem)
        newItem = QTableWidgetItem('%d' % en_entrust_amount)
        self.tableWidgetStock.setItem(2, 3, newItem)
        # 获得质押比例
        en_entrust_ratio = float(self.c_entrust_price.text())
        newItem = QTableWidgetItem('%.2f' % en_entrust_ratio)
        self.tableWidgetCurrent.setItem(2, 4, newItem)
        newItem = QTableWidgetItem('%.2f' % en_entrust_ratio)
        self.tableWidgetStock.setItem(2, 4, newItem)
        if en_entrust_direction == '提交质押':
            '''提交质押日初始化持仓变化'''
            for i, j in (enumerate(self.FirstCurrentBond)):
                newItem = QTableWidgetItem('%d' % j)
                self.tableWidgetCurrent.setItem(2, i + 6, newItem)
            '''提交质押日初始化标准券持仓变化'''
            for i, j in (enumerate(self.FirstStockList)):
                # print(i,j)
                newItem = QTableWidgetItem('%d' % j)
                self.tableWidgetStock.setItem(2, i + 6, newItem)
        else:
            '''转回质押日初始化持仓变化'''
            for i, j in (enumerate(self.FirstCurrentBond)):
                newItem = QTableWidgetItem('%d' % j)
                self.tableWidgetCurrent.setItem(2, i + 6, newItem)
            '''转回质押日初始化标准券持仓变化'''
            for i, j in (enumerate(self.FirstStockList)):
                # print(i,j)
                newItem = QTableWidgetItem('%d' % j)
                self.tableWidgetStock.setItem(2, i + 6, newItem)
    
    @pyqtSlot()
    def on_btnExport_clicked(self):
        """
        Slot documentation goes here.
        定义导出函数
        """
        QMessageBox.information(self, '提示', '抱歉，该功能尚未开通！')
    
    @pyqtSlot()
    def on_btnCalculate_clicked(self):
        """
        Slot documentation goes here.
        定义计算函数
        """
        # 获得业务品种
        en_stock_type = self.c_stock_type.currentText()
        newItem = QTableWidgetItem('%s' % en_stock_type)
        self.tableWidgetCurrent.setItem(1, 1, newItem)
        newItem = QTableWidgetItem('%s' % en_stock_type)
        self.tableWidgetStock.setItem(1, 1, newItem)
        # 获得委托方向
        en_entrust_direction = self.c_entrust_direction.currentText()
        newItem = QTableWidgetItem('%s' % en_entrust_direction)
        self.tableWidgetCurrent.setItem(1, 2, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_direction)
        self.tableWidgetStock.setItem(1, 2, newItem)
        # 获得委托状态
        en_entrust_status = self.c_entrust_status.currentText()
        newItem = QTableWidgetItem('%s' % en_entrust_status)
        self.tableWidgetCurrent.setItem(1, 5,  newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_status)
        self.tableWidgetStock.setItem(1, 5,  newItem)
        # 获得委托数量
        en_entrust_amount = float(self.c_entrust_amount.text())
        newItem = QTableWidgetItem('%d' % en_entrust_amount)
        self.tableWidgetCurrent.setItem(1, 3, newItem)
        newItem = QTableWidgetItem('%d' % en_entrust_amount)
        self.tableWidgetStock.setItem(1,3, newItem)
        # 获得质押比例
        en_entrust_ratio = float(self.c_entrust_price.text())
        newItem = QTableWidgetItem('%.2f' % en_entrust_ratio)
        self.tableWidgetCurrent.setItem(1, 4, newItem)
        newItem = QTableWidgetItem('%.2f' % en_entrust_ratio)
        self.tableWidgetStock.setItem(1, 4,  newItem)
        if en_entrust_direction == '提交质押':
            
            '''提交质押已成持仓变化'''
            #当前债券持仓数量 = 期初债券持仓数量
            BondHolding  = self.FirstCurrentBond[0]
            # 向FirstCurrentBond列表添加当前持仓数量值
            self.FirstCurrentBond.pop(0)
            self.FirstCurrentBond.insert(0, BondHolding)
            # 债券可用数量=期初债券可用数量-债券质押数量
            BondEnable = self.FirstCurrentBond[1]-en_entrust_amount
            # 向FirstCurrentBond列表添加债券可用数量值
            self.FirstCurrentBond.pop(1)
            self.FirstCurrentBond.insert(1, BondEnable)
            # 债券冻结数量=期初债券冻结数量+债券质押数量
            BondFrozen = self.FirstCurrentBond[2] +en_entrust_amount
            # 向FirstCurrentBond列表添加债券冻结数量
            self.FirstCurrentBond.pop(2)
            self.FirstCurrentBond.insert(2, BondFrozen)
            # 债券解冻数量 = 期初债券解冻数量
            BondUnFrozen = self.FirstCurrentBond[3] 
            # 向FirstAssetList列表添加债券解冻数量
            self.FirstCurrentBond.pop(3)
            self.FirstCurrentBond.insert(3, BondUnFrozen)
            # 质押数量= 期初质押数量+已成质押数量
            BondPledge = self.FirstCurrentBond[4]+en_entrust_amount
            # 向FirstCurrentBond列表添加质押数量
            self.FirstCurrentBond.pop(4)
            self.FirstCurrentBond.insert(4, BondPledge)
            # 成本价=期初成本价
            CostPrice = self.FirstCurrentBond[5]
            # 向FirstCurrentBond列表添加成本价的值
            self.FirstCurrentBond.pop(5)
            self.FirstCurrentBond.insert(5, CostPrice)
            # 成本=期初成本
            Cost = self.FirstCurrentBond[6]
            # 向FirstCurrentBond列表添加成本的值
            self.FirstCurrentBond.pop(6)
            self.FirstCurrentBond.insert(6, Cost)
            # 含费用成本=期初含费用成本
            CostCost = self.FirstCurrentBond[7]
            # 向FirstCurrentBond列表添加含费用成本的值
            self.FirstCurrentBond.pop(7)
            self.FirstCurrentBond.insert(7, CostCost)
            # 债券持变化赋值
            for i, j in (enumerate(self.FirstCurrentBond)):
                newItem = QTableWidgetItem('%d' % j)
                self.tableWidgetCurrent.setItem(1, i + 6, newItem)
            self.log.logger.info('提交质押已成持仓变化:')
            '''提交质押已成标准券持仓变化'''
            #标准券当前持仓数量=期初标准券持仓数量
            currentAmount = self.FirstStockList[0]
            # 向FirstStockList列表添标准券当前持仓数量值
            self.FirstStockList.pop(0)
            self.FirstStockList.insert(0, currentAmount)
            # 可用数量=期初可用数量+委托数量*质押比例
            enableAmmount = self.FirstStockList[1] + en_entrust_amount*en_entrust_ratio
            # 向FirstStockList列表添加可用数量值
            self.FirstStockList.pop(1)
            self.FirstStockList.insert(1, enableAmmount)
            # 冻结数量=期初冻结数量
            frozenAmount = self.FirstStockList[2]
            # 向FirstStockList列表添加冻结数量值
            self.FirstStockList.pop(2)
            self.FirstStockList.insert(2, frozenAmount)
            # 解冻数量=期初解冻数量+委托数量*质押比例
            unfrozenAmount = self.FirstStockList[3]+ en_entrust_amount*en_entrust_ratio
            # 向FirstStockList列表添加解冻数量的值
            self.FirstStockList.pop(3)
            self.FirstStockList.insert(3, unfrozenAmount)
            # 成本价 = 期初成本价格
            # QMessageBox.information(self, '123', '%d' % self.FirstStockList[4])
            currentInvestPrice = self.FirstStockList[4] 
            # 向FirstStockList列表添加成本价的值
            self.FirstStockList.pop(4)
            self.FirstStockList.insert(4, currentInvestPrice)
            # 成本 = 期初成本
            currentInvest = self.FirstStockList[5] 
            # 向FirstStockList列表添加成本的值
            self.FirstStockList.pop(5)
            self.FirstStockList.insert(5, currentInvest)
            # 含费用成本 = 期初含费用成本
            currentInvest = self.FirstStockList[6] 
            # 向FirstStockList列表添加成本的值
            self.FirstStockList.pop(6)
            self.FirstStockList.insert(6, currentInvest)
            # print('长度为{0}'.format(len(self.FirstAssetList)))
            # 标准券持仓变化赋值
            for i, j in (enumerate(self.FirstStockList)):
                # print(i,j)
                newItem = QTableWidgetItem('%d' % j)
                self.tableWidgetStock.setItem(1, i + 6, newItem)
        else:
            '''转回质押已成债券持仓变化.
            '''
            #当前债券持仓数量 = 期初债券持仓数量
            BondHolding  = self.FirstCurrentBond[0]
            # 向FirstCurrentBond列表添加当前持仓数量值
            self.FirstCurrentBond.pop(0)
            self.FirstCurrentBond.insert(0, BondHolding)
            # 债券可用数量=期初债券可用数量+债券转回质押数量
            BondEnable = self.FirstCurrentBond[1]+en_entrust_amount
            # 向FirstCurrentBond列表添加债券可用数量值
            self.FirstCurrentBond.pop(1)
            self.FirstCurrentBond.insert(1, BondEnable)
            # 债券冻结数量=期初债券冻结数量-债券转回质押数量
            BondFrozen = self.FirstCurrentBond[2] -en_entrust_amount
            # 向FirstCurrentBond列表添加债券冻结数量
            self.FirstCurrentBond.pop(2)
            self.FirstCurrentBond.insert(2, BondFrozen)
            # 债券解冻数量 = 期初债券解冻数量
            BondUnFrozen = self.FirstCurrentBond[3] 
            # 向FirstAssetList列表添加债券解冻数量
            self.FirstCurrentBond.pop(3)
            self.FirstCurrentBond.insert(3, BondUnFrozen)
            # 质押数量= 期初质押数量-已成转回质押数量
            BondPledge = self.FirstCurrentBond[4]-en_entrust_amount
            # 向FirstCurrentBond列表添加质押数量
            self.FirstCurrentBond.pop(4)
            self.FirstCurrentBond.insert(4, BondPledge)
            # 成本价=期初成本价
            CostPrice = self.FirstCurrentBond[5]
            # 向FirstCurrentBond列表添加成本价的值
            self.FirstCurrentBond.pop(5)
            self.FirstCurrentBond.insert(5, CostPrice)
            # 成本=期初成本
            Cost = self.FirstCurrentBond[6]
            # 向FirstCurrentBond列表添加成本的值
            self.FirstCurrentBond.pop(6)
            self.FirstCurrentBond.insert(6, Cost)
            # 含费用成本=期初含费用成本
            CostCost = self.FirstCurrentBond[7]
            # 向FirstCurrentBond列表添加含费用成本的值
            self.FirstCurrentBond.pop(7)
            self.FirstCurrentBond.insert(7, CostCost)
            # 债券持变化赋值
            for i, j in (enumerate(self.FirstCurrentBond)):
                newItem = QTableWidgetItem('%d' % j)
                self.tableWidgetCurrent.setItem(1, i + 6, newItem)
            '''转回质押已成标准券持仓变化'''
            #标准券当前持仓数量=期初标准券持仓数量
            currentAmount = self.FirstStockList[0]
            # 向FirstStockList列表添标准券当前持仓数量值
            self.FirstStockList.pop(0)
            self.FirstStockList.insert(0, currentAmount)
            # 可用数量=期初可用数量-委托数量*质押比例
            enableAmmount = self.FirstStockList[1] - en_entrust_amount*en_entrust_ratio
            # 向FirstStockList列表添加可用数量值
            self.FirstStockList.pop(1)
            self.FirstStockList.insert(1, enableAmmount)
            # 冻结数量=期初冻结数量
            frozenAmount = self.FirstStockList[2]
            # 向FirstStockList列表添加冻结数量值
            self.FirstStockList.pop(2)
            self.FirstStockList.insert(2, frozenAmount)
            # 解冻数量=期初解冻数量-委托数量*质押比例
            unfrozenAmount = self.FirstStockList[3]-en_entrust_amount*en_entrust_ratio
            # 向FirstStockList列表添加解冻数量的值
            self.FirstStockList.pop(3)
            self.FirstStockList.insert(3, unfrozenAmount)
            # 成本价 = 期初成本价格
            # QMessageBox.information(self, '123', '%d' % self.FirstStockList[4])
            currentInvestPrice = self.FirstStockList[4] 
            # 向FirstStockList列表添加成本价的值
            self.FirstStockList.pop(4)
            self.FirstStockList.insert(4, currentInvestPrice)
            # 成本 = 期初成本
            currentInvest = self.FirstStockList[5] 
            # 向FirstStockList列表添加成本的值
            self.FirstStockList.pop(5)
            self.FirstStockList.insert(5, currentInvest)
            # 含费用成本 = 期初含费用成本
            currentInvest = self.FirstStockList[6] 
            # 向FirstStockList列表添加成本的值
            self.FirstStockList.pop(6)
            self.FirstStockList.insert(6, currentInvest)
            # print('长度为{0}'.format(len(self.FirstAssetList)))
            # 持仓变化赋值
            for i, j in (enumerate(self.FirstStockList)):
                # print(i,j)
                newItem = QTableWidgetItem('%d' % j)
                self.tableWidgetStock.setItem(1, i + 6, newItem)
    @pyqtSlot(int, int)
    def on_tableWidgetCurrent_cellDoubleClicked(self, row, column):
        """持仓变化表格双击弹出提示"""
        # 获得委托方向
        en_entrust_direction = self.c_entrust_direction.currentText()
        if row == 1:
            if en_entrust_direction == '提交质押':
                if column == 6:
                        QMessageBox.about(self, '当前持仓数量', '当前债券持仓数量 = 期初债券持仓数量')
                elif column == 7:
                        QMessageBox.about(self, '债券可用数量', '可用数量=期初债券可用数量-债券质押数量')
                elif column == 8:
                    QMessageBox.about(self, '债券冻结数量', '债券冻结数量=期初债券冻结数量+债券质押数量')
                elif column == 9:
                    QMessageBox.about(self, '债券解冻数量', '债券解冻数量 = 期初债券解冻数量')
                elif column == 10:
                    QMessageBox.about(self, '质押数量', '质押数量= 期初质押数量+已成质押数量）')
                elif column == 11:
                    QMessageBox.about(self, '成本价', '成本价=期初成本价')
                elif column == 12:
                    QMessageBox.about(self, '成本', '成本=期初成本')
                elif column == 13:
                    QMessageBox.about(self, '含费用成本', '含费用成本=期初含费用成本')
            else:
                if column == 6:
                        QMessageBox.about(self, '当前持仓数量', '当前债券持仓数量 = 期初债券持仓数量')
                elif column == 7:
                        QMessageBox.about(self, '债券可用数量', '可用数量=期初债券可用数量+债券质押数量')
                elif column == 8:
                    QMessageBox.about(self, '债券冻结数量', '债券冻结数量=期初债券冻结数量-债券转回质押数量')
                elif column == 9:
                    QMessageBox.about(self, '债券解冻数量', '债券解冻数量 = 期初债券解冻数量')
                elif column == 10:
                    QMessageBox.about(self, '质押数量', '质押数量= 期初质押数量-已成转回质押数量）')
                elif column == 11:
                    QMessageBox.about(self, '成本价', '成本价=期初成本价')
                elif column == 12:
                    QMessageBox.about(self, '成本', '成本=期初成本')
                elif column == 13:
                    QMessageBox.about(self, '含费用成本', '含费用成本=期初含费用成本')
    @pyqtSlot(int, int)
    def on_tableWidgetStock_cellDoubleClicked(self, row, column):
        """标准券变化表格双击弹出提示"""
        # 获得业务品种
        # 获得委托方向
        en_entrust_direction = self.c_entrust_direction.currentText()
        if row == 1:
            if en_entrust_direction == '提交质押':
                if column == 6:
                        QMessageBox.about(self, '标准券当前当前持仓数量', '当前标准券持仓数量 = 期初标准券持仓数量')
                elif column == 7:
                        QMessageBox.about(self, '可用数量', '可用数量=期初可用数量+质押数量*质押比例')
                elif column == 8:
                    QMessageBox.about(self, '冻结数量', '冻结数量=期初冻结数量')
                elif column == 9:
                    QMessageBox.about(self, '解冻数量', '解冻数量 = 期初解冻数量+质押数量*质押比例')
                elif column == 10:
                    QMessageBox.about(self, '成本价', '成本价=期初成本价')
                elif column == 11:
                    QMessageBox.about(self, '成本', '成本=期初成本')
                elif column == 12:
                    QMessageBox.about(self, '含费用成本', '含费用成本=期初含费用成本')
            else:
                if column == 6:
                        QMessageBox.about(self, '当前标准券持仓数量', '当前标准券持仓数量 = 期初标准券持仓数量')
                elif column == 7:
                        QMessageBox.about(self, '可用数量', '可用数量=期初可用数量-转回质押数量*委托比例')
                elif column == 8:
                    QMessageBox.about(self, '冻结数量', '冻结数量=期初标准券冻结数量')
                elif column == 9:
                    QMessageBox.about(self, '解冻数量', '解冻数量 = 期初解冻数量-转回质押数量*委托比例')
                elif column == 10:
                    QMessageBox.about(self, '成本价', '成本价=期初成本价')
                elif column == 11:
                    QMessageBox.about(self, '成本', '成本=期初成本')
                elif column == 12:
                    QMessageBox.about(self, '含费用成本', '含费用成本=期初含费用成本')
            
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = CallBondPledge()
    ui.show()
    sys.exit(app.exec_())
