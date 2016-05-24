from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/hi')
def main():
    return '<h1>Hello Manuel</h1>'

@app.route('/')
def main():
    return 'Hi ! Im a Flask application.'

if __name__ == '__main__':
    app.run(host='0.0.0.0')