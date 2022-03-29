from flask import Flask
from .config import app_config
from .models import db

from .routes.Province  import province_api as province_blueprint

def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])
    
    db.init_app(app)
    
    app.register_blueprint(province_blueprint,  url_prefix='/api/v1/province')
    
    @app.route('/', methods=['GET'])
    def index():
        return 'TEST  ENDPOINT !!'
    return app