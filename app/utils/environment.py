import os
from os import environ, path
from dotenv import load_dotenv

ROOT_DIR = path.abspath(path.join(__file__, '../../..'))
load_dotenv(path.join(ROOT_DIR, '.env'))

def get_env_var(name) ->  str:
    try:
        return os.getenv(name)
    except KeyError:
        message =   "Variable d'environement {} non definie".format(name)
        raise Exception(message)