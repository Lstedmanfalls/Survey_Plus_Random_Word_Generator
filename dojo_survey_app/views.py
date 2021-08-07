from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'index.html')

def show_page(request):
    if request.method == "POST":
            request.session['name'] = request.POST['name']
            request.session['location'] = request.POST['location']
            request.session['language'] = request.POST['language']
            request.session['comments'] = request.POST['comments']
    return redirect('/results')

def results(request):
    return render(request,'results.html')
