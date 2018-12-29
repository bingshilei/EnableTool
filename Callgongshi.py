# -*- coding: utf-8 -*-

"""
公式显示.
"""


from PyQt5.QtWidgets import QMainWindow, QApplication, QAbstractItemView

from Ui_gongshi import Ui_gongshi


class Callgongshi(QMainWindow, Ui_gongshi):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Callgongshi, self).__init__(parent)
        self.setupUi(self)
        #合并资产变化单元格
        self.gstableWidget.setSpan(0, 0, 8, 1 )
        #设置所有列根据内容适应
        self.gstableWidget.resizeColumnsToContents()
        #设置某列根据内容适应
        #self.gstableWidget.resizeColumnToContents(2)
        #设置所有行根据内容适应
        self.gstableWidget.resizeRowsToContents()
        #设置表格不可编辑
        self.gstableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        
        #self.gstableWidget.horizontalHeader().setSectionResizeMode(1)#列宽设置
#        self.gstableWidget.verticalHeader().setSectionResizeMode(1)#行高设置          
#        self.gstableWidget.verticalHeader().setStretchLastSection(True); #充满行高  


        #合并资金变化单元格
        self.gstableWidget.setSpan(8, 0, 6, 1 )
        #合并资金变化单元格
        self.gstableWidget.setSpan(14, 0, 7, 1 )

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = Callgongshi()
    ui.show()
    sys.exit(app.exec_())
