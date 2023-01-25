from django.shortcuts import render, redirect
import random



def index(request):
	if "target_number" not in request.session:
		request.session["target_number"] = random.randint(1, 101)
	return render(request, "index.html")


def process(request):
    if request.method == "POST":
        guess_number_from_form = int(request.POST["guess_number"])
    if guess_number_from_form > request.session['target_number']:
        request.session["result"] = "high"
    elif guess_number_from_form < request.session['target_number']:
        request.session["result"] = "low"
    else:
        request.session["result"] = "correct"
    return render(request, 'index.html')

def play_Again(request):
    del request.session['target_number']
    del request.session["result"]
    return redirect('/')
    