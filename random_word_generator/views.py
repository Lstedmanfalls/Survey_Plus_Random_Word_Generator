from django.shortcuts import render, redirect, HttpResponse, resolve_url
from django.utils.crypto import get_random_string

def index(request):
    if 'attempts' not in request.session:
        request.session['attempts'] = 1
    else:
        request.session['attempts'] += 1    
    
    context = {
    'rand_word': get_random_string(length=4, allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    }
    return render(request,'random.html', context)

def reset(request):
    request.session.flush()
    return redirect("/random")
