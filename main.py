import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from src.app import app

HOST ='localhost'
PORT = 5050
DEBUG = True

if __name__ == '__main__' :
    app.run(HOST,PORT,DEBUG)