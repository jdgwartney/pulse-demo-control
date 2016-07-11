from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from application.ui import uis
from application.api import apis
from flask_log import Logging
import logging

logger = logging.getLogger(__name__)

app = Flask(__name__)

app.config['FLASK_LOG_LEVEL'] = 'DEBUG'
flask_log = Logging(app)

Bootstrap(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


app.register_blueprint(uis, url_prefix='/ui')
app.register_blueprint(apis, url_prefix='/v1/api')


logger.debug(app.url_map)

