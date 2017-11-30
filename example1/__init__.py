import os
from flask import Flask
import fair

app = Flask(__name__)
fair.setup(app, cache_path=os.path.join(__file__, '..', '..', 'var'))

with app.app_context():
    from . import views
