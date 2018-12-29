import logging, os
from logging import Handler, FileHandler, StreamHandler
from PyQt5.QtCore import QFile, QIODevice, QTextStream, QTextCodec

'''
日志记录类
'''
class PathFileHandler(FileHandler):
    def __init__(self, path, filename, mode='a', encoding=None, delay=False):

        filename = os.fspath(filename)
        if not os.path.exists(path):
            os.mkdir(path)
        self.baseFilename = os.path.join(path, filename)
        self.mode = mode
        self.encoding = encoding
        self.delay = delay
        if delay:
            Handler.__init__(self)
            self.stream = None
        else:
            StreamHandler.__init__(self, self._open())


class Loggers(object):
    # 日志级别关系映射
    level_relations = {
        'debug': logging.DEBUG, 'info': logging.INFO, 'warning': logging.WARNING,
        'error': logging.ERROR, 'critical': logging.CRITICAL
    }

    def __init__(self, filename='coder.log', level='info', log_dir='log',
                 fmt='%(asctime)s : %(message)s'):
        self.logger = logging.getLogger(filename)
        abspath = os.path.dirname(os.path.abspath(__file__))
        self.directory = os.path.join(abspath, log_dir)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        stream_handler = logging.StreamHandler()  # 往屏幕上输出
        stream_handler.setFormatter(format_str)
        file_handler = PathFileHandler(path=self.directory, filename=filename, mode='a')
        file_handler.setFormatter(format_str)
        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)


'''
QSS文件读取函数
'''
def readData(path):
    """red file data"""
    file = QFile(path)
    if not file.open(QIODevice.ReadOnly):
        return
    stream = QTextStream(file)
    stream.setCodec(QTextCodec.codecForName('UTF-8'))
    data = stream.readAll()
    file.close()
    del stream
    return data
