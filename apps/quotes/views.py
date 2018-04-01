# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login.models import Userdb
from .models import Quote
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

# Create your views here.
def quotes(request):

    context = {
        'user' : Userdb.objects.get(id = request.session['user_id']),
        'quotes' : Quote.objects.all().exclude(fav=request.session['user_id']),
        
        'favs' : Quote.objects.filter(fav=request.session['user_id']),
    }
    return render(request, 'quotes/quotes.html', context)

def post_quote(request):

    print request.POST
    validations = Quote.objects.validator(request.POST)
    if len(validations) > 0:
        for e in validations:
            messages.error(request, e)
    else:
        user_id = Userdb.objects.get(id=request.session['user_id'])
        Quote.objects.creator(request.POST, user_id)

    return redirect ('/quotes')

def add_list(request, quote_id):

    quote_id = Quote.objects.get(id=quote_id).id
    user_id = Userdb.objects.get(id=request.session['user_id']).id
    

    Quote.objects.get(id=quote_id).fav.add(Userdb.objects.get(id=user_id))

    return redirect ('/quotes')

def remove_list(request, fav_id):

    Quote.objects.get(id=fav_id).fav.remove(Userdb.objects.get(id=request.session['user_id']))
    
    return redirect ('/quotes')

def show(request, poster_id):

    context = {
        'poster' : Userdb.objects.get(id=poster_id),
        'count' : Quote.objects.filter(fav=poster_id).count(),
    }

    return render(request, 'quotes/show.html', context)

    


