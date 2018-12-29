"""
Created on 2018年12月26日
@author: Yiluo
@file: CallShareTrade
@description:债券回购计算
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication,  QTableWidgetItem, QMessageBox, QStyleFactory
from Ui_ShareTrade import Ui_EnableTool
from Log import Loggers


__Author__ = """
By: Yiluo 
QQ: 786129166
Email: 786129166@qq.com"""
__Copyright__ = 'Copyright (c) 2018 Yiluo'
__Version__ = 1.0

class CallShareTrade(QMainWindow, Ui_EnableTool):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(CallShareTrade, self).__init__(parent)
        self.setupUi(self)
        self.log = Loggers(level='debug')
        self.initUI()
        
    def initUI(self):
        # 获取初始资产数据
        self.InitAssetList = []
        # 获取初始资金数据
        self.InitCurrentList = []
        # 获取初始证券数据
        self.InitStockList = []
        for i in range(7, 15):
            demo = self.tableWidgetAsset.item(0, i).text()
            self.InitAssetList.append(float(demo))
        for j in range(7, 13):
            demo = self.tableWidgetCurrent.item(0, j).text()
            self.InitCurrentList.append(float(demo))
        for k in range(7, 14):
            demo = self.tableWidgetStock.item(0, k).text()
            self.InitStockList.append(float(demo))

        # 获取计算后的资产数据
        self.FirstAssetList = self.InitAssetList[:]
        # 获取计算后的资金数据
        self.FirstCurrentList = self.InitCurrentList[:]
        # 获取计算后的证券数据
        self.FirstStockList = self.InitStockList[:]
        
        
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

    @pyqtSlot()
    def on_btnClear_clicked(self):
        """
        Slot documentation goes here.
        定义清空数据函数
        """
        # TODO: not implemented yet
        '''清空资产变化'''
        for i in range(1, 3):
            for j in range(1, 15):
                newItem = QTableWidgetItem('')
                self.tableWidgetAsset.setItem(i, j, newItem)
        '''清空资金变化'''
        for i in range(1, 3):
            for j in range(1, 13):
                newItem = QTableWidgetItem('')
                self.tableWidgetCurrent.setItem(i, j, newItem)
        '''清空证券变化'''
        for i in range(1, 3):
            for j in range(1, 14):
                newItem = QTableWidgetItem('')
                self.tableWidgetStock.setItem(i, j, newItem)
                
        # 获取初始化资产数据
        self.FirstAssetList = self.InitAssetList[:]
        # 获取初始化资金数据
        self.FirstCurrentList = self.InitCurrentList[:]
        # 获取初始化证券数据
        self.FirstStockList = self.InitStockList[:]
        
        self.log.logger.info('开始清除数据，请稍等...')
        self.log.logger.info('清楚数据完成,请开始操作。')
    
    @pyqtSlot()
    def on_btnInit_clicked(self):
        """
        Slot documentation goes here.
        定义日初始化函数
        """
        # TODO: not implemented yet
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
        # 获得交易费率
        en_bond_interest = float(self.c_bond_interest.text())
        newItem = QTableWidgetItem('%.2f' % en_bond_interest)
        self.tableWidgetAsset.setItem(2, 5, newItem)
        newItem = QTableWidgetItem('%.2f' % en_bond_interest)
        self.tableWidgetCurrent.setItem(2, 5, newItem)
        newItem = QTableWidgetItem('%.2f' % en_bond_interest)
        self.tableWidgetStock.setItem(2, 5, newItem)
        if en_entrust_direction == '买入':
            if en_entrust_status == '已报':
                '''资产变化'''
                for i in range(len(self.InitAssetList)):
                    newItem = QTableWidgetItem('%.2f' % int(self.InitAssetList[i]))
                    self.log.logger.info('买入已报，资产不变')
                    self.tableWidgetAsset.setItem(2, i + 7, newItem)
                
                

                '''资金变化'''
                for i in range(len(self.InitCurrentList)):
                    newItem = QTableWidgetItem('%.2f' % int(self.InitCurrentList[i]))
                    self.tableWidgetCurrent.setItem(2, i + 7, newItem)
                    
                self.log.logger.info('买入已报，资金不变')
                
                '''持仓变化'''
                for i in range(len(self.InitStockList)):
                    newItem = QTableWidgetItem('%d' % int(self.InitStockList[i]))
                    self.tableWidgetStock.setItem(2, i + 7, newItem)
                    
                self.log.logger.info('买入已报，持仓不变')    
            elif en_entrust_status == '已成':
                '''资产变化'''
                for i in range(8):
                    newItem = QTableWidgetItem('%.2f' % int(self.FirstAssetList[i]))
                    self.tableWidgetAsset.setItem(2, i + 7, newItem)
                '''资金变化'''
                for i in range(1, 5):
                    newItem = QTableWidgetItem('%.2f' % self.FirstCurrentList[i])
                    self.tableWidgetCurrent.setItem(2, i + 7, newItem)
                # 交易费为0
                newItem = QTableWidgetItem('0.00')
                self.tableWidgetCurrent.setItem(2, 7, newItem)
                # 解冻交易费为0
                newItem = QTableWidgetItem('0.00')
                self.tableWidgetCurrent.setItem(2, 12, newItem)
                '''持仓变化'''
                #当前持仓赋值
                newItem = QTableWidgetItem('%d'%self.FirstStockList[0])
                self.tableWidgetStock.setItem(2, 7, newItem)
                #可用数量=期初可用数量+冻结数量-解冻数量
                demo = self.FirstStockList[1]+self.FirstStockList[2]-self.FirstStockList[3]
                #为可用数量赋值
                newItem = QTableWidgetItem('%d'%demo)
                self.tableWidgetStock.setItem(2, 8, newItem)
                #冻结置为0
                newItem = QTableWidgetItem('0')
                self.tableWidgetStock.setItem(2, 9, newItem)
                for i in range(3, 7):
                    newItem = QTableWidgetItem('%d' % int(self.FirstStockList[i]))
                    self.tableWidgetStock.setItem(2, i + 7, newItem)
        elif en_entrust_direction == '卖出':
            if en_entrust_status == '已报':
                '''资产变化'''
                for i in range(len(self.FirstAssetList)):
                    newItem = QTableWidgetItem('%.2f' % int(self.FirstAssetList[i]))
                    self.tableWidgetAsset.setItem(2, i + 7, newItem)
                '''资金变化'''
                for i in range(len(self.FirstCurrentList)):
                    newItem = QTableWidgetItem('%.2f' % self.FirstCurrentList[i])
                    self.tableWidgetCurrent.setItem(2, i + 7, newItem)
                '''证券变化'''
                for i in range(len(self.InitStockList)):
                    newItem = QTableWidgetItem('%d' % int(self.InitStockList[i]))
                    self.tableWidgetStock.setItem(2, i + 7, newItem)
            elif en_entrust_status == '已成':
                '''资产变化'''
                for i in range(len(self.FirstAssetList)):
                    newItem = QTableWidgetItem('%.2f' % int(self.FirstAssetList[i]))
                    self.tableWidgetAsset.setItem(2, i + 7, newItem)
                '''资金变化'''
                # 交易费为0
                newItem = QTableWidgetItem('0.00')
                self.tableWidgetCurrent.setItem(2, 7, newItem)
                # 当前现金余额
                newItem = QTableWidgetItem('%.2f'%self.FirstCurrentList[1])
                self.tableWidgetCurrent.setItem(2, 8, newItem)
                # T+0可用金额 = 当前现金余额+冻结-解冻
                demo = self.FirstCurrentList[1]+self.FirstCurrentList[4]-self.FirstCurrentList[5]
                newItem = QTableWidgetItem('%.2f'%demo)
                self.tableWidgetCurrent.setItem(2, 9, newItem)
                # T+1可用金额 = 当前现金余额+冻结-解冻
                demo = self.FirstCurrentList[1]+self.FirstCurrentList[4]-self.FirstCurrentList[5]
                newItem = QTableWidgetItem('%.2f'%demo)
                self.tableWidgetCurrent.setItem(2, 10, newItem)
                # 冻结费为0
                newItem = QTableWidgetItem('0.00')
                self.tableWidgetCurrent.setItem(2, 11, newItem)
                # 解冻
                newItem = QTableWidgetItem('0.00')
                self.tableWidgetCurrent.setItem(2, 12, newItem)
                '''持仓变化'''
                for i in range(len(self.InitStockList)):
                    newItem = QTableWidgetItem('%d' % int(self.InitStockList[i]))
                    self.tableWidgetStock.setItem(2, i + 7, newItem)
                
    
    @pyqtSlot()
    def on_btnExport_clicked(self):
        """
        Slot documentation goes here.
        定义导出函数
        """
        # TODO: not implemented yet
        QMessageBox.information(self, '提示', '抱歉，该功能尚未开通！')
    
    @pyqtSlot()
    def on_btnCalculate_clicked(self):
        """
        Slot documentation goes here.
        定义股票买卖计算函数
        """
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
        # 获得交易费率
        en_bond_interest = float(self.c_bond_interest.text())
        newItem = QTableWidgetItem('%.2f' % en_bond_interest)
        self.tableWidgetAsset.setItem(1, 5, newItem)
        newItem = QTableWidgetItem('%.2f' % en_bond_interest)
        self.tableWidgetCurrent.setItem(1, 5, newItem)
        newItem = QTableWidgetItem('%.2f' % en_bond_interest)
        self.tableWidgetStock.setItem(1, 5, newItem)
        if en_stock_type == '股票':
            if en_entrust_direction == '买入':
                if en_entrust_status == '已报':
                    
                    #打印日志
                    self.log.logger.info('股票买入已报，资产、资金、持仓计算开始：')
                    
                    '''资产不变'''
                    for i in range(len(self.InitAssetList)):
                        newItem = QTableWidgetItem('%.2f' % int(self.InitAssetList[i]))
                        self.tableWidgetAsset.setItem(1, i + 7, newItem)
                    self.log.logger.info('股票买入已报，资产不变。')
                    
                    '''资金变化'''
                    #交易费 = 委托数量*委托价格*委托费率
                    TradeFee = round(self.FirstCurrentList[0]+en_entrust_amount*en_entrust_price*en_bond_interest, 2)
                    # 向FirstCurrentList列表添加现交易费值
                    self.FirstCurrentList.pop(0)
                    self.FirstCurrentList.insert(0, TradeFee)
                    
                    self.log.logger.info('股票买入已报交易费=委托数量*委托价格*委托费率')
                    # 当前现金余额=期初当前现金余额
                    cashBalance = self.FirstCurrentList[1]
                    # 向FirstCurrentList列表添加现金资产值
                    self.FirstCurrentList.pop(1)
                    self.FirstCurrentList.insert(1, cashBalance)
                    # T+0可用金额=期初T+0可用金额-委托数量*委托价格*(1+交易费率）
                    T0Balance = self.FirstCurrentList[2] - en_entrust_amount * en_entrust_price *(1+ en_bond_interest)
                    # 向FirstCurrentList列表添加T+0可用金额值
                    #print(len(self.FirstCurrentList))
                    self.FirstCurrentList.pop(2)
                    self.FirstCurrentList.insert(2, T0Balance)
                    # T+1可用金额=期初T+1可用金额-委托数量*委托价格*（1+交易费率）
                    T1Balance = self.FirstCurrentList[3] - en_entrust_amount * en_entrust_price *(1+ en_bond_interest)
                    # 向FirstAssetList列表添加应收值
                    self.FirstCurrentList.pop(3)
                    self.FirstCurrentList.insert(3, T1Balance)
                    # 冻结金额表示产品债券买卖实际交易成功后日终交收后实际需增加的金额
                    frozenBalance = self.FirstCurrentList[4]
                    # 向FirstCurrentList列表添加应付值
                    self.FirstCurrentList.pop(4)
                    self.FirstCurrentList.insert(4, frozenBalance)
                    # 解冻金额表示资金流出，但是未成交 无需进行解冻
                    unfrozenBalance = self.FirstCurrentList[5]
                    # 向FirstCurrentList列表添加总净值的值
                    self.FirstCurrentList.pop(5)
                    self.FirstCurrentList.insert(5, unfrozenBalance)
                    # 资金变化赋值
                    for i, j in (enumerate(self.FirstCurrentList)):
                        # print(i,j)
                        newItem = QTableWidgetItem('%.2f' % j)
                        self.tableWidgetCurrent.setItem(1, i + 7, newItem)
                    '''持仓变化'''
                    for i in range(7):
                        newItem = QTableWidgetItem('%s' % int(self.InitStockList[i]))
                        self.tableWidgetStock.setItem(1, i + 7, newItem)
                else:
                    '''资产变化'''
                    # 现金资产=当前现金余额-成交数量*成交价格*(1+交易费率）
                    currentAsset = self.FirstAssetList[0] - en_entrust_amount * en_entrust_price*(1 + en_bond_interest)
                    # currentAsset = previousCurrentAsset-en_entrust_amount * (en_entrust_price + en_bond_interest)
                    # 向FirstAssetList列表添加现金资产值
                    self.FirstAssetList.pop(0)
                    self.FirstAssetList.insert(0, currentAsset)
                    # 证券资产=期初证券资产+成交价格*成交数量
                    stockAsset = self.FirstAssetList[1] + en_entrust_amount * en_bond_interest
                    # 向FirstAssetList列表添加证券资产值
                    #print(len(self.FirstAssetList))
                    self.FirstAssetList.pop(1)
                    self.FirstAssetList.insert(1, stockAsset)
                    # 应收=期初应收
                    acceptAsset = self.FirstAssetList[2]
                    # 向FirstAssetList列表添加应收值
                    self.FirstAssetList.pop(2)
                    self.FirstAssetList.insert(2, acceptAsset)
                    # 应付=期初应付
                    giveAsset = self.FirstAssetList[3]
                    # 向FirstAssetList列表添加应付值
                    self.FirstAssetList.pop(3)
                    self.FirstAssetList.insert(3, giveAsset)
                    # 总资产=期初总资产-成交价格*成交数量*交易费率
                    totalAsset = self.FirstAssetList[4]-en_entrust_amount * en_bond_interest*en_bond_interest
                    # 向FirstAssetList列表添加总净值的值
                    self.FirstAssetList.pop(4)
                    self.FirstAssetList.insert(4, totalAsset)
                    # 净值=现金资产+证券资产+应收-应付
                    valueAsset = currentAsset + stockAsset + acceptAsset - giveAsset
                    # 向FirstAssetList列表添加净值的值
                    self.FirstAssetList.pop(5)
                    self.FirstAssetList.insert(5, valueAsset)
                    # 产品份额：即产品成立时的份额，开放期会有申购或者赎回
                    productAmount = int(self.InitAssetList[6])
                    # 向FirstAssetList列表添加产品份额值
                    self.FirstAssetList.pop(6)
                    self.FirstAssetList.insert(6, productAmount)
                    # 单位净值=净值/产品份额
                    perValueAsset = valueAsset / productAmount
                    # 向FirstAssetList列表添加单位净值的值
                    self.FirstAssetList.pop(7)
                    self.FirstAssetList.insert(7, perValueAsset)
                    # print('长度为{0}'.format(len(self.FirstAssetList)))
                    # 资产变化赋值
                    for i, j in (enumerate(self.FirstAssetList)):
                        # print(i,j)
                        newItem = QTableWidgetItem('%.2f' % j)
                        self.tableWidgetAsset.setItem(1, i + 7, newItem)
                    
                    '''资金变化'''
                    #交易费 = 委托数量*委托价格*委托费率
                    TradeFee = round(self.FirstCurrentList[0]+en_entrust_amount*en_entrust_price*en_bond_interest, 2)
                    # 向FirstCurrentList列表添加现交易费值
                    self.FirstCurrentList.pop(0)
                    self.FirstCurrentList.insert(0, TradeFee)
                    # 当前现金余额=期初当前现金余额-成交数量*成交价格*(1+交易费率）
                    cashBalance = self.FirstCurrentList[1]-en_entrust_amount * en_entrust_price *(1+ en_bond_interest)
                    # 向FirstCurrentList列表添加现金资产值
                    self.FirstCurrentList.pop(1)
                    self.FirstCurrentList.insert(1, cashBalance)
                    # T+0可用金额=期初T+0可用金额-成交数量*成交价格*(1+交易费率）
                    T0Balance = self.FirstCurrentList[2] - en_entrust_amount * en_entrust_price *(1+ en_bond_interest)
                    # 向FirstCurrentList列表添加T+0可用金额值
                    #print(len(self.FirstCurrentList))
                    self.FirstCurrentList.pop(2)
                    self.FirstCurrentList.insert(2, T0Balance)
                    # T+1可用金额=期初T+1可用金额-成交数量*成交价格*(1+交易费率）
                    T1Balance = self.FirstCurrentList[3] - en_entrust_amount * en_entrust_price *(1+ en_bond_interest)
                    # 向FirstAssetList列表添加应收值
                    self.FirstCurrentList.pop(3)
                    self.FirstCurrentList.insert(3, T1Balance)
                    # 冻结金额表示产品债券买卖实际交易成功后日终交收后实际需增加的金额
                    frozenBalance = self.FirstCurrentList[4]
                    # 向FirstCurrentList列表添加应付值
                    self.FirstCurrentList.pop(4)
                    self.FirstCurrentList.insert(4, frozenBalance)
                    # 解冻金额表示资金流出，解冻金额=成交数量*成交价格*(1+交易费率）
                    unfrozenBalance = self.FirstCurrentList[5]+en_entrust_amount * en_entrust_price *(1+ en_bond_interest)
                    # 向FirstCurrentList列表添加总净值的值
                    self.FirstCurrentList.pop(5)
                    self.FirstCurrentList.insert(5, unfrozenBalance)
                    # 资金变化赋值
                    for i, j in (enumerate(self.FirstCurrentList)):
                        # print(i,j)
                        newItem = QTableWidgetItem('%.2f' % j)
                        self.tableWidgetCurrent.setItem(1, i + 7, newItem)
                    
                    '''持仓变化'''
                    # 当前持仓数量=期初持仓数量+成交数量
                    currentAmount = self.FirstStockList[0] + en_entrust_amount
                    # 向FirstStockList列表添加当前持仓数量值
                    self.FirstStockList.pop(0)
                    self.FirstStockList.insert(0, currentAmount)
                    # 可用数量=期初可用数量
                    enableAmmount = self.FirstStockList[1] 
                    # 向FirstStockList列表添加T+0可用数量值
                    #print(len(self.FirstStockList))
                    self.FirstStockList.pop(1)
                    self.FirstStockList.insert(1, enableAmmount)
                    # 股票买卖属于T+1交易，冻结数量=期初冻结数量+成交数量
                    frozenAmount = self.FirstStockList[2]+ en_entrust_amount
                    # 向FirstStockList列表添加冻结数量值
                    self.FirstStockList.pop(2)
                    self.FirstStockList.insert(2, frozenAmount)
                    # 解冻数量=期初解冻数量
                    unfrozenAmount = self.FirstStockList[3]
                    # 向FirstStockList列表添加总净值的值
                    self.FirstStockList.pop(3)
                    self.FirstStockList.insert(3, unfrozenAmount)
                    # 成本价 = 期初成本价格+成交价格
                    # QMessageBox.information(self, '123', '%d' % self.FirstStockList[4])
                    currentInvestPrice = self.FirstStockList[4] + en_entrust_price
                    # 向FirstStockList列表添加成本价的值
                    self.FirstStockList.pop(4)
                    self.FirstStockList.insert(4, currentInvestPrice)
                    # 成本 = 期初成本+成交价格*成交数量
                    currentInvest = self.FirstStockList[5] + en_entrust_price * en_entrust_amount
                    # 向FirstStockList列表添加成本的值
                    self.FirstStockList.pop(5)
                    self.FirstStockList.insert(5, currentInvest)
                    # 含费用成本 = 成交价格*成交数量*(1+交易费率)
                    currentInvest = self.FirstStockList[6] + en_entrust_price * en_entrust_amount*(1+en_bond_interest)
                    # 向FirstStockList列表添加成本的值
                    self.FirstStockList.pop(6)
                    self.FirstStockList.insert(6, currentInvest)
                    # print('长度为{0}'.format(len(self.FirstAssetList)))
                    # 持仓变化赋值
                    for i, j in (enumerate(self.FirstStockList)):
                        # print(i,j)
                        newItem = QTableWidgetItem('%d' % j)
                        self.tableWidgetStock.setItem(1, i + 7, newItem)
            elif en_entrust_direction == '卖出':
                if en_entrust_status == '已报':
                    '''资产变化'''
                    # 卖出已报，资产不变化
                    for i in range(8):
                        newItem = QTableWidgetItem('%.2f' % int(self.InitAssetList[i]))
                        self.tableWidgetAsset.setItem(1, i + 7, newItem)
                    '''资金变化'''
                    # 卖出已报，资金不变化
                    for i in range(6):
                        newItem = QTableWidgetItem('%.2f' % int(self.InitCurrentList[i]))
                        self.tableWidgetCurrent.setItem(1, i + 7, newItem)
                    '''证券变化'''
                    # 当前持仓数量=期初持仓数量
                    currentAmount = self.FirstStockList[0] 
                    # 向FirstStockList列表添加当前持仓数量值
                    self.FirstStockList.pop(0)
                    self.FirstStockList.insert(0, currentAmount)
                    # 可用数量=期初可用数量-委托数量
                    enableAmmount = self.FirstStockList[1] - en_entrust_amount
                    # 向FirstStockList列表添加T+0可用数量值
                    #print(len(self.FirstStockList))
                    self.FirstStockList.pop(1)
                    self.FirstStockList.insert(1, enableAmmount)
                    # 股票买卖属于T+1交易，冻结数量=期初冻结数量+委托数量
                    frozenAmount = self.FirstStockList[2]+ en_entrust_amount
                    # 向FirstStockList列表添加冻结数量值
                    self.FirstStockList.pop(2)
                    self.FirstStockList.insert(2, frozenAmount)
                    # 解冻数量=期初解冻数量
                    unfrozenAmount = self.FirstStockList[3]
                    # 向FirstStockList列表添加总净值的值
                    self.FirstStockList.pop(3)
                    self.FirstStockList.insert(3, unfrozenAmount)
                    # 成本价 = 期初本价
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
                        self.tableWidgetStock.setItem(1, i + 7, newItem)
                else:
                    '''资产变化'''
                    # 现金资产=当前现金余额+成交数量*成交价格*(1-交易费率）
                    currentAsset = self.FirstAssetList[0] + en_entrust_amount * en_entrust_price*(1 - en_bond_interest)
                    # currentAsset = previousCurrentAsset-en_entrust_amount * (en_entrust_price + en_bond_interest)
                    # 向FirstAssetList列表添加现金资产值
                    self.FirstAssetList.pop(0)
                    self.FirstAssetList.insert(0, currentAsset)
                    # 证券资产=期初证券资产-成交价格*成交数量
                    stockAsset = self.FirstAssetList[1] - en_entrust_amount * en_bond_interest
                    # 向FirstAssetList列表添加证券资产值
                    #print(len(self.FirstAssetList))
                    self.FirstAssetList.pop(1)
                    self.FirstAssetList.insert(1, stockAsset)
                    # 应收=期初应收
                    acceptAsset = self.FirstAssetList[2]
                    # 向FirstAssetList列表添加应收值
                    self.FirstAssetList.pop(2)
                    self.FirstAssetList.insert(2, acceptAsset)
                    # 应付=期初应付
                    giveAsset = self.FirstAssetList[3]
                    # 向FirstAssetList列表添加应付值
                    self.FirstAssetList.pop(3)
                    self.FirstAssetList.insert(3, giveAsset)
                    # 总资产=期初总资产-成交价格*成交数量*交易费率
                    totalAsset = self.FirstAssetList[4]-en_entrust_amount * en_bond_interest*en_bond_interest
                    # 向FirstAssetList列表添加总净值的值
                    self.FirstAssetList.pop(4)
                    self.FirstAssetList.insert(4, totalAsset)
                    # 净值=现金资产+证券资产+应收-应付
                    valueAsset = currentAsset + stockAsset + acceptAsset - giveAsset
                    # 向FirstAssetList列表添加净值的值
                    self.FirstAssetList.pop(5)
                    self.FirstAssetList.insert(5, valueAsset)
                    # 产品份额：即产品成立时的份额，开放期会有申购或者赎回
                    productAmount = int(self.InitAssetList[6])
                    # 向FirstAssetList列表添加产品份额值
                    self.FirstAssetList.pop(6)
                    self.FirstAssetList.insert(6, productAmount)
                    # 单位净值=净值/产品份额
                    perValueAsset = valueAsset / productAmount
                    # 向FirstAssetList列表添加单位净值的值
                    self.FirstAssetList.pop(7)
                    self.FirstAssetList.insert(7, perValueAsset)
                    # print('长度为{0}'.format(len(self.FirstAssetList)))
                    # 资产变化赋值
                    for i, j in (enumerate(self.FirstAssetList)):
                        # print(i,j)
                        newItem = QTableWidgetItem('%.2f' % j)
                        self.tableWidgetAsset.setItem(1, i + 7, newItem)
                    '''资金变化'''
                    #交易费 = 期初交易费+委托数量*委托价格*委托费率
                    TradeFee = round(self.FirstCurrentList[0]+en_entrust_amount*en_entrust_price*en_bond_interest, 2)
                    # 向FirstCurrentList列表添加现交易费值
                    self.FirstCurrentList.pop(0)
                    self.FirstCurrentList.insert(0, TradeFee)
                    # 当前现金余额=期初当前现金余额+成交数量*成交价格*(1-交易费率）
                    cashBalance = self.FirstCurrentList[1]+en_entrust_amount * en_entrust_price *(1-en_bond_interest)
                    # 向FirstCurrentList列表添加现金资产值
                    self.FirstCurrentList.pop(1)
                    self.FirstCurrentList.insert(1, cashBalance)
                    # T+0可用金额=期初T+0可用金额
                    T0Balance = self.FirstCurrentList[2]
                    # 向FirstCurrentList列表添加T+0可用金额值
                    #print(len(self.FirstCurrentList))
                    self.FirstCurrentList.pop(2)
                    self.FirstCurrentList.insert(2, T0Balance)
                    # T+1可用金额=期初T+1可用金额+成交数量*成交价格*(1-交易费率）
                    T1Balance = self.FirstCurrentList[3] + en_entrust_amount * en_entrust_price *(1- en_bond_interest)
                    # 向FirstAssetList列表添加应收值
                    self.FirstCurrentList.pop(3)
                    self.FirstCurrentList.insert(3, T1Balance)
                    # 冻结金额表示产品股票买卖实际交易成功后日终交收后实际需增加的金额
                    #冻结金额=期初冻结金额+成交数量*成交价格*(1-交易费率）
                    frozenBalance = self.FirstCurrentList[4]+en_entrust_amount * en_entrust_price *(1- en_bond_interest)
                    # 向FirstCurrentList列表添加应付值
                    self.FirstCurrentList.pop(4)
                    self.FirstCurrentList.insert(4, frozenBalance)
                    # 解冻金额表示资金流出，解冻金额=期初解冻金额
                    unfrozenBalance = self.FirstCurrentList[5]
                    # 向FirstCurrentList列表添加总净值的值
                    self.FirstCurrentList.pop(5)
                    self.FirstCurrentList.insert(5, unfrozenBalance)
                    # 资金变化赋值
                    for i, j in (enumerate(self.FirstCurrentList)):
                        # print(i,j)
                        newItem = QTableWidgetItem('%.2f' % j)
                        self.tableWidgetCurrent.setItem(1, i + 7, newItem)
                    '''持仓变化'''
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
                    # 股票买卖属于T+1交易，冻结数量=期初冻结数量
                    frozenAmount = self.FirstStockList[2]
                    # 向FirstStockList列表添加冻结数量值
                    self.FirstStockList.pop(2)
                    self.FirstStockList.insert(2, frozenAmount)
                    # 解冻数量=期初解冻数量
                    unfrozenAmount = self.FirstStockList[3]
                    # 向FirstStockList列表添加总净值的值
                    self.FirstStockList.pop(3)
                    self.FirstStockList.insert(3, unfrozenAmount)
                    # 成本价 = 期初成本价格
                    # QMessageBox.information(self, '123', '%d' % self.FirstStockList[4])
                    currentInvestPrice = self.FirstStockList[4] 
                    # 向FirstStockList列表添加成本价的值
                    self.FirstStockList.pop(4)
                    self.FirstStockList.insert(4, currentInvestPrice)
                    # 成本 = 期初成本-成本价*成交数量
                    currentInvest = self.FirstStockList[5] - currentInvestPrice * en_entrust_amount
                    # 向FirstStockList列表添加成本的值
                    self.FirstStockList.pop(5)
                    self.FirstStockList.insert(5, currentInvest)
                    # 含费用成本 = 期初含费用成本-成本价*成交数量
                    currentInvest = self.FirstStockList[6] - currentInvestPrice * en_entrust_amount
                    # 向FirstStockList列表添加含费用成本的值
                    self.FirstStockList.pop(6)
                    self.FirstStockList.insert(6, currentInvest)
                    # print('长度为{0}'.format(len(self.FirstAssetList)))
                    # 持仓变化赋值
                    for i, j in (enumerate(self.FirstStockList)):
                        newItem = QTableWidgetItem('%d' % j)
                        self.tableWidgetStock.setItem(1, i + 7, newItem)
                    

                    
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    ui = CallShareTrade()
    ui.show()
    sys.exit(app.exec_())
