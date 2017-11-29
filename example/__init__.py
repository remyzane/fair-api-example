# -*- coding: utf-8 -*-
import os
from flask import Flask
from http_api.configure import http_api_setup

from .utility import get_config

conf_dir = os.path.realpath(os.path.join(__file__, '..', '..', 'conf'))
print(conf_dir)
# load config
config = get_config(conf_dir, 'example.yml')

# create wsgi application
app = application = Flask(__name__, static_folder='../www', static_url_path='/res',  template_folder='../')

workspace = http_api_setup(app, config)
