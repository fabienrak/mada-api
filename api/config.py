import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Development(object):
    DEBUG   =   True
    SQLALCHEMY_TRACK_MODIFICATIONS  =   False
    SQLALCHEMY_DATABASE_URI =   os.getenv('DATABASE_URL')
    
app_config = {
    'development':  Development
}    
    