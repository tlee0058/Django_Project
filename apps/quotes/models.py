# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login.models import Userdb
from django.db import models

# Create your models here.
class QuoteManager(models.Manager):
       
    def validator(self, postData):
        errors = []
        if len(postData['author']) < 4:
            errors.append("'Quoted By' must be at least 3 characters")
        if len(postData['message']) < 11:
            errors.append("Message must be at least 10 characters")
        
        return errors

    def creator(self, cleanData, id):
        return self.create(
            message = cleanData['message'],
            author = cleanData['author'],
            poster = id,
        )
    
    # def add_fav(self, postdata, quote_id, user_id):
    #     # quotes = Quote.objects.all()
    #     # quote_id = quotes.id
    #     # user = Userdb.objects.get(id=user_id)
    #     # user_id = user.id
        
    #         return self.get(id=quote_id).fav.add(Userdb.objects.get(id=user_id))

        # def joinTrip(self, trip_id, user):
        #     trip = Trip.objects.get(id=trip_id)
        # trip.group.add(user)
        # return (True, "Successfully added trip to your schedule!")
        
class Quote(models.Model):
    message= models.TextField()
    author= models.CharField(max_length=255)
    poster= models.ForeignKey(Userdb, related_name= "poster")
    fav = models.ManyToManyField(Userdb, related_name="favs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()

    def __str__(self):
        return "{}: {}".format(self.author, self.message)