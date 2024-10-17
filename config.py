# alsa_api/config.py
class Config:
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/alsa'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
