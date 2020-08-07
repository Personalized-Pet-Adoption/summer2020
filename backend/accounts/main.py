from backend.wsgi import application
from google.auth import app_engine

app = application
credentials = app_engine.Credentials()
