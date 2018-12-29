#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年12月26日
@author: Yiluo
@file: CallBondHG
@description:债券买卖计算
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem, \
    QAbstractItemView
from Ui_EnableTest import Ui_EnableTool
from demo import  NotificationWindow
from Log import Loggers
import time
from CallBaseTitleWidget import BaseTitleWidget

__Author__ = """
By: Yiluo 
QQ: 786129166
Email: 786129166@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Yiluo'
__Version__ = 1.0

class CallEnableTool(QMainWindow, Ui_EnableTool):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(CallEnableTool, self).__init__(parent)
        self.setupUi(self)
        self.log = Loggers(level='debug')
        self.ds = NotificationWindow()
        self.initUI()

    def initUI(self):
        
        #设置表格不可以编辑
        self.tableWidgetAsset.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidgetCurrent.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidgetStock.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 获取初始资产数据
        self.InitAssetList = []
        # 获取初始资金数据
        self.InitCurrentList = []
        # 获取初始证券数据
        self.InitStockList = []
        for i in range(7, 15):
            demo = self.tableWidgetAsset.item(0, i).text()
            self.InitAssetList.append(float(demo))
        for j in range(7, 12):
            demo = self.tableWidgetCurrent.item(0, j).text()
            self.InitCurrentList.append(float(demo))
        for k in range(7, 13):
            demo = self.tableWidgetStock.item(0, k).text()
            self.InitStockList.append(float(demo))

        # 获取计算后的资产数据
        self.FirstAssetList = self.InitAssetList[:]
        # 获取计算后的资金数据
        self.FirstCurrentList = self.InitCurrentList[:]
        # 获取计算后的证券数据
        self.FirstStockList = self.InitStockList[:]
        # 声明计算函数
        self.btnCalculate.clicked.connect(self.Calculate)
        # 声明系统日初始化函数
        self.btnInit.clicked.connect(self.InitBond)
        # 声明清空函数
        self.btnClear.clicked.connect(self.ClearEmpty)
        self.tableWidgetAsset.horizontalHeader().setSectionResizeMode(1)#列宽设置
        self.tableWidgetAsset.verticalHeader().setSectionResizeMode(1)#行高设置          
        self.tableWidgetAsset.verticalHeader().setStretchLastSection(True); #充满行高         
        self.resizeHeight(self.tableWidgetCurrent)
        self.resizeHeight(self.tableWidgetStock)
        
  
    def resizeHeight(self, table):
        table.horizontalHeader().setSectionResizeMode(2)#列宽设置

        table.horizontalHeader().setStretchLastSection(True); #充满列宽    

        table.verticalHeader().setSectionResizeMode(1)#行高设置          

        table.verticalHeader().setStretchLastSection(True); #充满行高   

    '''定义清空函数'''

    def ClearEmpty(self):
        '''清空资产变化'''
        for i in range(1, 3):
            for j in range(1, 15):
                newItem = QTableWidgetItem('')
                self.tableWidgetAsset.setItem(i, j, newItem)
        '''清空资金变化'''
        for i in range(1, 3):
            for j in range(1, 12):
                newItem = QTableWidgetItem('')
                self.tableWidgetCurrent.setItem(i, j, newItem)
        '''清空证券变化'''
        for i in range(1, 3):
            for j in range(1, 13):
                newItem = QTableWidgetItem('')
                self.tableWidgetStock.setItem(i, j, newItem)
        # 获取计算后的资产数据
        self.FirstAssetList = self.InitAssetList[:]
        # 获取计算后的资金数据
        self.FirstCurrentList = self.InitCurrentList[:]
        # 获取计算后的证券数据
        self.FirstStockList = self.InitStockList[:]
        self.log.logger.info('数据开始清除，请稍等...')
        time.sleep(1)
        self.log.logger.info('数据清除完成，请开始操作!')

    '''定义日初始化函数'''

    def InitBond(self):
        # 创建一个宽度为8，高度为4的数组
        self.listStockFile = [([0] * 9) for i in range(4)]
        # 获得业务品种
        en_stock_type = self.c_stock_type.currentText()
        newItem = QTableWidgetItem('%s' % en_stock_type)
        self.tableWidgetAsset.setItem(2, 1, newItem)
        newItem = QTableWidgetItem('%s' % en_stock_type)
        self.tableWidgetCurrent.setItem(2, 1, newItem)
        newItem = QTableWidgetItem('%s' % en_stock_type)
        self.tableWidgetStock.setItem(2, 1, newItem)
        # 获得委托方向
        en_entrust_direction = self.c_entrust_direction.currentText()
        newItem = QTableWidgetItem('%s' % en_entrust_direction)
        self.tableWidgetAsset.setItem(2, 2, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_direction)
        self.tableWidgetCurrent.setItem(2, 2, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_direction)
        self.tableWidgetStock.setItem(2, 2, newItem)
        # 获得委托状态
        en_entrust_status = self.c_entrust_status.currentText()
        newItem = QTableWidgetItem('%s' % en_entrust_status)
        self.tableWidgetAsset.setItem(2, 6, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_status)
        self.tableWidgetCurrent.setItem(2, 6, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_status)
        self.tableWidgetStock.setItem(2, 6, newItem)
        # 获得委托数量
        en_entrust_amount = float(self.c_entrust_amount.text())
        newItem = QTableWidgetItem('%d' % en_entrust_amount)
        self.tableWidgetAsset.setItem(2, 3, newItem)
        newItem = QTableWidgetItem('%d' % en_entrust_amount)
        self.tableWidgetCurrent.setItem(2, 3, newItem)
        newItem = QTableWidgetItem('%d' % en_entrust_amount)
        self.tableWidgetStock.setItem(2, 3, newItem)
        # 获得委托价格
        en_entrust_price = float(self.c_entrust_price.text())
        newItem = QTableWidgetItem('%.2f' % en_entrust_price)
        self.tableWidgetAsset.setItem(2, 4, newItem)
        newItem = QTableWidgetItem('%.2f' % en_entrust_price)
        self.tableWidgetCurrent.setItem(2, 4, newItem)
        newItem = QTableWidgetItem('%.2f' % en_entrust_price)
        self.tableWidgetStock.setItem(2, 4, newItem)
        # 获得百元债券利息
        en_bond_interest = float(self.c_bond_interest.text())
        newItem = QTableWidgetItem('%.2f' % en_bond_interest)
        self.tableWidgetAsset.setItem(2, 5, newItem)
        newItem = QTableWidgetItem('%.2f' % en_bond_interest)
        self.tableWidgetCurrent.setItem(2, 5, newItem)
        newItem = QTableWidgetItem('%.2f' % en_bond_interest)
        self.tableWidgetStock.setItem(2, 5, newItem)

        if en_entrust_direction == '买入':
            if en_entrust_status == '已报':
                '''资产不变'''
                for i in range(8):
                    newItem = QTableWidgetItem('%.2f' % int(self.InitAssetList[i]))
                    self.tableWidgetAsset.setItem(2, i + 7, newItem)
                '''资金不变'''
                for i in range(5):
                    newItem = QTableWidgetItem('%.2f' % int(self.InitCurrentList[i]))
                    self.tableWidgetCurrent.setItem(2, i + 7, newItem)
                '''证券不变'''
                for i in range(6):
                    newItem = QTableWidgetItem('%.2f' % int(self.InitStockList[i]))
                    self.tableWidgetStock.setItem(2, i + 7, newItem)
            elif en_entrust_status == '已成':
                '''资产变化'''
                for i in range(8):
                    newItem = QTableWidgetItem('%.2f' % int(self.FirstAssetList[i]))
                    self.tableWidgetAsset.setItem(2, i + 7, newItem)
                '''资金变化'''
                for i in range(4):
                    newItem = QTableWidgetItem('%.2f' % self.FirstCurrentList[i])
                    self.tableWidgetCurrent.setItem(2, i + 7, newItem)
                    # 冻结置为0
                    newItem = QTableWidgetItem('0.000')
                    self.tableWidgetCurrent.setItem(2, 11, newItem)
                '''证券日初始化'''
                for i in range(6):
                    newItem = QTableWidgetItem('%.2f' % int(self.FirstStockList[i]))
                    self.tableWidgetStock.setItem(2, i + 7, newItem)
        elif en_entrust_direction == '卖出':
            if en_entrust_status == '已报':
                '''资产变化'''
                for i in range(8):
                    newItem = QTableWidgetItem('%.2f' % int(self.FirstAssetList[i]))
                    self.tableWidgetAsset.setItem(2, i + 7, newItem)
                '''资金变化'''
                for i in range(5):
                    newItem = QTableWidgetItem('%.2f' % self.FirstCurrentList[i])
                    self.tableWidgetCurrent.setItem(2, i + 7, newItem)
                '''证券变化'''
                for i in range(6):
                    newItem = QTableWidgetItem('%.2f' % int(self.FirstStockList[i]))
                    self.tableWidgetStock.setItem(2, i + 7, newItem)
            elif en_entrust_status == '已成':
                '''资产变化'''
                for i in range(8):
                    newItem = QTableWidgetItem('%.2f' % int(self.FirstAssetList[i]))
                    self.tableWidgetAsset.setItem(2, i + 7, newItem)
                '''资金变化'''
                for i in range(3):
                    newItem = QTableWidgetItem('%.2f' % self.FirstCurrentList[i])
                    self.tableWidgetCurrent.setItem(2, i + 7, newItem)
                    newItem = QTableWidgetItem('0.000')
                    self.tableWidgetCurrent.setItem(2, 10, newItem)
                    newItem = QTableWidgetItem('0.000')
                    self.tableWidgetCurrent.setItem(2, 11, newItem)
                '''证券变化'''
                for i in range(6):
                    newItem = QTableWidgetItem('%.2f' % int(self.FirstStockList[i]))
                    self.tableWidgetStock.setItem(2, i + 7, newItem)


    '''定义计算函数'''

    def Calculate(self):
        # 获得业务品种
        en_stock_type = self.c_stock_type.currentText()
        newItem = QTableWidgetItem('%s' % en_stock_type)
        self.tableWidgetAsset.setItem(1, 1, newItem)
        newItem = QTableWidgetItem('%s' % en_stock_type)
        self.tableWidgetCurrent.setItem(1, 1, newItem)
        newItem = QTableWidgetItem('%s' % en_stock_type)
        self.tableWidgetStock.setItem(1, 1, newItem)
        # 获得委托方向
        en_entrust_direction = self.c_entrust_direction.currentText()
        newItem = QTableWidgetItem('%s' % en_entrust_direction)
        self.tableWidgetAsset.setItem(1, 2, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_direction)
        self.tableWidgetCurrent.setItem(1, 2, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_direction)
        self.tableWidgetStock.setItem(1, 2, newItem)
        # 获得委托状态
        en_entrust_status = self.c_entrust_status.currentText()
        newItem = QTableWidgetItem('%s' % en_entrust_status)
        self.tableWidgetAsset.setItem(1, 6, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_status)
        self.tableWidgetCurrent.setItem(1, 6, newItem)
        newItem = QTableWidgetItem('%s' % en_entrust_status)
        self.tableWidgetStock.setItem(1, 6, newItem)
        # 获得委托数量
        en_entrust_amount = float(self.c_entrust_amount.text())
        newItem = QTableWidgetItem('%d' % en_entrust_amount)
        self.tableWidgetAsset.setItem(1, 3, newItem)
        newItem = QTableWidgetItem('%d' % en_entrust_amount)
        self.tableWidgetCurrent.setItem(1, 3, newItem)
        newItem = QTableWidgetItem('%d' % en_entrust_amount)
        self.tableWidgetStock.setItem(1, 3, newItem)
        # 获得委托价格
        en_entrust_price = float(self.c_entrust_price.text())
        newItem = QTableWidgetItem('%.2f' % en_entrust_price)
        self.tableWidgetAsset.setItem(1, 4, newItem)
        newItem = QTableWidgetItem('%.2f' % en_entrust_price)
        self.tableWidgetCurrent.setItem(1, 4, newItem)
        newItem = QTableWidgetItem('%.2f' % en_entrust_price)
        self.tableWidgetStock.setItem(1, 4, newItem)
        # 获得百元债券利息
        en_bond_interest = float(self.c_bond_interest.text())
        newItem = QTableWidgetItem('%.2f' % en_bond_interest)
        self.tableWidgetAsset.setItem(1, 5, newItem)
        newItem = QTableWidgetItem('%.2f' % en_bond_interest)
        self.tableWidgetCurrent.setItem(1, 5, newItem)
        newItem = QTableWidgetItem('%.2f' % en_bond_interest)
        self.tableWidgetStock.setItem(1, 5, newItem)
        #日志入口
        log = self.log.logger
        if en_stock_type == '债券':
            if en_entrust_direction == '买入':
                if en_entrust_status == '已报':
                    log.info('债券买入已报，资产变化计算开始-->>:')
                    '''资产不变'''
                    for i in range(8):
                        newItem = QTableWidgetItem('%.2f' % int(self.InitAssetList[i]))
                        self.tableWidgetAsset.setItem(1, i + 7, newItem)
                    log.info('债券买入已报，资产不变。')
                    log.info('债券买入已报，资产变化计算结束--<<.')
                    '''资金变化'''
                    log.info('债券买入已报，资金变化计算开始-->>:')
                    # 当前现金余额=期初当前现金余额
                    cashBalance = self.FirstCurrentList[0]
                    # 向FirstCurrentList列表添加现金资产值
                    self.FirstCurrentList.pop(0)
                    self.FirstCurrentList.insert(0, cashBalance)
                    log.info('现金余额=期初现金余额+当天业务处理资金变化部分＋手工调整部分')
                    # T+0可用金额=期初T+0可用金额-成交数量*（成交价格+对应债券的百元应收利息）
                    T0Balance = self.FirstCurrentList[1] - en_entrust_amount * (en_entrust_price + en_bond_interest)
                    # 向FirstCurrentList列表添加T+0可用金额值
                    log.info('T+0可用金额= 当前金额-冻结金额+解冻金额+Min{T+1变化,0}')
                    self.FirstCurrentList.pop(1)
                    self.FirstCurrentList.insert(1, T0Balance)
                    # T+1可用金额=期初T+1可用金额-成交数量*（成交价格+对应债券的百元应收利息）
                    T1Balance = self.FirstCurrentList[2] - en_entrust_amount * (en_entrust_price + en_bond_interest)
                    # 向FirstAssetList列表添加应收值
                    self.FirstCurrentList.pop(2)
                    self.FirstCurrentList.insert(2, T1Balance)
                    log.info('T+1可用金额=当前金额-冻结金额+解冻金额-T+1变化')
                    # 冻结金额表示产品债券买卖实际交易成功后日终交收后实际需增加的金额
                    frozenBalance = self.FirstCurrentList[3]
                    # 向FirstCurrentList列表添加应付值
                    self.FirstCurrentList.pop(3)
                    self.FirstCurrentList.insert(3, frozenBalance)
                    log.info('冻结金额=债券买入成功后实际需要减少的金额，因为未成交，故无冻结')
                    # 解冻金额表示资金流出，但是未成交 无需进行解冻
                    unfrozenBalance = self.FirstCurrentList[4]
                    # 向FirstCurrentList列表添加解冻的值
                    self.FirstCurrentList.pop(4)
                    self.FirstCurrentList.insert(4, unfrozenBalance)
                    log.info('解冻金额=债券卖出成功后实际需要增加的金额')
                    # 资金变化赋值
                    for i, j in (enumerate(self.FirstCurrentList)):
                        # print(i,j)
                        newItem = QTableWidgetItem('%.2f' % j)
                        self.tableWidgetCurrent.setItem(1, i + 7, newItem)
                    log.info('债券买入已报，资金变化计算结束--<<.')
                    
                    log.info('债券买入已报，证券变化计算开始-->>.')
                    '''持仓变化'''
                    log.info('债券买入已报，证券不变化.')
                    for i in range(6):
                        newItem = QTableWidgetItem('%d' % int(self.InitAssetList[i]))
                        self.tableWidgetStock.setItem(1, i + 7, newItem)
                        
                    log.info('债券买入已报，证券变化计算结束--<<.')
                        
                else:
                    log.info('债券买入已成，资产变化计算开始-->>:')
                    '''资产变化'''
                    # 现金资产=当前现金余额-成交数量*（成交价格+对应债券的百元应收利息）
                    currentAsset = self.FirstAssetList[0] - en_entrust_amount * (en_entrust_price + en_bond_interest)
                    # 向FirstAssetList列表添加现金资产值
                    self.FirstAssetList.pop(0)
                    self.FirstAssetList.insert(0, currentAsset)
                    log.info('现金资产=期初现金余额-成交数量*（成交价格+对应债券的百元应收利息）')
                    # 债券资产=成交价格*成交数量
                    stockAsset = self.FirstAssetList[1] + en_entrust_amount * en_bond_interest
                    # 向FirstAssetList列表添加证券资产值
                    self.FirstAssetList.pop(1)
                    self.FirstAssetList.insert(1, stockAsset)
                    log.info('债券资产=期初资产+成交价格*成交数量')
                    # 应收=当前持仓数量*百元债券利息
                    acceptAsset = self.FirstAssetList[2] + en_entrust_amount * en_bond_interest
                    # 向FirstAssetList列表添加应收值
                    self.FirstAssetList.pop(2)
                    self.FirstAssetList.insert(2, acceptAsset)
                    log.info('应收=期初应收+当前持仓数量*百元债券利息')
                    # 应付=0
                    giveAsset = self.FirstAssetList[3] + self.InitAssetList[3]
                    # 向FirstAssetList列表添加应付值
                    self.FirstAssetList.pop(3)
                    self.FirstAssetList.insert(3, giveAsset)
                    log.info('应付=应付科目余额的合计')
                    # 总资产=净值+应付
                    totalAsset = self.FirstAssetList[4]
                    # 向FirstAssetList列表添加总净值的值
                    self.FirstAssetList.pop(4)
                    self.FirstAssetList.insert(4, totalAsset)
                    log.info('总资产=当前资金余额+应收+债券资产')
                    # 净值=现金资产+证券资产+应收-应付
                    valueAsset = currentAsset + stockAsset + acceptAsset - giveAsset
                    # 向FirstAssetList列表添加净值的值
                    self.FirstAssetList.pop(5)
                    self.FirstAssetList.insert(5, valueAsset)
                    log.info('净值=当前现金余额 - 应付 + 应收  + 债券资产 ')
                    # 产品份额：即产品成立时的份额，开放期会有申购或者赎回
                    productAmount = int(self.InitAssetList[6])
                    # 向FirstAssetList列表添加产品份额值
                    self.FirstAssetList.pop(6)
                    self.FirstAssetList.insert(6, productAmount)
                    log.info('产品份额=即产品成立时的份额，开放期会有申购或者赎回')
                    # 单位净值=净值/产品份额
                    perValueAsset = valueAsset / productAmount
                    # 向FirstAssetList列表添加单位净值的值
                    self.FirstAssetList.pop(7)
                    self.FirstAssetList.insert(7, perValueAsset)
                    log.info('单位净值=净值/产品份额')
                    # 资产变化赋值
                    for i, j in (enumerate(self.FirstAssetList)):
                        # print(i,j)
                        newItem = QTableWidgetItem('%.2f' % j)
                        self.tableWidgetAsset.setItem(1, i + 7, newItem)
                    log.info('债券买入已成，资产变化计算结束--<<')
                    
                    log.info('债券买入已成，资金变化计算开始-->>:')
                    '''资金变化'''
                    
                    # 当前现金余额=期初当前现金余额-成交数量*（成交价格+对应债券的百元应收利息）
                    cashBalance = self.FirstCurrentList[0] - en_entrust_amount * (en_entrust_price + en_bond_interest)
                    # 向FirstCurrentList列表添加现金资产值
                    self.FirstCurrentList.pop(0)
                    self.FirstCurrentList.insert(0, cashBalance)
                    log.info('当前现金余额=期初当前现金余额-成交数量*（成交价格+对应债券的百元应收利息）')
                    
                    # T+0可用金额=期初T+0可用金额-成交数量*（成交价格+对应债券的百元应收利息）
                    T0Balance = self.FirstCurrentList[1] - en_entrust_amount * (en_entrust_price + en_bond_interest)
                    # 向FirstCurrentList列表添加T+0可用金额值
                    self.FirstCurrentList.pop(1)
                    self.FirstCurrentList.insert(1, T0Balance)
                    log.info('T+0可用金额= 当前金额-冻结金额+解冻金额+Min{T+1变化,0}')
                    
                    # T+1可用金额=期初T+1可用金额-成交数量*（成交价格+对应债券的百元应收利息）
                    T1Balance = self.FirstCurrentList[2] - en_entrust_amount * (en_entrust_price + en_bond_interest)
                    # 向FirstAssetList列表添加应收值
                    self.FirstCurrentList.pop(2)
                    self.FirstCurrentList.insert(2, T1Balance)
                    log.info('T+1可用金额=当前金额-冻结金额+解冻金额-T+1变化')
                    
                    # 冻结金额表示产品债券买卖实际交易成功后日终交收后实际需增加的金额
                    frozenBalance = self.FirstCurrentList[3]
                    # 向FirstCurrentList列表添加应付值
                    self.FirstCurrentList.pop(3)
                    self.FirstCurrentList.insert(3, frozenBalance)
                    log.info('冻结金额=债券买入成功后冻结取消')
                    
                    # 解冻金额=成交数量*（成交价格+对应债券的百元应收利息）
                    unfrozenBalance = self.FirstCurrentList[4] + en_entrust_amount * (
                        en_entrust_price + en_bond_interest)
                    # 向FirstCurrentList列表添加总净值的值
                    self.FirstCurrentList.pop(4)
                    self.FirstCurrentList.insert(4, unfrozenBalance)
                    log.info('解冻金额=成交数量*（成交价格+对应债券的百元应收利息）')
                    
                    # 资金变化赋值
                    for i, j in (enumerate(self.FirstCurrentList)):
                        # print(i,j)
                        newItem = QTableWidgetItem('%.2f' % j)
                        self.tableWidgetCurrent.setItem(1, i + 7, newItem)
                    log.info('债券买入已成，资金变化计算结束--<<')
                    
                    log.info('债券买入已成，证券变化计算开始-->>:')
                    '''证券变化'''
                    # 当前持仓数量=期初持仓数量+成交数量
                    currentAmount = self.FirstStockList[0] + en_entrust_amount
                    # 向FirstStockList列表添加当前持仓数量值
                    self.FirstStockList.pop(0)
                    self.FirstStockList.insert(0, currentAmount)
                    log.info('当前持仓数量=期初持仓数量+成交数量')
                    
                    # 可用数量=期初可用数量+成交数量
                    enableAmmount = self.FirstStockList[1] + en_entrust_amount
                    # 向FirstStockList列表添加T+0可用数量值
                    #print(len(self.FirstStockList))
                    self.FirstStockList.pop(1)
                    self.FirstStockList.insert(1, enableAmmount)
                    log.info('可以数量=当前数量-冻结数量+解冻数量+min{T+1变化,0}')
                    
                    # 债券买卖属于T+0交易，当天买入的债券当天可以卖出。不存在冻结数量，即都为0
                    frozenAmount = self.FirstStockList[2]
                    # 向FirstStockList列表添加冻结数量值
                    self.FirstStockList.pop(2)
                    self.FirstStockList.insert(2, frozenAmount)
                    
                    # 债券买卖属于T+0交易，当天买入的债券当天可以卖出。不存在解冻数量，即都为0
                    unfrozenAmount = self.FirstStockList[3]
                    # 向FirstStockList列表添加解冻的值
                    self.FirstStockList.pop(3)
                    self.FirstStockList.insert(3, unfrozenAmount)
                    log.info('冻结/解冻数量=债券买卖属于T+0交易，当天买入的债券当天可以卖出。不存在冻结和解冻数量，即冻结和解冻都为0')
                    
                    # 成本价 = 成交价格
                    # QMessageBox.information(self, '123', '%d' % self.FirstStockList[4])
                    currentInvestPrice = self.FirstStockList[4] + en_entrust_price
                    # 向FirstStockList列表添加成本价的值
                    self.FirstStockList.pop(4)
                    self.FirstStockList.insert(4, currentInvestPrice)
                    log.info('成本价=成本/（当前数量+卖出数量）')
                    
                    # 成本 = 成交价格*成交数量
                    currentInvest = self.FirstStockList[5] + en_entrust_price * en_entrust_amount
                    # 向FirstStockList列表添加成本的值
                    self.FirstStockList.pop(5)
                    self.FirstStockList.insert(5, currentInvest)
                    log.info('成本 =当前数量 *　成本价')
                    # 资金变化赋值
                    for i, j in (enumerate(self.FirstStockList)):
                        # print(i,j)
                        newItem = QTableWidgetItem('%d' % j)
                        self.tableWidgetStock.setItem(1, i + 7, newItem)
                    log.info('债券买入已成，资金变化计算结束--<<.')
                        
            elif en_entrust_direction == '卖出':
                if en_entrust_status == '已报':
                    '''资产变化'''
                    # 卖出已报，资产不变化
                    for i in range(8):
                        newItem = QTableWidgetItem('%.2f' % int(self.InitAssetList[i]))
                        self.tableWidgetAsset.setItem(1, i + 7, newItem)
                    '''资金变化'''
                    # 卖出已报，资金不变化
                    for i in range(5):
                        newItem = QTableWidgetItem('%.2f' % int(self.InitCurrentList[i]))
                        self.tableWidgetCurrent.setItem(1, i + 7, newItem)
                    '''证券变化'''
                    # 卖出已报，证券不变化
                    for i in range(6):
                        newItem = QTableWidgetItem('%d' % int(self.InitStockList[i]))
                        self.tableWidgetStock.setItem(1, i + 7, newItem)
                        
                else:
                    '''资产变化'''
                    # 卖出已成，资产不变化
                    for i in range(8):
                        newItem = QTableWidgetItem('%.2f' % int(self.InitAssetList[i]))
                        self.tableWidgetAsset.setItem(1, i + 7, newItem)
                    '''资金变化'''
                    # 当前现金余额=期初当前现金余额+成交数量*（成交价格+对应债券的百元应收利息）
                    cashBalance = self.FirstCurrentList[0] + en_entrust_amount * (en_entrust_price + en_bond_interest)
                    # 向FirstCurrentList列表添加现金资产值
                    self.FirstCurrentList.pop(0)
                    self.FirstCurrentList.insert(0, cashBalance)
                    # T+0可用金额=期初T+0可用金额+成交数量*（成交价格+对应债券的百元应收利息）
                    T0Balance = self.FirstCurrentList[1] + en_entrust_amount * (en_entrust_price + en_bond_interest)
                    # 向FirstCurrentList列表添加T+0可用金额值
                    #print(len(self.FirstCurrentList))
                    self.FirstCurrentList.pop(1)
                    self.FirstCurrentList.insert(1, T0Balance)
                    # T+1可用金额=期初T+1可用金额+成交数量*（成交价格+对应债券的百元应收利息）
                    T1Balance = self.FirstCurrentList[2] + en_entrust_amount * (en_entrust_price + en_bond_interest)
                    # 向FirstAssetList列表添加应收值
                    self.FirstCurrentList.pop(2)
                    self.FirstCurrentList.insert(2, T1Balance)
                    # 冻结金额表示产品债券买卖实际交易成功后日终交收后实际需增加的金额
                    # 冻结金额 = 期初冻结金额+成交数量*（成交价格+对应债券的百元应收利息）
                    frozenBalance = self.FirstCurrentList[3] + en_entrust_amount * (en_entrust_price + en_bond_interest)
                    # 向FirstCurrentList列表添加应付值
                    self.FirstCurrentList.pop(3)
                    self.FirstCurrentList.insert(3, frozenBalance)
                    # 解冻金额表示产品债券买卖实际交易成功后日终交收后实际需减少的金额，即买入已成的交易。
                    unfrozenBalance = self.FirstCurrentList[4]
                    # 向FirstCurrentList列表添加总净值的值
                    self.FirstCurrentList.pop(4)
                    self.FirstCurrentList.insert(4, unfrozenBalance)
                    # print('长度为{0}'.format(len(self.FirstAssetList)))
                    # 资金变化赋值
                    for i, j in (enumerate(self.FirstCurrentList)):
                        # print(i,j)
                        newItem = QTableWidgetItem('%.2f' % j)
                        self.tableWidgetCurrent.setItem(1, i + 7, newItem)
                    '''证券变化'''
                    # 当前持仓数量=期初持仓数量-成交数量
                    currentAmount = self.FirstStockList[0] - en_entrust_amount
                    # 向FirstStockList列表添加当前持仓数量值
                    self.FirstStockList.pop(0)
                    self.FirstStockList.insert(0, currentAmount)
                    # 可用数量=期初可用数量-成交数量
                    enableAmmount = self.FirstStockList[1] - en_entrust_amount
                    # 向FirstStockList列表添加T+0可用数量值
                    #print(len(self.FirstStockList))
                    self.FirstStockList.pop(1)
                    self.FirstStockList.insert(1, enableAmmount)
                    # 债券买卖属于T+0交易，当天买入的债券当天可以卖出。不存在冻结数量，即都为0
                    frozenAmount = self.FirstStockList[2]
                    # 向FirstStockList列表添加冻结数量值
                    self.FirstStockList.pop(2)
                    self.FirstStockList.insert(2, frozenAmount)
                    # 债券买卖属于T+0交易，当天买入的债券当天可以卖出。不存在解冻数量，即都为0
                    unfrozenAmount = self.FirstStockList[3]
                    # 向FirstStockList列表添加总净值的值
                    self.FirstStockList.pop(3)
                    self.FirstStockList.insert(3, unfrozenAmount)
                    # 成本价 = 成交价格
                    # QMessageBox.information(self, '123', '%d' % self.FirstStockList[4])
                    currentInvestPrice = self.FirstStockList[4] + en_entrust_price
                    # 向FirstStockList列表添加成本价的值
                    self.FirstStockList.pop(4)
                    self.FirstStockList.insert(4, currentInvestPrice)
                    # 成本 = 期初成本-成交价格*成交数量
                    currentInvest = self.FirstStockList[5] - en_entrust_price * en_entrust_amount
                    # 向FirstStockList列表添加成本的值
                    self.FirstStockList.pop(5)
                    self.FirstStockList.insert(5, currentInvest)
                    # print('长度为{0}'.format(len(self.FirstAssetList)))
                    # 证券变化赋值
                    for i, j in (enumerate(self.FirstStockList)):
                        # print(i,j)
                        newItem = QTableWidgetItem('%d' % j)
                        self.tableWidgetStock.setItem(1, i + 7, newItem)



    @pyqtSlot(int, int)
    def on_tableWidgetAsset_cellEntered(self, row, column):
        '''资产变化表格鼠标滑过弹框提示'''
        # 获得委托方向
        en_entrust_direction = self.c_entrust_direction.currentText()
        # 获得委托状态
        en_entrust_status = self.c_entrust_status.currentText()
        if row == 1:
            if en_entrust_direction == '买入':
                if en_entrust_status == '已报':
                    self.dd = BaseTitleWidget()
                    self.dd.setTitle('123')
                    self.dd.windowMoved.connect(self.dd.doMoveWindow)
                    self.dd.show()
                    #self.ds.success('提示', '买入已报，资产不变化')
        

    @pyqtSlot(int, int)
    def on_tableWidgetAsset_cellDoubleClicked(self, row, column):
        '''资产变化表格双击弹出提示'''
        
        # 获得委托方向
        en_entrust_direction = self.c_entrust_direction.currentText()
        # 获得委托状态
        en_entrust_status = self.c_entrust_status.currentText()
        if row == 1:
            if en_entrust_direction == '买入':
                if en_entrust_status == '已报':
                    #QMessageBox.about(self, '提示', '买入已报，资产不变化')
                    
                    self.ds.success('提示', '买入已报，资产不变化')
                    
                elif en_entrust_status == '已成':
                    if column == 6:
                        QMessageBox.about(self, '提示', '现金资产=当前现金余额-成交数量*（成交价格+对应债券的百元应收利息）')
                    elif column == 7:
                        QMessageBox.about(self, '提示', '证券资产=成交价格*成交数量')
                    elif column == 8:
                        QMessageBox.about(self, '提示', '应收=当前持仓数量*百元债券利息')
                    elif column == 9:
                        QMessageBox.about(self, '提示', '应付是资金流出')
                    elif column == 10:
                        QMessageBox.about(self, '提示', '总资产=净值+应付')
                    elif column == 11:
                        QMessageBox.about(self, '提示', '净值=现金资产+证券资产+应收-应付')
                    elif column == 12:
                        QMessageBox.about(self, '提示', '产品份额：即产品成立时的份额，开放期会有申购或者赎回')
                    elif column == 13:
                        QMessageBox.about(self, '提示', '单位净值=净值/产品份额')
            elif en_entrust_direction == '卖出':
                if en_entrust_status == '已报':
                    # 设置表格整行选中
                    self.tableWidgetAsset.setSelectionBehavior(QAbstractItemView.SelectRows)
                    QMessageBox.about(self, '提示', '卖出已报，资产不变化')
                else:
                    QMessageBox.about(self, '提示', '卖出已成，资产不变化')

    @pyqtSlot(int, int)
    def on_tableWidgetCurrent_cellDoubleClicked(self, row, column):
        """资金变化表格双击弹出提示"""
        # 获得委托方向
        en_entrust_direction = self.c_entrust_direction.currentText()
        # 获得委托状态
        en_entrust_status = self.c_entrust_status.currentText()
        if row == 1:
            if en_entrust_direction == '买入':
                if en_entrust_status == '已报':
                    '''这里有问题'''
                    QMessageBox.about(self, '提示', '资产没有变化')
                elif en_entrust_status == '已成':
                    if column == 6:
                        QMessageBox.about(self, '当前现金余额', '当前现金余额=期初当前现金余额-成交数量*（成交价格+对应债券的百元应收利息）')
                    elif column == 7:
                        QMessageBox.about(self, 'T+0可用金额', 'T+0可用金额=期初T+0可用金额-成交数量*（成交价格+对应债券的百元应收利息）')
                    elif column == 8:
                        QMessageBox.about(self, 'T+1可用金额', 'T+1可用金额=期初T+1可用金额-成交数量*（成交价格+对应债券的百元应收利息）')
                    elif column == 9:
                        QMessageBox.about(self, '冻结金额', '冻结金额表示产品债券买卖实际交易成功后日终交收后实际需增加的金额')
                    elif column == 10:
                        QMessageBox.about(self, '解冻金额', '解冻金额=成交数量*（成交价格+对应债券的百元应收利息）')
            elif en_entrust_direction == '卖出':
                if en_entrust_status == '已报':
                    QMessageBox.about(self, '提示', '卖出已报，资金不变化')
                elif en_entrust_status == '已成':
                    if column == 6:
                        QMessageBox.about(self, '当前现余额', '当前现金余额=期初当前现金余额+成交数量*（成交价格+对应债券的百元应收利息）')
                    elif column == 7:
                        QMessageBox.about(self, 'T+0可用金额', 'T+0可用金额=期初T+0可用金额+成交数量*（成交价格+对应债券的百元应收利息）')
                    elif column == 8:
                        QMessageBox.about(self, 'T+1可用金额', 'T+1可用金额=期初T+1可用金额+成交数量*（成交价格+对应债券的百元应收利息）')
                    elif column == 9:
                        QMessageBox.about(self, '冻结金额', '冻结金额 = 期初冻结金额+成交数量*（成交价格+对应债券的百元应收利息）')
                    elif column == 10:
                        QMessageBox.about(self, '解冻金额', '解冻金额表示产品债券买卖实际交易成功后日终交收后实际需减少的金额，卖出不影响解冻金额')

    @pyqtSlot(int, int)
    def on_tableWidgetStock_cellDoubleClicked(self, row, column):
        """证券变化表格双击弹出提示"""
        # 获得委托方向
        en_entrust_direction = self.c_entrust_direction.currentText()
        # 获得委托状态
        en_entrust_status = self.c_entrust_status.currentText()
        if row == 1:
            if en_entrust_direction == '买入':
                if en_entrust_status == '已报':
                    QMessageBox.about(self, '提示', '买入已报，证券不变化')
                elif en_entrust_status == '已成':
                    if column == 6:
                        QMessageBox.about(self, '当前持仓数量', '当前持仓数量=期初持仓数量+成交数量')
                    elif column == 7:
                        QMessageBox.about(self, '可用数量', '可用数量=期初可用数量+成交数量')
                    elif column == 8:
                        QMessageBox.about(self, '冻结数量', '债券买卖属于T+0交易，当天买入的债券当天可以卖出。不存在冻结数量，即都为0')
                    elif column == 9:
                        QMessageBox.about(self, '解冻数量', '债券买卖属于T+0交易，当天买入的债券当天可以卖出。不存在解冻数量，即都为0')
                    elif column == 10:
                        QMessageBox.about(self, '成本价', '成本价 = 成交价格')
                    elif column == 11:
                        QMessageBox.about(self, '成本', '成本=成交价格*成交数量')
            elif en_entrust_direction == '卖出':
                if en_entrust_status == '已报':
                    QMessageBox.about(self, '提示', '卖出已报，证券不变化')
                elif en_entrust_status == '已成':
                    if column == 6:
                        QMessageBox.about(self, '当前持仓数量', '当前持仓数量=期初持仓数量-成交数量')
                    elif column == 7:
                        QMessageBox.about(self, '可用数量', '可用数量=期初可用数量-成交数量')
                    elif column == 8:
                        QMessageBox.about(self, '冻结数量', '债券买卖属于T+0交易，当天买入的债券当天可以卖出。不存在冻结数量，即都为0')
                    elif column == 9:
                        QMessageBox.about(self, '解冻数量', '债券买卖属于T+0交易，当天买入的债券当天可以卖出。不存在解冻数量，即都为0')
                    elif column == 10:
                        QMessageBox.about(self, '成本价', '成本价 = 成交价格')
                    elif column == 11:
                        QMessageBox.about(self, '成本', '期初成本-成交价格*成交数量')

    '''重写事件：按下ESC键，程序结束'''

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = CallEnableTool()
    ex.show()
    sys.exit(app.exec_())
