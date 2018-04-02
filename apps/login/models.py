# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re, bcrypt
# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^.{8,}$')


# Create your models here.
class UserdbManager(models.Manager):
    def validator(self, postData):
        errors=[]
        # check if email exists first before moving forward
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("Invalid Email")
        else: 
            query = self.filter(email = postData['email'])
            if len(query) > 0:
                errors.append("Email exists, please log in")

        if len((postData['name'])) < 3:
            errors.append("Name must be at least 2 characters")
        elif not postData['name'].isalpha():
            errors.append("Name cannot contain letters")

        if len(postData['alias']) < 3: 
            errors.append("Alias must be at least 2 characters")
        
        if not PASSWORD_REGEX.match(postData['password']):
            errors.append("Password must be at least 8 characters")

        if postData['confirm_pw'] != postData['password']:
            errors.append("Password do not match")

        if len(postData['dob']) == 0:
            errors.append("Date of Birth cannot be blank")
        
        return errors

    def creator(self, cleanData):
        hashed_pw = bcrypt.hashpw(cleanData['password'].encode(), bcrypt.gensalt())
        return self.create(
            name = cleanData['name'],
            alias = cleanData['alias'],
            email = cleanData['email'],
            password = hashed_pw,
            dob = cleanData['dob'],
        )

    def login(self, loginData):
        errors = []

        if not self.filter(email = loginData['email']):
            errors.append("Invalid Login")
        else:
            dbpw = self.get(email=loginData['email']).password.encode()
            user_pw = loginData['password'].encode()         

            if not bcrypt.checkpw(user_pw, dbpw):
                errors.append("invalid Login")

        return errors
    
class Userdb(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, unique=True)
    email= models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    dob= models.DateField(auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserdbManager()


