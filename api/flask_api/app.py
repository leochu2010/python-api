from flask import Flask
from api.flask_api.endpoint.hello import hello_apis
from api.flask_api.endpoint.summarize import summarize_apis
from logging.handlers import RotatingFileHandler
import logging

app = Flask(__name__)

handler = RotatingFileHandler('logs/flask.log', maxBytes=10000, backupCount=1)
formatter = logging.Formatter("[%(asctime)s] {%(name)s:%(lineno)d} %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logging.getLogger().setLevel(logging.INFO)
logging.getLogger().addHandler(handler)

app.register_blueprint(hello_apis)
app.register_blueprint(summarize_apis)

logging.getLogger().info("APIs ready")
