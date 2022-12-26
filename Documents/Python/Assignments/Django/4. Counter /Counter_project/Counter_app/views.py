from django.shortcuts import render, redirect

def count(request):
    if 'count' in request.session:
        request.session['count'] += 1 
    else:
        request.session['count'] = 0 
    return render(request, 'index.html')

def destroy_session(request): 
    del request.session['count']
    return redirect ('/')

def add_two(request):
    request.session['count'] += 2
    return render(request, 'index.html')
