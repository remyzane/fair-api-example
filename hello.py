from fair import Fair

app = Fair(__name__)


@app.route('/')
def hello(name):
    """ Hello Fair-API

    :param Str * name: you name ...
    """
    return 'Hello %s' % name
