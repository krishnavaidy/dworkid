# app/__init__.py

from flask import Flask

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'dworkid',
    'host': 'mongodb://admin:blockhack@ds153869.mlab.com:53869/dworkid'
}

from app import views


