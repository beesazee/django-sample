from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    value = request.session.get('strategy',0)

    if 0 == value:
        request.session['strategy'] = 1
        return HttpResponse("It's a six one way .!!!")

    else:
        #request.session['strategy'] = 0
        request.session['strategy'] += 1
        return HttpResponse("It's a half way .!! and the session hit count : {}".format(request.session['strategy']))