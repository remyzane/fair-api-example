import fair
from . import app, air


@app.route('/flask')
def flask_route():
    return 'This route build by flask self.'


@air.route('/')
def area(area_id):
    """ Get the area information through it's id.

    Detail info for api ...

    :plugin: json_p
    :param Int * area_id: Area id's description ...
    :raise id_not_exist: Record does not exist.
    """
    if area_id > 100:
        return 'id_not_exist'
    else:
        return 'success'
