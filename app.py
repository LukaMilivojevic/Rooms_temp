from flask import Flask,jsonify,request,render_template
#from psycopg2 import connect
import psycopg2

import os

url = os.environ.get('DATABASE_URL')
connection = psycopg2.connect(url)
app = Flask(__name__)
CREATE_TABLE = """CREATE TABLE IF NOT EXISTS rooms (
                id SERIAL PRIMARY KEY,
                name TEXT);
            """


"""
{
  "name": "Room name",
  "temperatures": [
    {"date": "2022-03-10", "temperature": 13.4},
    {"date": "2022-03-09", "temperature": 14.4},
    {"date": "2022-03-08", "temperature": 17.4},
    {"date": "2022-03-07", "temperature": 13.4},
    {"date": "2022-03-06", "temperature": 13.4},
    {"date": "2022-03-05", "temperature": 16.4},
    {"date": "2022-03-04", "temperature": 13.4},
  ],
  "average": 15.7
}
"""

@app.route("/")
def home_view():
        return "<h1>Welcome to rooms temp control</h1>"
  

# POST /api/room {'name':room_name}
@app.route('/api/room',methods=['POST'])
def create_room():
    data = request.get_json()
    name = data['name']
    with connection:
        cursor = connection.cursor()
        cursor.execute(CREATE_TABLE)
    return {"id": 2, "message": f"Room {name} created."}
  

if __name__ == "__main__":
        app.run()