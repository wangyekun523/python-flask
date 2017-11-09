#!/usr/bin/env python3

import connexion
import sys
from daemon import Daemon
class RunDaemon(Daemon):
    def __init__(self):
        super(RunDaemon, self).__init__(pidfile='/var/run/swagger.pid', stdout='/var/log/swagger.log')

    def run(self):
        # 执行业务类的方法
        # code.
        app = connexion.App(__name__, specification_dir='./swagger/')
        app.add_api('swagger.yaml', arguments={'title': '业务对象管理后端 API 列表'})
        app.run(port=8081)
if __name__ == '__main__':
    daemon = RunDaemon()
    # 进入初始参数判断
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print ("Unknown command")
            sys.exit(2)
            sys.exit(0)
    else:
        print ("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)

