from flask import Flask

from methods import db_check_connection

app = Flask(__name__)  

@app.route('/')  
def home():  
    return "Hello, Docker Swarm!"  

@app.route('/test')
def test():
    return "test"

@app.route('/check_db')
def check_db():
    return db_check_connection()

@app.route('/result/<x>/<y>')
def result(x, y):
    add = x + y
    return add


if __name__ == "__main__":  
    app.run(host="0.0.0.0", port=5000)  
