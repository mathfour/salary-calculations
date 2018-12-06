from flask import Flask, render_template, request
# from models import db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/calculate')
def calculate(a, b):
    return render_template('answer.html', product = a * b)


if __name__ == '__main__':
    app.run(debug=True)
