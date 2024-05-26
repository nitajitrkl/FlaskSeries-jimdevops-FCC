from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!!!'


@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/hello')
def hello():
    return render_template('hello.html')
