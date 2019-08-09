from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, kubernetes! CI/CD\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
