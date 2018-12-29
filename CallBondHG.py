#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年12月26日
@author: Yiluo
@file: CallBondHG
@description:债券回购计算
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication,QTableWidget, QTableWidgetItem, QMessageBox
from Ui_BondHG import Ui_EnableTool

__Author__ = """
By: Yiluo 
QQ: 786129166
Email: 786129166@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Yiluo'
__Version__ = 1.0


class CallBondHG(QMainWindow, Ui_EnableTool):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(CallBondHG, self).__init__(parent)
        self.setupUi(self)
        self.iniUI()
    def iniUI(self):
        # 设置表格第一行第一列的字体颜色和背景颜色
#        for i in range(3):
#            self.tableWidgetAsset.item(i ,0).setForeground(QBrush(QColor(102,102,102)))
#            self.tableWidgetAsset.item(i, 0).setBackground(QBrush(QColor(193, 124, 172)))
#            
#            self.tableWidgetCurrent.item(i ,0).setForeground(QBrush(QColor(102,102,102)))
#            self.tableWidgetCurrent.item(i, 0).setBackground(QBrush(QColor(243, 243, 243)))
#            
#            self.tableWidgetStock.item(i ,0).setForeground(QBrush(QColor(102,102,102)))
#            self.tableWidgetStock.item(i, 0).setBackground(QBrush(QColor(243, 243, 243)))
#            
#            self.tableWidgetStandard.item(i ,0).setForeground(QBrush(QColor(102,102,102)))
#            self.tableWidgetStandard.item(i, 0).setBackground(QBrush(QColor(243, 243, 243)))
        self.tableWidgetAsset.setEditTriggers(QTableWidget.NoEditTriggers)
#        for x in range(self.tableWidgetAsset.columnCount()): 
#            print(x) 
#            headItem = self.tableWidgetAsset.horizontalHeaderItem(0)   #获得水平方向表头的Item对象
#            #设置单元格背景颜色
#            headItem.setBackground(QBrush(QColor(255, 255, 255)))
#            self.tableWidgetAsset.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")
#            headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        # 获取初始资产数据
        self.InitAssetList = []
        # 获取初始资金数据
        self.InitCurrentList = []
        # 获取初始证券数据
        self.InitStockList = []
         # 获取初始标准券数据
        self.InitStandardList = []
        for i in range(8, 17):
            demo = self.tableWidgetAsset.item(0, i).text()
            self.InitAssetList.append(float(demo))
        for j in range(8, 14):
            demo = self.tableWidgetCurrent.item(0, j).text()
            self.InitCurrentList.append(float(demo))
        for k in range(8, 15):
            demo = self.tableWidgetStock.item(0, k).text()
            self.InitStockList.append(float(demo))
        for w in range(8, 15):
            demo = self.tableWidgetStandard.item(0, w).text()
            self.InitStandardList.append(float(demo))
         # 获取计算后的资产数据
        self.FirstAssetList = self.InitAssetList[:]
        # 获取计算后的资金数据
        self.FirstCurrentList = self.InitCurrentList[:]
        # 获取计算后的证券数据
        self.FirstStockList = self.InitStockList[:]
        # 获取计算后的标准券数据
        self.FirstStandardList = self.InitStandardList[:]
        
#        self.tableWidgetAsset.horizontalHeader().setSectionResizeMode(1)#列宽设置
#        self.tableWidgetAsset.verticalHeader().setSectionResizeMode(1)#行高设置          
#        self.tableWidgetAsset.verticalHeader().setStretchLastSection(True); #充满行高         
#        self.resizeHeight(self.tableWidgetCurrent)
#        self.resizeHeight(self.tableWidgetStock)
        
  
    def resizeHeight(self, table):
        table.horizontalHeader().setSectionResizeMode(2)#列宽设置

        table.horizontalHeader().setStretchLastSection(True); #充满列宽    

        table.verticalHeader().setSectionResizeMode(1)#行高设置          

        table.verticalHeader().setStretchLastSection(True); #充满行高  
        
    @pyqtSlot()
    def on_btnCalculate_clicked(self):
        """
        Slot documentation goes here.
        定义计算函数
        """
        # 获得业务品种
        en_stock_type = self.c_stock_type.currentText()
        newItem = QTableWidgetItem('%s' % en_stock_type)
        self.tableWidgetAsset.setItem(1, 1, newItem)
        newItem = QTableWidgetItem('%s' % en_stock_type)
        self.tableWidgetCurrent.setItem(1, 1, newItem)
        newItem = QTableWidgetItem('%s' % en_stock_type)
        self.tableWidgetStock.setItem(1, 1, newItem)
        newItem = QTableWidgetItem('%s' % en_stock_type)
        self.tableWidgetStandard.setItem(1, 1, newItem)
        # 获得委托方向
        en_entrust_direction = self.c_entrust_direction.currentText()
        newItem = QTableWidgetItem('%s' % en_entrust_direction)
        self.tableWidgetAsset.setItem(1, 2, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_direction)
        self.tableWidgetCurrent.setItem(1, 2, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_direction)
        self.tableWidgetStock.setItem(1, 2, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_direction)
        self.tableWidgetStandard.setItem(1, 2, newItem)
        # 获得证券代码
        en_stock = self.l_stock.text()
        newItem = QTableWidgetItem('%s' % en_stock)
        self.tableWidgetAsset.setItem(1, 3, newItem)
        newItem = QTableWidgetItem('%s' % en_stock)
        self.tableWidgetCurrent.setItem(1, 3, newItem)
        newItem = QTableWidgetItem('%s' % en_stock)
        self.tableWidgetStock.setItem(1, 3, newItem)
        newItem = QTableWidgetItem('%s' % en_stock)
        self.tableWidgetStandard.setItem(1, 3, newItem)
        # 获得委托状态
        en_entrust_status = self.c_entrust_status.currentText()
        newItem = QTableWidgetItem('%s' % en_entrust_status)
        self.tableWidgetAsset.setItem(1, 7, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_status)
        self.tableWidgetCurrent.setItem(1, 7, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_status)
        self.tableWidgetStock.setItem(1, 7, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_status)
        self.tableWidgetStandard.setItem(1, 7, newItem)
        # 获得委托数量
        en_entrust_amount = float(self.c_entrust_amount.text())
        newItem = QTableWidgetItem('%d' % en_entrust_amount)
        self.tableWidgetAsset.setItem(1, 4, newItem)
        newItem = QTableWidgetItem('%d' % en_entrust_amount)
        self.tableWidgetCurrent.setItem(1, 4, newItem)
        newItem = QTableWidgetItem('%d' % en_entrust_amount)
        self.tableWidgetStock.setItem(1, 4, newItem)
        newItem = QTableWidgetItem('%d' % en_entrust_amount)
        self.tableWidgetStandard.setItem(1, 4, newItem)
        # 获得委托价格
        en_entrust_price = float(self.c_entrust_price.text())
        newItem = QTableWidgetItem('%.2f' % en_entrust_price)
        self.tableWidgetAsset.setItem(1, 5, newItem)
        newItem = QTableWidgetItem('%.2f' % en_entrust_price)
        self.tableWidgetCurrent.setItem(1, 5, newItem)
        newItem = QTableWidgetItem('%.2f' % en_entrust_price)
        self.tableWidgetStock.setItem(1, 5, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_price)
        self.tableWidgetStandard.setItem(1, 5, newItem)
        # 获得交易费率
        en_bond_interest = float(self.c_bond_interest.text())
        newItem = QTableWidgetItem('%.6f' % en_bond_interest)
        self.tableWidgetAsset.setItem(1, 6, newItem)
        newItem = QTableWidgetItem('%.6f' % en_bond_interest)
        self.tableWidgetCurrent.setItem(1, 6, newItem)
        newItem = QTableWidgetItem('%.6f' % en_bond_interest)
        self.tableWidgetStock.setItem(1, 6, newItem)
        newItem = QTableWidgetItem('%.6f' % en_bond_interest)
        self.tableWidgetStandard.setItem(1, 6, newItem)
        if en_entrust_direction == '融资回购':
            if en_entrust_status == '已报':
                '''资产不变'''
                for i in range(len(self.InitAssetList)):
                    newItem = QTableWidgetItem('%.2f' % int(self.InitAssetList[i]))
                    self.tableWidgetAsset.setItem(1, i + 8, newItem)
                '''资金不变'''
                for i in range(len(self.InitCurrentList)):
                    newItem = QTableWidgetItem('%.2f' % int(self.InitCurrentList[i]))
                    self.tableWidgetCurrent.setItem(1, i + 8, newItem)
                '''债券持仓不变'''
                for i in range(len(self.InitStockList)):
                    newItem = QTableWidgetItem('%d' % int(self.InitStockList[i]))
                    self.tableWidgetStock.setItem(1, i + 8, newItem)
                '''标准券持仓变化'''
                for i in range(len(self.FirstStandardList)):
                    if i ==1:
                        # 可用数量=期初可用数量-回购数量
                        enableAmmount = self.FirstStandardList[i] - en_entrust_amount
                        # 向FirstStockList列表添加T+0可用数量值
                        #print(len(self.FirstStockList))
                        self.FirstStandardList.pop(1)
                        self.FirstStandardList.insert(1, enableAmmount)
                    elif i ==3:
                        # 解冻数量=期初解冻数量-回购数量
                        unfrozenAmount = self.FirstStandardList[3]-en_entrust_amount
                        # 向FirstStockList列表添加解冻的值
                        self.FirstStandardList.pop(3)
                        self.FirstStandardList.insert(3, unfrozenAmount)
                    newItem = QTableWidgetItem('%d' % int(self.FirstStandardList[i]))
                    self.tableWidgetStandard.setItem(1, i + 8, newItem)
            else:
                '''资产变化'''
                for i in range(len(self.FirstAssetList)):
                    if i == 0:
                        #资金资产=期初资金资产+回购数量*100*(1-交易费率)
                        CurrentAsset = self.FirstAssetList[i]+en_entrust_amount*100*(1-en_bond_interest)
                        # 向FirstAssetList列表添加资金资产值
                        self.FirstAssetList.pop(0)
                        self.FirstAssetList.insert(0, CurrentAsset)
                    elif i == 2:
                        #回购资产=期初回购资产-回购数量*100*(1-交易费率)
                        HGAsset = self.FirstAssetList[i]-en_entrust_amount*100*(1-en_bond_interest)
                        # 向FirstAssetList列表添加回购资产值
                        self.FirstAssetList.pop(i)
                        self.FirstAssetList.insert(i, HGAsset)
                    newItem = QTableWidgetItem('%.2f' % self.FirstAssetList[i])
                    self.tableWidgetAsset.setItem(1, i + 8, newItem)
                '''资金变化'''
                #交易费=期初交易费+委托数量*100*交易费率
                TradeFee = self.FirstCurrentList[0]+en_entrust_amount*100*en_bond_interest
                #向FirstAssetList添加交易费
                self.FirstCurrentList.pop(0)
                self.FirstCurrentList.insert(0, TradeFee)
                # 当前现金余额=期初当前现金余额+委托数量*100*(1-交易费率)
                cashBalance = self.FirstCurrentList[1] +en_entrust_amount*100*(1-en_bond_interest)
                # 向FirstCurrentList列表添加现金资产值
                self.FirstCurrentList.pop(1)
                self.FirstCurrentList.insert(1, cashBalance)
                # T+0可用金额=期初T+0可用金额+委托数量*100*(1-交易费率)
                T0Balance = self.FirstCurrentList[2]+en_entrust_amount*100*(1-en_bond_interest)
                # 向FirstCurrentList列表添加T+0可用金额值
                #print(len(self.FirstCurrentList))
                self.FirstCurrentList.pop(2)
                self.FirstCurrentList.insert(2, T0Balance)
                # T+1可用金额=期初T+1可用金额+委托数量*100*(1-交易费率)
                T1Balance = self.FirstCurrentList[3] +en_entrust_amount*100*(1-en_bond_interest)
                # 向FirstAssetList列表添加应收值
                self.FirstCurrentList.pop(3)
                self.FirstCurrentList.insert(3, T1Balance)
                # 冻结金额=期初冻结金额+委托数量*100*(1-交易费率)
                frozenBalance = self.FirstCurrentList[4]+en_entrust_amount*100*(1-en_bond_interest)
                # 向FirstCurrentList列表添加冻结金额值
                self.FirstCurrentList.pop(4)
                self.FirstCurrentList.insert(4, frozenBalance)
                # 解冻金额=期初解冻数量
                unfrozenBalance = self.FirstCurrentList[5] 
                # 向FirstCurrentList列表添加解冻金额的值
                self.FirstCurrentList.pop(5)
                self.FirstCurrentList.insert(5, unfrozenBalance)
                # 资金变化赋值
                for i, j in (enumerate(self.FirstCurrentList)):
                    # print(i,j)
                    newItem = QTableWidgetItem('%.2f' % j)
                    self.tableWidgetCurrent.setItem(1, i +8, newItem)
                '''持仓变化'''
                for i in range(len(self.FirstStockList)):
                    if i ==0:
                        # 当前持仓数量=期初持仓数量-回购数量
                        currentAmount = self.FirstStockList[i] - en_entrust_amount
                        # 向FirstStockList列表添加当前持仓数量值
                        #print(len(self.FirstStockList))
                        self.FirstStockList.pop(i)
                        self.FirstStockList.insert(i, currentAmount)
                    elif i ==2:
                        #冻结数量=期初冻结数量-回购数量
                        frozenAmount = self.FirstStockList[i]-en_entrust_amount
                        # 向FirstStockList列表添加冻结数量的值
                        self.FirstStockList.pop(i)
                        self.FirstStockList.insert(i, frozenAmount)
                    newItem = QTableWidgetItem('%d' % int(self.FirstStockList[i]))
                    self.tableWidgetStock.setItem(1, i + 8, newItem)
                '''标准券持仓变化'''
                for i in range(len(self.FirstStandardList)):
                    if i == 0:
                        # 当前持仓数量=期初持仓数量-回购数量
                        currentAmount = self.FirstStandardList[i] - en_entrust_amount
                        # 向FirstStockList列表添加T+0可用数量值
                        #print(len(self.FirstStockList))
                        self.FirstStandardList.pop(i)
                        self.FirstStandardList.insert(i, currentAmount)
                    elif i ==1:
                        # 可用数量=期初可用数量-回购数量
                        enableAmmount = self.FirstStandardList[i] - en_entrust_amount
                        # 向FirstStockList列表添加T+0可用数量值
                        #print(len(self.FirstStockList))
                        self.FirstStandardList.pop(1)
                        self.FirstStandardList.insert(1, enableAmmount)
                    newItem = QTableWidgetItem('%d' % int(self.FirstStandardList[i]))
                    self.tableWidgetStandard.setItem(1, i + 8, newItem)
        else:
            if en_entrust_status == '已报':
                '''资产不变'''
                for i in range(len(self.InitAssetList)):
                    newItem = QTableWidgetItem('%.2f' % int(self.InitAssetList[i]))
                    self.tableWidgetAsset.setItem(1, i + 8, newItem)
                '''资金变化'''
                for i in range(len(self.InitCurrentList)):
                    if i == 2:
                       # T+0可用金额=期初T+0可用金额-成交数量*100
                       T0Balance = self.FirstCurrentList[i] - en_entrust_amount *100
                       # 向FirstCurrentList列表添加T+0可用金额值
                       self.FirstCurrentList.pop(i)
                       self.FirstCurrentList.insert(i, T0Balance)
                    elif i == 3:
                       # T+1可用金额=期初T+0可用金额-成交数量*100
                       T1Balance = self.FirstCurrentList[i] - en_entrust_amount *100
                       # 向FirstCurrentList列表添加T+0可用金额值
                       self.FirstCurrentList.pop(i)
                       self.FirstCurrentList.insert(i, T1Balance)
                    newItem = QTableWidgetItem('%.2f' % self.FirstCurrentList[i])
                    self.tableWidgetCurrent.setItem(1, i + 8, newItem)
                '''债券持仓不变'''
                for i in range(len(self.InitStockList)):
                    newItem = QTableWidgetItem('%d' % int(self.InitStockList[i]))
                    self.tableWidgetStock.setItem(1, i + 8, newItem)
                '''标准券不变'''
                for i in range(len(self.InitStandardList)):
                    newItem = QTableWidgetItem('%d' % int(self.InitStandardList[i]))
                    self.tableWidgetStandard.setItem(1, i + 8, newItem)
            else:
                '''资产变化'''
                for i in range(len(self.FirstAssetList)):
                    if i == 0:
                        #资金资产=期初资金资产-委托数量*100*(1+交易费率)
                        CurrentAsset = self.FirstAssetList[i]-en_entrust_amount*100*(1+en_bond_interest)
                        # 向FirstAssetList列表添加资金资产值
                        self.FirstAssetList.pop(0)
                        self.FirstAssetList.insert(0, CurrentAsset)
                    elif i == 2:
                        #回购资产=期初回购资产+回购数量*100*(1+交易费率)
                        HGAsset = self.FirstAssetList[i]+en_entrust_amount*100*(1+en_bond_interest)
                        # 向FirstAssetList列表添加回购资产值
                        self.FirstAssetList.pop(i)
                        self.FirstAssetList.insert(i, HGAsset)
                    elif i == 5:
                        #总资产=期初总资产-回购数量*100*(1+交易费率)
                        TotalAsset = self.FirstAssetList[i]+en_entrust_amount*100*(1+en_bond_interest)
                        # 向FirstAssetList列表添加总资产值
                        self.FirstAssetList.pop(i)
                        self.FirstAssetList.insert(i, TotalAsset)
                    elif i ==6 :
                        # 净值=现金资产+证券资产+应收-应付
                        valueAsset = CurrentAsset + self.FirstAssetList[1] + self.FirstAssetList[3] - self.FirstAssetList[4]
                        # 向FirstAssetList列表添加净值的值
                        self.FirstAssetList.pop(5)
                        self.FirstAssetList.insert(5, valueAsset)
                    newItem = QTableWidgetItem('%.2f' % self.FirstAssetList[i])
                    self.tableWidgetAsset.setItem(1, i + 8, newItem)
                '''资金变化'''
                #交易费=期初交易费+委托数量*100*交易费率
                TradeFee = self.FirstCurrentList[0]+en_entrust_amount*100*en_bond_interest
                #向FirstAssetList添加交易费
                self.FirstCurrentList.pop(0)
                self.FirstCurrentList.insert(0, TradeFee)
                # 当前现金余额=期初当前现金余额-委托数量*100*(1+交易费率)
                cashBalance = self.FirstCurrentList[1] -en_entrust_amount*100*(1+en_bond_interest)
                # 向FirstCurrentList列表添加现金资产值
                self.FirstCurrentList.pop(1)
                self.FirstCurrentList.insert(1, cashBalance)
                # T+0可用金额=期初T+0可用金额-委托数量*100*(1+交易费率)
                T0Balance = self.FirstCurrentList[2]-en_entrust_amount*100*(1+en_bond_interest)
                # 向FirstCurrentList列表添加T+0可用金额值
                #print(len(self.FirstCurrentList))
                self.FirstCurrentList.pop(2)
                self.FirstCurrentList.insert(2, T0Balance)
                # T+1可用金额=期初T+1可用金额-委托数量*100*(1+交易费率)
                T1Balance = self.FirstCurrentList[3] -en_entrust_amount*100*(1+en_bond_interest)
                # 向FirstAssetList列表添加T1可用金额值
                self.FirstCurrentList.pop(3)
                self.FirstCurrentList.insert(3, T1Balance)
                # 冻结金额=期初冻结金额
                frozenBalance = self.FirstCurrentList[4]
                # 向FirstCurrentList列表添加冻结金额值
                self.FirstCurrentList.pop(4)
                self.FirstCurrentList.insert(4, frozenBalance)
                # 解冻金额=期初解冻数量+委托数量*100*(1+交易费率)
                unfrozenBalance = self.FirstCurrentList[5]+en_entrust_amount*100*(1+en_bond_interest)
                # 向FirstCurrentList列表添加解冻金额的值
                self.FirstCurrentList.pop(5)
                self.FirstCurrentList.insert(5, unfrozenBalance)
                # 资金变化赋值
                for i, j in (enumerate(self.FirstCurrentList)):
                    # print(i,j)
                    newItem = QTableWidgetItem('%.2f' % j)
                    self.tableWidgetCurrent.setItem(1, i +8, newItem)
                '''持仓变化'''
                for i in range(len(self.FirstStockList)):
                    if i ==0:
                        # 当前持仓数量=期初持仓数量+回购数量
                        currentAmount = self.FirstStockList[i] + en_entrust_amount
                        # 向FirstStockList列表添加当前持仓数量值
                        #print(len(self.FirstStockList))
                        self.FirstStockList.pop(i)
                        self.FirstStockList.insert(i, currentAmount)
                    elif i ==1:
                        #可用数量=期初可用数量+回购数量
                        enableAmount = self.FirstStockList[i]+en_entrust_amount
                        # 向FirstStockList列表添加冻结数量的值
                        self.FirstStockList.pop(i)
                        self.FirstStockList.insert(i, enableAmount)
                    newItem = QTableWidgetItem('%d' % int(self.FirstStockList[i]))
                    self.tableWidgetStock.setItem(1, i + 8, newItem)
                '''标准券持仓变化'''
                for i in range(len(self.FirstStandardList)):
                    if i == 0:
                        # 当前持仓数量=期初持仓数量+回购数量
                        currentAmount = self.FirstStandardList[i] + en_entrust_amount
                        # 向FirstStockList列表添加T+0可用数量值
                        #print(len(self.FirstStockList))
                        self.FirstStandardList.pop(i)
                        self.FirstStandardList.insert(i, currentAmount)
                    elif i ==2:
                        # 冻结数量=期初可用数量-回购数量
                        frozenAmmount = self.FirstStandardList[i] + en_entrust_amount
                        # 向FirstStockList列表添加T+0可用数量值
                        #print(len(self.FirstStockList))
                        self.FirstStandardList.pop(i)
                        self.FirstStandardList.insert(i, frozenAmmount)
                    newItem = QTableWidgetItem('%d' % int(self.FirstStandardList[i]))
                    self.tableWidgetStandard.setItem(1, i + 8, newItem)
                
            
                
                
    
    @pyqtSlot()
    def on_btnClear_clicked(self):
        """
        Slot documentation goes here.
        定义清空函数
        """
        # TODO: not implemented yet
        '''清空资产变化'''
        for i in range(1, 3):
            for j in range(1, 17):
                newItem = QTableWidgetItem('')
                self.tableWidgetAsset.setItem(i, j, newItem)
        '''清空资金变化'''
        for i in range(1, 3):
            for j in range(1, 14):
                newItem = QTableWidgetItem('')
                self.tableWidgetCurrent.setItem(i, j, newItem)
        '''清空证券变化'''
        for i in range(1, 3):
            for j in range(1, 15):
                newItem = QTableWidgetItem('')
                self.tableWidgetStock.setItem(i, j, newItem)
        '''清空标准券变化'''
        for i in range(1, 3):
            for j in range(1, 15):
                newItem = QTableWidgetItem('')
                self.tableWidgetStandard.setItem(i, j, newItem)
        # 获取计算后的资产数据
        self.FirstAssetList = self.InitAssetList[:]
        # 获取计算后的资金数据
        self.FirstCurrentList = self.InitCurrentList[:]
        # 获取计算后的证券数据
        self.FirstStockList = self.InitStockList[:]
        # 获取计算后的标准券数据
        self.FirstStandardList = self.InitStandardList[:]
    
    @pyqtSlot()
    def on_btnInit_clicked(self):
        """
        Slot documentation goes here.
        定义日初始化函数
        """
        # 获得业务品种
        en_stock_type = self.c_stock_type.currentText()
        newItem = QTableWidgetItem('%s' % en_stock_type)
        self.tableWidgetAsset.setItem(2, 1, newItem)
        newItem = QTableWidgetItem('%s' % en_stock_type)
        self.tableWidgetCurrent.setItem(2, 1, newItem)
        newItem = QTableWidgetItem('%s' % en_stock_type)
        self.tableWidgetStock.setItem(2, 1, newItem)
        newItem = QTableWidgetItem('%s' % en_stock_type)
        self.tableWidgetStandard.setItem(2, 1, newItem)
        # 获得委托方向
        en_entrust_direction = self.c_entrust_direction.currentText()
        newItem = QTableWidgetItem('%s' % en_entrust_direction)
        self.tableWidgetAsset.setItem(2, 2, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_direction)
        self.tableWidgetCurrent.setItem(2, 2, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_direction)
        self.tableWidgetStock.setItem(2, 2, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_direction)
        self.tableWidgetStandard.setItem(2, 2, newItem)
        # 获得证券代码
        en_stock = self.l_stock.text()
        newItem = QTableWidgetItem('%s' % en_stock)
        self.tableWidgetAsset.setItem(2, 3, newItem)
        newItem = QTableWidgetItem('%s' % en_stock)
        self.tableWidgetCurrent.setItem(2, 3, newItem)
        newItem = QTableWidgetItem('%s' % en_stock)
        self.tableWidgetStock.setItem(2, 3, newItem)
        newItem = QTableWidgetItem('%s' % en_stock)
        self.tableWidgetStandard.setItem(2, 3, newItem)
        # 获得委托状态
        en_entrust_status = self.c_entrust_status.currentText()
        newItem = QTableWidgetItem('%s' % en_entrust_status)
        self.tableWidgetAsset.setItem(2, 7, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_status)
        self.tableWidgetCurrent.setItem(2, 7, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_status)
        self.tableWidgetStock.setItem(2, 7, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_status)
        self.tableWidgetStandard.setItem(2, 7, newItem)
        # 获得委托数量
        en_entrust_amount = float(self.c_entrust_amount.text())
        newItem = QTableWidgetItem('%d' % en_entrust_amount)
        self.tableWidgetAsset.setItem(2, 4, newItem)
        newItem = QTableWidgetItem('%d' % en_entrust_amount)
        self.tableWidgetCurrent.setItem(2, 4, newItem)
        newItem = QTableWidgetItem('%d' % en_entrust_amount)
        self.tableWidgetStock.setItem(2, 4, newItem)
        newItem = QTableWidgetItem('%d' % en_entrust_amount)
        self.tableWidgetStandard.setItem(2, 4, newItem)
        # 获得委托价格
        en_entrust_price = float(self.c_entrust_price.text())
        newItem = QTableWidgetItem('%.2f' % en_entrust_price)
        self.tableWidgetAsset.setItem(2, 5, newItem)
        newItem = QTableWidgetItem('%.2f' % en_entrust_price)
        self.tableWidgetCurrent.setItem(2, 5, newItem)
        newItem = QTableWidgetItem('%.2f' % en_entrust_price)
        self.tableWidgetStock.setItem(2, 5, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_price)
        self.tableWidgetStandard.setItem(2, 5, newItem)
        # 获得交易费率
        en_bond_interest = float(self.c_bond_interest.text())
        newItem = QTableWidgetItem('%.6f' % en_bond_interest)
        self.tableWidgetAsset.setItem(2, 6, newItem)
        newItem = QTableWidgetItem('%.6f' % en_bond_interest)
        self.tableWidgetCurrent.setItem(2, 6, newItem)
        newItem = QTableWidgetItem('%.6f' % en_bond_interest)
        self.tableWidgetStock.setItem(2, 6, newItem)
        newItem = QTableWidgetItem('%.6f' % en_bond_interest)
        self.tableWidgetStandard.setItem(2, 6, newItem)
        if en_entrust_direction == '融资回购':
            if en_entrust_status == '已报':
                '''资产不变'''
                for i in range(len(self.InitAssetList)):
                    newItem = QTableWidgetItem('%.2f' % int(self.InitAssetList[i]))
                    self.tableWidgetAsset.setItem(2, i + 8, newItem)
                '''资金不变'''
                for i in range(len(self.InitCurrentList)):
                    newItem = QTableWidgetItem('%.2f' % int(self.InitCurrentList[i]))
                    self.tableWidgetCurrent.setItem(2, i + 8, newItem)
                '''债券持仓不变'''
                for i in range(len(self.InitStockList)):
                    newItem = QTableWidgetItem('%d' % int(self.InitStockList[i]))
                    self.tableWidgetStock.setItem(2, i + 8, newItem)
                '''标准券不变'''
                for i in range(len(self.InitStandardList)):
                    newItem = QTableWidgetItem('%d' % int(self.InitStandardList[i]))
                    self.tableWidgetStandard.setItem(2, i + 8, newItem)
            else:
                '''资产变化'''
                for i in range(len(self.FirstAssetList)):
                    if i == 0:
                        #资金资产=期初资金资产-委托数量*100*(1-交易费率)-委托数量*100(委托价格/365+1)
                        CurrentAsset = self.FirstAssetList[i]-en_entrust_amount*100*(1-en_bond_interest)-en_entrust_amount*100*(float(en_entrust_price)/365+1)
                        # 向FirstAssetList列表添加资金资产值
                        self.FirstAssetList.pop(0)
                        self.FirstAssetList.insert(0, CurrentAsset)
                    elif i == 2:
                        #回购资产=期初回购资产
                        self.FirstAssetList.pop(i)
                        self.FirstAssetList.insert(i, self.InitAssetList[2])
                    elif i == 5:
                        #总资产=期初总资产-回购数量*100*((委托价格+交易费率)/365)
                        TotalAsset = self.FirstAssetList[i]-en_entrust_amount*100*((en_entrust_price+en_bond_interest)/365)
                        # 向FirstAssetList列表添加总资产值
                        self.FirstAssetList.pop(i)
                        self.FirstAssetList.insert(i, TotalAsset)
                    elif i ==6 :
                        # 净值=现金资产+证券资产+应收-应付
                        valueAsset = CurrentAsset + self.FirstAssetList[1] + self.FirstAssetList[3] - self.FirstAssetList[4]
                        # 向FirstAssetList列表添加净值的值
                        self.FirstAssetList.pop(5)
                        self.FirstAssetList.insert(5, valueAsset)
                    elif i == 8:
                        #单位净值 = 净值/总份额
                        perValueAsset = valueAsset /self.FirstAssetList[7]
                        # 向FirstAssetList列表添加单位净值的值
                        self.FirstAssetList.pop(i)
                        self.FirstAssetList.insert(i, perValueAsset)
                    newItem = QTableWidgetItem('%.2f' % self.FirstAssetList[i])
                    self.tableWidgetAsset.setItem(2, i + 8, newItem)
                '''资金变化'''
                #交易费=期初交易费
                #向FirstAssetList添加交易费
                self.FirstCurrentList.pop(0)
                self.FirstCurrentList.insert(0, 0)
                # 当前现金余额=期初当前现金余额+委托数量*100*(1-交易费率)-委托数量*100(委托价格/365+1)
                cashBalance = self.InitCurrentList[1] +en_entrust_amount*100*(1-en_bond_interest)-en_entrust_amount*100*(float(en_entrust_price)/365+1)
                # 向FirstCurrentList列表添加现金资产值
                self.FirstCurrentList.pop(1)
                self.FirstCurrentList.insert(1, cashBalance)
                # T+0可用金额=期初T+0可用金额+委托数量*100*(1-交易费率)-委托数量*100(委托价格/365+1)
                T0Balance = self.FirstCurrentList[2]+en_entrust_amount*100*(1-en_bond_interest)-en_entrust_amount*100*(float(en_entrust_price)/365+1)
                # 向FirstCurrentList列表添加T+0可用金额值
                #print(len(self.FirstCurrentList))
                self.FirstCurrentList.pop(2)
                self.FirstCurrentList.insert(2, T0Balance)
                # T+1可用金额=期初T+1可用金额+委托数量*100*(1-交易费率)-委托数量*100(委托价格/365+1)
                T1Balance = self.FirstCurrentList[3] +en_entrust_amount*100*(1-en_bond_interest)-en_entrust_amount*100*(float(en_entrust_price)/365+1)
                # 向FirstAssetList列表添加T1可用金额值
                self.FirstCurrentList.pop(3)
                self.FirstCurrentList.insert(3, T1Balance)
                # 冻结金额=期初冻结金额
                frozenBalance = self.InitCurrentList[4]
                # 向FirstCurrentList列表添加冻结金额值
                self.FirstCurrentList.pop(4)
                self.FirstCurrentList.insert(4, frozenBalance)
                # 解冻金额=期初解冻数量+委托数量*100*(1-交易费率)-委托数量*100(委托价格/365+1)
                unfrozenBalance = self.FirstCurrentList[5]+en_entrust_amount*100*(float(en_entrust_price)/365+1)
                # 向FirstCurrentList列表添加解冻金额的值
                self.FirstCurrentList.pop(5)
                self.FirstCurrentList.insert(5, unfrozenBalance)
                # 资金变化赋值
                for i, j in (enumerate(self.FirstCurrentList)):
                    # print(i,j)
                    newItem = QTableWidgetItem('%.2f' % j)
                    self.tableWidgetCurrent.setItem(2, i +8, newItem)
                '''持仓变化'''
                for i in range(len(self.FirstStockList)):
                    if i ==0:
                        # 当前持仓数量=期初持仓数量
                        currentAmount = self.FirstStockList[i]
                        # 向FirstStockList列表添加当前持仓数量值
                        #print(len(self.FirstStockList))
                        self.FirstStockList.pop(i)
                        self.FirstStockList.insert(i, currentAmount)
                    elif i ==2:
                        #冻结数量=期初冻结数量
                        frozenAmount = self.InitStockList[i]
                        # 向FirstStockList列表添加冻结数量的值
                        self.FirstStockList.pop(i)
                        self.FirstStockList.insert(i, frozenAmount)
                    elif i == 5:
                        # 成本 = 期初成本+100*成交数量
                        currentInvest = self.FirstStockList[i] + 100 * en_entrust_amount
                        # 向FirstStockList列表添加成本的值
                        self.FirstStockList.pop(i)
                        self.FirstStockList.insert(i, currentInvest)
                    elif i == 6:
                        # 含费用成本 = 期初含费用成本+100*成交数量
                        currentInvestFee = self.FirstStockList[6] +100 * en_entrust_amount
                        # 向FirstStockList列表添加成本的值
                        self.FirstStockList.pop(6)
                        self.FirstStockList.insert(6, currentInvestFee)
                    newItem = QTableWidgetItem('%d' % int(self.FirstStockList[i]))
                    self.tableWidgetStock.setItem(2, i + 8, newItem)
                '''标准券不变'''
                for i in range(len(self.InitStandardList)):
                    newItem = QTableWidgetItem('%d' % int(self.InitStandardList[i]))
                    self.tableWidgetStandard.setItem(2, i + 8, newItem)
        else:
            if en_entrust_status == '已报':
                '''资金不变'''
                for i in range(len(self.InitAssetList)):
                    newItem = QTableWidgetItem('%.2f' % int(self.InitAssetList[i]))
                    self.tableWidgetAsset.setItem(2, i + 8, newItem)
                '''资金不变'''
                for i in range(len(self.InitCurrentList)):
                    newItem = QTableWidgetItem('%.2f' % int(self.InitCurrentList[i]))
                    self.tableWidgetCurrent.setItem(2, i + 8, newItem)
                '''债券持仓不变'''
                for i in range(len(self.InitStockList)):
                    newItem = QTableWidgetItem('%d' % int(self.InitStockList[i]))
                    self.tableWidgetStock.setItem(2, i + 8, newItem)
                '''标准券持仓变化'''
                for i in range(len(self.FirstStandardList)):
                    newItem = QTableWidgetItem('%d' % int(self.FirstStandardList[i]))
                    self.tableWidgetStandard.setItem(2, i + 8, newItem)
            else:
                '''资产变化'''
                for i in range(len(self.FirstAssetList)):
                    if i == 0:
                        #资金资产=期初资金资产-委托数量*100*(1+交易费率)+委托数量*100(委托价格/365+1)
                        CurrentAsset = self.InitAssetList[i]-en_entrust_amount*100*(1+en_bond_interest)+en_entrust_amount*100*(float(en_entrust_price)/365+1)
                        # 向FirstAssetList列表添加资金资产值
                        self.FirstAssetList.pop(0)
                        self.FirstAssetList.insert(0, CurrentAsset)
                    elif i == 2:
                        #回购资产=期初回购资产
                        self.FirstAssetList.pop(i)
                        self.FirstAssetList.insert(i, self.InitAssetList[2])
                    elif i == 5:
                        #总资产=期初总资产-委托数量*100*(1+交易费率)+委托数量*100(委托价格/365+1)
                        TotalAsset = self.InitAssetList[i]-en_entrust_amount*100*(1+en_bond_interest)+en_entrust_amount*100*(float(en_entrust_price)/365+1)
                        # 向FirstAssetList列表添加总资产值
                        self.FirstAssetList.pop(i)
                        self.FirstAssetList.insert(i, TotalAsset)
                    elif i ==6 :
                        # 净值=现金资产+证券资产+应收-应付
                        valueAsset = CurrentAsset + self.FirstAssetList[1] + self.FirstAssetList[3] - self.FirstAssetList[4]
                        # 向FirstAssetList列表添加净值的值
                        self.FirstAssetList.pop(i)
                        self.FirstAssetList.insert(i, valueAsset)
                    elif i == 8:
                        #单位净值 = 净值/总份额
                        perValueAsset = valueAsset /self.FirstAssetList[7]
                        # 向FirstAssetList列表添加单位净值的值
                        self.FirstAssetList.pop(i)
                        self.FirstAssetList.insert(i, perValueAsset)
                    newItem = QTableWidgetItem('%.2f' % self.FirstAssetList[i])
                    self.tableWidgetAsset.setItem(2, i + 8, newItem)
                '''资金变化'''
                #交易费=期初交易费
                #向FirstAssetList添加交易费
                self.FirstCurrentList.pop(0)
                self.FirstCurrentList.insert(0, 0)
                # 当前现金余额=期初当前现金余额-委托数量*100*(1+交易费率)-委托数量*100(委托价格/365+1)
                cashBalance = self.InitCurrentList[1] -en_entrust_amount*100*(1+en_bond_interest)-en_entrust_amount*100*(float(en_entrust_price)/365+1)
                # 向FirstCurrentList列表添加现金资产值
                self.FirstCurrentList.pop(1)
                self.FirstCurrentList.insert(1, cashBalance)
                # T+0可用金额=期初T+0可用金额-委托数量*100*(1+交易费率)
                T0Balance = self.FirstCurrentList[2]-en_entrust_amount*100*(1+en_bond_interest)
                # 向FirstCurrentList列表添加T+0可用金额值
                #print(len(self.FirstCurrentList))
                self.FirstCurrentList.pop(2)
                self.FirstCurrentList.insert(2, T0Balance)
                # T+1可用金额=期初T+1可用金额-委托数量*100*(1+交易费率)-委托数量*100(委托价格/365+1)
                T1Balance = self.FirstCurrentList[3] -en_entrust_amount*100*(1+en_bond_interest)-en_entrust_amount*100*(float(en_entrust_price)/365+1)
                # 向FirstAssetList列表添加T1可用金额值
                self.FirstCurrentList.pop(3)
                self.FirstCurrentList.insert(3, T1Balance)
                # 冻结金额=期初冻结金额+委托数量*100(委托价格/365+1)
                frozenBalance = self.InitCurrentList[4]+en_entrust_amount*100*(float(en_entrust_price)/365+1)
                # 向FirstCurrentList列表添加冻结金额值
                self.FirstCurrentList.pop(4)
                self.FirstCurrentList.insert(4, frozenBalance)
                # 解冻金额=期初解冻数量
                unfrozenBalance = self.InitCurrentList[5]
                # 向FirstCurrentList列表添加解冻金额的值
                self.FirstCurrentList.pop(5)
                self.FirstCurrentList.insert(5, unfrozenBalance)
                # 资金变化赋值
                for i, j in (enumerate(self.FirstCurrentList)):
                    # print(i,j)
                    newItem = QTableWidgetItem('%.2f' % j)
                    self.tableWidgetCurrent.setItem(2, i +8, newItem)
                '''债券持仓不变'''
                for i in range(len(self.InitStockList)):
                    newItem = QTableWidgetItem('%.2f' % int(self.InitStockList[i]))
                    self.tableWidgetStock.setItem(2, i + 8, newItem)
                '''标准券持仓变化'''
                for i in range(len(self.FirstStandardList)):
                    newItem = QTableWidgetItem('%d' % int(self.FirstStandardList[i]))
                    self.tableWidgetStandard.setItem(2, i + 8, newItem)
        
    
    @pyqtSlot()
    def on_btnExport_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        QMessageBox.information(self, '提示', '抱歉，该功能尚未开通！')
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = CallBondHG()
    ui.show()
    sys.exit(app.exec_())
