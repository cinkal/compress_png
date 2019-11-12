#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading


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


