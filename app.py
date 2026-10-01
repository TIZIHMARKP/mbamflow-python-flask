from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello MbamFlow Personal Project"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8082, debug=True)

    