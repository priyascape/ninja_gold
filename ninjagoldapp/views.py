
from django.shortcuts import render,redirect
from .models import *
import random


def index(request):
    if 'goldcreated' in request.session:
        print("this is my gold", request.session['gold'])
        request.session['gold'] = request.session['gold'] + request.session['goldcreated']
    else:
        request.session['act_log'] = []
        request.session['goldcreated'] = 0
        request.session['gold'] = 0
    return render(request, 'index.html')

def process_money(request):
    if request.POST['building'] == 'farm':
        request.session['goldcreated'] = random.randint(10,20)
        request.session['act_log'].append(f"you add this much gold {request.session['goldcreated']}")
        
    if request.POST['building'] == 'cave':
        request.session['goldcreated'] = random.randint(5,10)
        request.session['act_log'].append(f"you add this much gold {request.session['goldcreated']}")
        
    if request.POST['building'] == 'house':
        request.session['goldcreated'] = random.randint(2,5)
        request.session['act_log'].append(f"you add this much gold {request.session['goldcreated']}")
        
    if request.POST['building'] == 'casino':
        request.session['goldcreated'] = random.randint(-50,50)
        request.session['act_log'].append(f"you add this much gold {request.session['goldcreated']}")
        
    return redirect ('/')

def destroy(request):
    request.session.flush()
    return redirect('/')