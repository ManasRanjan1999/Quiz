
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///quiz_app.db' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)  
