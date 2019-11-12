#!/usr/bin/python
# -*- coding: UTF-8 -*-

#启动入口
if __name__ == '__main__':
    ##初始化服务管理
    import server
    server.manager.initialize()

    #初始化界面
    import view
    view.manager.initialize()
