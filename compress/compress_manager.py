#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading

#压缩逻辑管理类，2种压缩方式可以选择，所以使用了策略模式 + 简单工厂方法
class CompressManager(object):
    def __init__(self):
        self._compress = None

    def _createCompress(self, data):
        type = data["type"]
        compress = None
        if type == "tinypng":
            import tinyCompress
            compress = tinyCompress.TinyCompress()
        elif type == "quanpng":
            import  quanCompress
            compress = quanCompress.QuanCompress()
        return compress

    def compress(self, *data):
        t = threading.Thread(target=self.thread_compress, args=data)
        t.start()

    def thread_compress(self,  data):
        self._compress = self._createCompress(data)
        if self._compress is None:
            return
        self._compress.compress(data)


