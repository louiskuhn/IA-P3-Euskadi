import os

class Config:

  SECRET_KEY = os.environ.get('SECRET_KEY') or 'ma_cle_aleatoire2'