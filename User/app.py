import Flask from flask
app= Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hellohello</h1>'

if __name__ == "__main__":
    app.run()