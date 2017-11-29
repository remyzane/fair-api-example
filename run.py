#!/usr/bin/env python3

import os
import sys
from argparse import ArgumentParser

sys.path.insert(0, 'fair-api')

import example


def do_run(address=None):
    address = address or '0.0.0.0:5000'
    host, port = address.split(':')
    extra_files = [os.path.join(example.workspace, 'conf', 'example.toml')]
    print(extra_files)
    example.app.debug = True
    example.app.jinja_env.auto_reload = True
    example.app.run(host, int(port), use_reloader=True, extra_files=extra_files)


def do_shell():
    from fair.assist.pyshell import start_ipython
    # start shell using environment variable
    start_ipython([
        ('app', example.app, 'flask app'),
        ('rules', example.app.url_map._rules, 'url -> view rule')
    ])


def do_profile(params=None):
    from fair.assist.profile import run_profile
    var_env = {'run': do_run, 'params': params}
    save_dir = os.path.join(example.workspace)
    run_profile('run(params)', var_env, save_dir)


# main
if __name__ == '__main__':
    from example.utility import CustomizeHelpFormatter
    usage = [
        ' ------------------------------ help ------------------------------',
        ' -h                            show help message',
        ' run       -p x.x.x.x:yyy      run simple server',
        ' shell                         shell environment with project',
        ' profile                       performance analysis',
    ]
    parser = ArgumentParser(usage=os.linesep.join(usage), formatter_class=CustomizeHelpFormatter)
    parser.add_argument('command', type=str)
    parser.add_argument('-p', '--params', nargs='+')    # e.g. -p 'param 1' param2 'param 3'
    args = parser.parse_args()
    if 'do_' + args.command not in dir():
        parser.print_help()
    else:
        locals()['do_' + args.command](*[] if not args.params else args.params)
