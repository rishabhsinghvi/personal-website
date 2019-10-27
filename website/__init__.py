from flask import Flask
import os
from website.config import CONFIG_OBJ


app = Flask(__name__)
app.config.from_object(CONFIG_OBJ)

from website import routes

