from flask import Flask

from .config import app_config
from src.models._init_ import db,bcrypt

def create_app(env_name): 

  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])

  bcrypt.init_app(app)
  """For initialization of bycrypt"""
  
  db.init_app(app)
  """for initialization of db"""

  @app.route('/', methods=['GET'])
  def index():
    return 'first endpoint is working'

  return app
