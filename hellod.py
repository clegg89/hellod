#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 clegg <clegg@penrose>
#
# Distributed under terms of the MIT license.

"""

"""

import daemon
import time
import datetime
import os
import sys
import signal

#log = open('/tmp/hellod.log', 'a')

def get_timestamp():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

def sigterm_cleanup(signal, frame):
    print get_timestamp() + ' Received SIGTERM, Exit'
    sys.exit(0)

signal_map = {
        signal.SIGTERM : sigterm_cleanup
        }

with open('/tmp/hellod.log', 'a') as log:
    log.write(get_timestamp() + " Start" + os.linesep)
    log.flush()
    with daemon.DaemonContext(signal_map=signal_map, stdout=log) as d:
        while True:
            print get_timestamp() + " Hello, World!"
            sys.stdout.flush()
            time.sleep(30)
