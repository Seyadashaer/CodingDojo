from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!" 

@app.route("/dojo")
def dojo():
    return "Dojo"

@app.route("/say/<name>")
def say_hi(name):
    return f"Hi {name}"

@app.route("/repeat/<times>/<word>")
def repeat_word(times, word):
    return f"{word} " * int(times)

if __name__ == "__main__":
    app.run(debug = True)