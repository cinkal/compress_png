#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    import sys
    sys.path.append("./pngquant")

    import server
    server.manager.initialize()

    import view
    view.manager.initialize()
