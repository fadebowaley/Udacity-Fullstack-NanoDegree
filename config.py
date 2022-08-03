import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
#Sqlalchemy database URI settings



# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:root@localhost:5432/fyyur"
# SQLALCHEMY_DATABASE_URI = '<Put your local database url>'
