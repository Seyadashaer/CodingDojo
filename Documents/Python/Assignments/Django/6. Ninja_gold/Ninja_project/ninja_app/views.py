from django.shortcuts import render, redirect
import random

def index(request):
    if not 'total_gold' in request.session:
        request.session['total_gold'] = 0 
    context = {'total_gold': request.session['total_gold']}
    return render(request, 'index.html', context)


def process_money(request):
    if request.method == 'POST': 
        if request.POST['building'] == 'farm':
            earned_gold = random.randint(10,20)
            request.session['total_gold'] += earned_gold
            return redirect('/')
        if request.POST['building'] == 'cave':
            earned_gold = random.randint(5,10)
            request.session['total_gold'] += earned_gold    
            return redirect('/')
        if request.POST['building'] == 'house':
            earned_gold = random.randint(2,5)
            request.session['total_gold'] += earned_gold
            return redirect('/')
        if request.POST['building'] == 'casino':
            earned_gold = random.randint(-50,50)
            request.session['total_gold'] += earned_gold
            return redirect('/')
        
    else:
        return redirect('/')

def reset(request):
    request.session['total_gold'] = 0
    return redirect('/')
