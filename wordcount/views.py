from django.http import HttpResponse

def homepage(request):
    return HttpResponse('Hello')

def eggs(request):
    return HttpResponse('<h1>Eggs are great!</h1>')