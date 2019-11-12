#!/usr/bin/python
# -*- coding: UTF-8 -*-

class ServerManager(object):
    def __init__(self):
        self._event = {}

    def initialize(self):
        pass

    def sendEvent(self, event, args):
        if self._event is None or len(self._event) <= 0:
            return
        fun = self._event.get(event)
        if fun is None:
            return
        fun(args)

    def listenEvent(self, event, function):
        self._event.setdefault(event, function)
        # print event, function