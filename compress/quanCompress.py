#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import subprocess

import server
from compress.baseCompress import BaseCompress

class QuanCompress(BaseCompress):
    def __init__(self):
        self._inpath = ""
        self._outpath = ""
        self._exe_path = os.getcwd() + "\libs\pngquant.exe"

    def compress(self, data=None):
        if not data is None:
            self._inpath = data["inpath"]
            self._outpath = data["outpath"]

        if self._inpath == "":
            print "QuanCompress inpath is null"
            return

        if not os.path.exists(self._exe_path):
            print "pngquant.exe is null, path=",self._exe_path
            return

        temp_inpath = self._inpath
        for dirpath, dirs, files in os.walk(self._inpath):
            for file in files:
                if file[-4:] == ".png":
                    if self._outpath is None or self._outpath == "":
                        self._pngquantPicture(os.path.join(dirpath, file))
                    else:
                        out_dir = self._outpath + dirpath.replace(temp_inpath, "")
                        if not os.path.exists(out_dir):
                            os.makedirs(out_dir)
                            print "====makedirs===",out_dir
                        # print file
                        self._pngquantPicture(os.path.join(dirpath,file),os.path.join(out_dir, file))


    def _pngquantPicture(self, file, outpath = ""):
        if outpath == "":
            com = " --ext .png -f --quality 50-80 " + file
        else:
            com = " -f --quality 50-80 -o " + outpath + " " + file
        dir_path = self._exe_path

        command = dir_path + com;
        p = subprocess.Popen(command, shell=True)
        p.wait()
        server.manager.sendEvent("update_text", file)
        # print file


