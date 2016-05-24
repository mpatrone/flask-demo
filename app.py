from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/')
def main():
    return 'Hi ! Im a Flask application.'

@app.route('/hi')
def hello():
    return '<h1>Hello Manuel</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0')