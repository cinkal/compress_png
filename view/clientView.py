#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkconstants import END
import Tkinter
import tkFileDialog
import ScrolledText

import server


class ClientView(object):
    def __init__(self):
        self._window = None
        self._api = None
        self._inpath = None
        self._outpath = None

        self._compress_type = None
        self._text = None

        self._remain_var = None

        self._compress_manager = None

    def create_out_frame(self, window, pady):
        frame = Tkinter.Frame(window)

        def select_path():
            _dir_path = tkFileDialog.askdirectory()
            self._outpath.set(_dir_path)

        label = Tkinter.Label(frame, text='输出的资源路径:')
        label.grid(row=1, column=0)

        entry = Tkinter.Entry(frame, show=None, textvariable=self._outpath, width=50)
        entry.grid(row=1, column=1)

        button = Tkinter.Button(frame, text='路径选择', command=select_path)
        button.grid(row=1, column=2)

        radio_var = Tkinter.StringVar()

        def select_type():
            print radio_var.get(), button
            if radio_var.get() == "cover":
                label.configure(state="disabled")
                entry.configure(state="disabled")
                button.configure(state="disabled")
                self._outpath.set("")
            else:
                label.configure(state="normal")
                entry.configure(state="normal")
                button.configure(state="normal")

        r1 = Tkinter.Radiobutton(frame, text='覆盖压缩', variable=radio_var, value='cover', command=select_type)
        r1.grid(row=0, column=0)
        r1.select()
        select_type()

        Tkinter.Radiobutton(frame, text='拷贝压缩', variable=radio_var, value='copy', command=select_type).grid(row=0,
                                                                                                            column=1)
        frame.pack(side="top", pady=pady, padx=20)

    def _do_after_init(self):
        self._window = Tkinter.Tk()
        self._api = Tkinter.StringVar()
        self._inpath = Tkinter.StringVar()
        self._outpath = Tkinter.StringVar()
        self._compress_type = Tkinter.StringVar()

        window = self._window
        window.geometry('650x720')

        ori_x = 0
        ori_y = 0

        Tkinter.Label(window, text='压缩方法选择:').place(x=ori_x, y=ori_y)

        r2 = Tkinter.Radiobutton(window, text='quanpng(本地)', variable=self._compress_type, value='quanpng')
        r2.place(x=ori_x, y=ori_y + 30, anchor="nw")
        r2.select()

        r1 = Tkinter.Radiobutton(window, text='tinypng(联网)', variable=self._compress_type, value='tinypng')
        r1.place(x=ori_x, y=ori_y + 60)

        self._remain_var = Tkinter.StringVar()
        self._remain_var.set("(剩余压缩张数: 0 张)")
        Tkinter.Label(window, text='剩余压缩张数:', textvariable=self._remain_var).place(x=ori_x + 100, y=ori_y + 60)

        Tkinter.Label(window, text='tiny_api:').place(x=ori_x + 220, y=ori_y + 60)

        self._api.set("QKmW4ZlG6bjmchvXcGlDpl94SnGpffnW")
        entry = Tkinter.Entry(window, show=None, textvariable=self._api, width=50, state="normal")
        entry.place(x=ori_x + 280, y=ori_y + 60)

        canvas = Tkinter.Canvas(window, bg='black', height=1, width=600)
        canvas.place(x=ori_x, y=ori_y + 90)

        self._inpath = Tkinter.StringVar()
        def select_path():
            _dir_path = tkFileDialog.askdirectory()
            self._inpath.set(_dir_path)

        label = Tkinter.Label(window, text='需要压缩的资源路径:')
        label.place(x=ori_x, y=ori_y + 110)

        entry = Tkinter.Entry(window, show=None, textvariable=self._inpath, width=50)
        entry.place(x=ori_x + 120, y=ori_y + 110)

        button = Tkinter.Button(window, text='路径选择', command=select_path)
        button.place(x=ori_x + 480, y=ori_y + 105)

        canvas = Tkinter.Canvas(window, bg='black', height=1, width=600)
        canvas.place(x=ori_x, y=ori_y + 150)
        # Tkinter.create_line(x0 - 50, y0 - 50, x1 - 50, y1 - 50)  # 画直线
        Tkinter.Label(window, text='压缩后资源存放方式:').place(x=ori_x, y=ori_y + 170)

        self.create_out_frame(window, 200)

        canvas = Tkinter.Canvas(window, bg='black', height=1, width=600)
        canvas.place(x=ori_x, y=ori_y + 300)

        def startCompress():
            self._compress_png()

        Tkinter.Button(window, text='开始压缩', command=startCompress).place(x=ori_x + 300, y=ori_y + 320)

        self._text = Tkinter.Text(window)
        self._text.place(x=ori_x, y=ori_y + 360)

        # 进入消息循环
        window.mainloop()

    def _compress_png(self):
        data = {
            "type": self._compress_type.get(),
            "api": self._api.get(),
            "inpath": self._inpath.get(),
            "outpath": self._outpath.get(),
        }
        if self._compress_manager is None:
            import compress.compress_manager
            self._compress_manager = compress.compress_manager.CompressManager()
        self._compress_manager.compress(data)



    def updateText(self, value):
        if self._text is None:
            return
        self._text.insert('end', "\n")
        self._text.insert('end', value)
        self._text.see('end')

    def updateRemainCount(self, value):
        self._remain_var.set("(剩余压缩张数: " + str(500-value) + " 张)")

    def initialize(self):
        server.manager.listenEvent("update_text", self.updateText)
        server.manager.listenEvent("update_remain_count", self.updateRemainCount)

        self._do_after_init()





