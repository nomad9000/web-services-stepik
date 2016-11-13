import os

path = os.path.abspath(__file__)
path = os.path.dirname(path)
path = os.path.dirname(path)
bind = "0.0.0.0:8000"
pythonpath = path + '/ask/ask/'