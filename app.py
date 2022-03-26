from flask import Flask,jsonify,request,render_template
from psycopg2 import connection

import os

url = os.environ.get('DATABASE_URL')