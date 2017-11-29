# -*- coding: utf-8 -*-
import os
import datetime
from flask import Flask
from fair.configure import fair_setup

from .utility import get_config, set_logging

workspace = os.path.realpath(os.path.join(__file__, '..', '..'))
var_path = os.path.join(workspace, 'var')

# load config
config = get_config(os.path.join(workspace, 'conf'), 'example.yml')

# setting logging
set_logging(config['logging'], var_path)

# create wsgi application
app = application = Flask(__name__, static_folder='../www', static_url_path='/res',  template_folder='../')


flask_config = config.get('flask') or {}
for key, value in flask_config.items():
    # set the expiration date of a permanent session.
    if key == 'PERMANENT_SESSION_LIFETIME':
        app.config[key] = datetime.timedelta(days=int(value))
    else:
        app.config[key] = value

app_config = config.get('app') or {}
for key, value in app_config.items():
    app.config[key] = value


from fair.response import JsonRaise
from fair.plugin.jsonp import JsonP

fair_setup(app, var_path, config,
           plugins={'json_p': JsonP('callback')},
           responses={'default': JsonRaise}
           )
