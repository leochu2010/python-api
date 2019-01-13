from flask import Blueprint

hello_apis = Blueprint("hello_apis", __name__)


@hello_apis.route('/api/hello')
def hello():
    return 'Hello, World!'
