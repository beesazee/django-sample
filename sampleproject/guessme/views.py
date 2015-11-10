from django.shortcuts import render,HttpResponse,redirect,render_to_response
from random import randint

# Create your views here.
def reset_game(request,**param):
    if param['winflag']:
        request.session['content'] = 'you won :) !!!'
    else:
        request.session['content'] = 'you lost, loser .!!!'

    request.session.pop('chance')
    request.session.pop('rand_value')
    request.session.pop('user_value')

def check4win(request):
    if request.session.get('user_value') == request.session.get('rand_value'):
        reset_game(request,winflag=True)

def do_play(request, template_name = 'do_play.html'):
    if not ('rand_value' in request.session):
        request.session['rand_value'] = randint(1,1000)
    if request.session.get('chance') > 10:
        reset_game(request,winflag=False)

    if request.POST and request.POST['user_value']:
        user_value = int(request.POST['user_value'])
        request.session.setdefault('user_value',[]).append(user_value)
        check4win(request)
        request.session['chance'] = request.session.get('chance',1) + 1
    return render(request, template_name,{
        'user_value':request.session.get('user_value',[]),
        'rand_value':request.session.get('rand_value',0),
        'counter':request.session.get('chance',1),
        'content':request.session.get('content'),
    })
