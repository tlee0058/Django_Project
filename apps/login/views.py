# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Userdb
from ..quotes.models import Quote
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    if 'user_id' not in request.session:
        request.session['user_id'] = 0

    return render(request, 'login/index.html')


def register(request):
    validations = Userdb.objects.validator(request.POST)
    if len(validations) > 0:
        for e in validations:
            messages.error(request, e)

    else:
        Userdb.objects.creator(request.POST)
        messages.add_message(request, messages.INFO, "Registration success! You may login")
    
    return redirect ('/main')

def login(request):
    validations = Userdb.objects.login(request.POST)
    if len(validations) > 0:
        for e in validations:
            messages.error(request, e)
        return redirect ('/main')
        
    else:
        user = Userdb.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        return redirect("/quotes")

def logout(request):
    request.session.clear()
    return redirect ('/main')