from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)

app.secret_key = "my_secret2"

@app.route("/")
def index():
	if "target_number" not in session:
		session["target_number"] = random.randint(1, 101)
	return render_template("index.html")

@app.route("/process", methods=["POST"])
def Process():
	if int(request.form["guess_number"]) == session["target_number"]:
		session["result"] = "Correct"
	elif int(request.form["guess_number"]) > session["target_number"]:
		session["result"] = "high"
	else:
		session["result"] = "low"
	return redirect("/")

@app.route("/replay")
def play_Again():
	session.pop("target_number")
	session.pop("result")
	return redirect("/")

if __name__ == "__main__":
	app.run(debug=True)