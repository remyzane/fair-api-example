#!/usr/bin/env python3

import os
import sys
from argparse import ArgumentParser

sys.path.insert(0, '..')
from http_api.utility import CustomizeHelpFormatter
from http_api.assist.profile import run_profile
from http_api.assist.pyshell import start_ipython

import example
from example import config, program_dir, workspace


# test mode
def run(params=None):
    # run simple web server, don't use flask reloader (invalid when threw exception)
    example.app.run('localhost', 5000, use_reloader=False)


# shell interface
def shell():
    # start shell using environment variable
    start_ipython([
        ('app', example.app, 'flask app'),
        ('rules', example.app.url_map._rules, 'url -> view rule')
    ])


# performance analysis
def profile(params=None):
    var_env = {'run': run, 'params': params}
    save_dir = os.path.join(workspace)
    run_profile('run(params)', var_env, save_dir)


# main
if __name__ == '__main__':
    usage = [
        ' ------------------------------ help ------------------------------',
        ' -h                    show help message',
        ' run                   test mode (running only)',
        ' code                  development mode (automatic reload and compilation)',
        ' shell                 shell interface',
        ' profile               performance analysis',
    ]
    parser = ArgumentParser(usage=os.linesep.join(usage), formatter_class=CustomizeHelpFormatter)
    parser.add_argument('command', type=str)
    parser.add_argument('-p', '--params', default=[])
    args = parser.parse_args()

    # run command
    if args.command not in ['run', 'code', 'shell', 'profile']:
        parser.print_help()
    else:
        locals()[args.command](*[] if not args.params else args.params)