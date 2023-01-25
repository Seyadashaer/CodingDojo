from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key = 'gjergoij9485'

@app.route('/')
def index(): 
    if 'total_gold' not in session:
        session['total_gold'] = 0 
    return render_template("index.html")

def createRandom(min,max):
    earned_gold = random.randrange(min, max)
    session['total_gold'] += earned_gold

@app.route('/process_money', methods = ["GET", "POST"])
def process_money():
    if request.form['building'] == 'farm':
        createRandom(10,20)
    if request.form['building'] == 'cave':
        createRandom(5,10)    
    if request.form['building'] == 'house':
        createRandom(2,5)
    if request.form['building'] == 'casino':
        createRandom(-50,50)
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)


