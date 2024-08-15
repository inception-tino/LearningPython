from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to flask application"

@app.route('/about')
def about():
    return "c394 application building session"

@app.route('/details')
def details():
    return "Python programming"

if __name__ == '__main__':
    app.run(debug=True)
