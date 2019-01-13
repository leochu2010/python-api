from flask import Flask
from api.flask_api.endpoint.hello import hello_apis

app = Flask(__name__)

app.register_blueprint(hello_apis)
