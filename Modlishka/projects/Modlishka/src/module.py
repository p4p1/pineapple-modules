#!/usr/bin/env python

import logging
import os
import signal

from pineapple.modules import Module, Request

# CONSTANTS
_MODULE_PATH = '/pineapple/ui/modules/Modlishka'
_ASSETS_PATH = f'{_MODULE_PATH}/assets'
_MODLISHKA_BIN = f'{_ASSETS_PATH}/proxy_mipsle'
_MODLISHKA_LOG = '/tmp/modlishka.log'
_CONFIG_FILE = f'{_ASSETS_PATH}/config.json'
_PID_FILE = '/tmp/modlishka_pid'
module = Module('Modlishka', logging.DEBUG)

@module.handles_action('get_config')
def get_config(request: Request):
    with open(_CONFIG_FILE, "r") as fp:
        return fp.read()

@module.handles_action('run_modlishka')
def run_modlishka(request: Request):
    os.system('service dnsmasq restart')
    pid = os.fork()
    if pid > 0:
        with open(_PID_FILE, "w") as fp:
            fp.write(str(pid))
        os.system(f'{_MODLISHKA_BIN} -debug -config {_CONFIG_FILE} &> {_MODLISHKA_LOG}')
    return pid

@module.handles_action('stop_modlishka')
def stop_modlishka(request: Request):
    pid = -1
    with open(_PID_FILE, "r") as fp:
        pid = int(fp.read())
    if pid > 0:
        os.kill(pid, signal.KILL)
        return True
    return False

if __name__ == "__main__":
    module.start()
