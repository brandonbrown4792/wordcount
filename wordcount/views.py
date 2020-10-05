from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html', {'hithere': 'This is me'})

def count(request):
    return render(request, 'count.html')