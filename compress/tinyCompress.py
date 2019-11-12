#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import tinify

import server
from compress.baseCompress import BaseCompress

class TinyCompress(BaseCompress):
    def __init__(self):
        self._inpath = ""
        self._outpath = ""
        self._api = ""


    def compress(self,data):
        if not data is None:
            self._inpath = data["inpath"]
            self._outpath = data["outpath"]
            self._api = data["api"]

        if self._inpath == "":
            print "TinyCompress inpath is null"
            return

        tinify.key = self._api
        temp_inpath = self._inpath
        for dirpath, dirs, files in os.walk(self._inpath):
            for file in files:
                if file[-4:] == ".png":
                    if self._outpath is None or self._outpath == "":
                        self._tinypngPicture(os.path.join(dirpath, file))
                    else:
                        out_dir = self._outpath + dirpath.replace(temp_inpath, "")
                        if not os.path.exists(out_dir):
                            os.makedirs(out_dir)
                            print "====makedirs===",out_dir
                        # print file
                        self._tinypngPicture(os.path.join(dirpath,file),os.path.join(out_dir, file))

    def _tinypngPicture(self, file, outpath = ""):
        if outpath == "":
            tinify.from_file(file).to_file(file)
        else:
            tinify.from_file(file).to_file(outpath)
        server.manager.sendEvent("update_text", file)
        server.manager.sendEvent("update_remain_count", tinify.compression_count)
        print file

