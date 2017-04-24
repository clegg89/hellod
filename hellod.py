#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 clegg <clegg@penrose>
#
# Distributed under terms of the MIT license.

"""

"""

from daemon import Daemon
import time
import datetime
import sys
import signal

def get_timestamp():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

def sigterm_cleanup(signal, frame):
    print get_timestamp() + ' Received SIGTERM, Exit'
    sys.stdout.flush()
    sys.exit(0)

signal_map = {
        signal.SIGTERM : sigterm_cleanup
        }

class Hello(Daemon):
    def run(self):
        print get_timestamp() + " Start"
        while True:
            print get_timestamp() + " Hello, World!"
            sys.stdout.flush()
            time.sleep(30)

hellod = Hello(pidfile='/var/run/hellod.pid', stdout='/tmp/hellod.log')
hellod.start()
