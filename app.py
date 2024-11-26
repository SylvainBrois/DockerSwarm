from flask import Flask, redirect

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


@app.route('/redirect_amazon')
def redirect_amazon():
    return redirect("https://www.amazon.fr")




if __name__ == "__main__":  
    app.run(host="0.0.0.0", port=5000)  
