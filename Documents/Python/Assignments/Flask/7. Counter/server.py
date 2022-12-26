from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "helloworld"

@app.route('/')
def count():
    if not "count" in session:
        session['count'] = 1   
    return render_template('index.html')

@app.route('/reset', methods = ["POST"])
def reset():
    session['count'] = 0
    return redirect('/')

@app.route('/add', methods = ["POST"])
def add(): 
    session['count'] +=  2
    return redirect('/')

if __name__ =="__main__": 
    app.run(debug=True)
