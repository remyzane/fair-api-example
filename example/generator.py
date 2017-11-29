# -*- coding: utf-8 -*-

from flask import request

from example import app
from example.utility import SimpleAes


@app.route('/generator/token/', endpoint='generator.token')
def token():
    identity = request.args.get('identity')
    tests_access_key = request.args.get('tests_access_key')
    if not identity:
        return '/generator/token/ must specify the parameter [identity]'
    if not tests_access_key:
        return '/generator/token/ must specify the parameter [tests_access_key]'
    if tests_access_key not in app.config['web_ui']['access_keys']:
        return 'invalid tests_access_key'
    return app.config['plugins']['token'].create(identity)


@app.route('/generator/encrypt/', endpoint='generator.encrypt')
def encrypt():
    tests_access_key = request.args.get('tests_access_key')
    if not tests_access_key:
        return '/generator/token/ must specify the parameter [tests_access_key]'
    content = request.args.get('content')
    if not content:
        return ''
    try:
        encrypted = SimpleAes.decrypt(content)
        if encrypted:
            return content
    except UnicodeDecodeError:
        pass
    return SimpleAes.encrypt(content) or content
