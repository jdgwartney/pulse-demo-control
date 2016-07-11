from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from application.ui import uis
from application.api import apis

app = Flask(__name__)

Bootstrap(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


app.register_blueprint(uis, url_prefix='')
app.register_blueprint(apis, url_prefix='/v1/api')

# import application.models
# import application.views

print(app.url_map)

if __name__ == "__main__":
    app.run()
