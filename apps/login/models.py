from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

emailRegEx = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def validatorLogin(self, postData):
        emailRegEx = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors={}
        if postData['email'] =='' or postData['password'] == '':
            errors['login'] = 'Cannot leave fields blank'
            return errors
        if not emailRegEx.match(postData['email']):
            errors['login'] = 'Invalid email'
            return errors
        if not User.objects.filter(email = postData['email']):
            errors['login'] = 'Unable to login'
            return errors
        userOb = User.objects.get(email = postData['email'])
        if not bcrypt.checkpw(postData['password'].encode(), userOb.password.encode()):
            errors['login'] = 'Unable to login'
            return errors
        print('we cool honey bunny')
        return errors

    def validatorReg(self, postData):
        errors={}
        if postData['email'] =='' or postData['password'] == '' or postData['fName'] == '' or postData['lName'] == '':
            errors['reg'] = 'Cannot leave fields blank'
            return errors
        if len(postData['fName']) <= 2 or len(postData['lName']) <= 2:
            errors['reg'] = 'Name must be longer than 2 characters'
        if postData['fName'].isalpha() == False or postData['lName'] == False:
            errors['reg'] = 'Name can only contain letters'
        if not emailRegEx.match(postData['email']):
            errors['reg'] = 'Invalid email'
            return errors
        if User.objects.filter(email = postData['email']):
            errors['reg'] = 'Email already exists'
            return errors
        if len(postData['password']) < 8:
            errors['reg'] = 'Password must be 8 characters'
            return errors
        if postData['password'] != postData['confPassword']:
            errors['reg'] = 'Passowrds do not match'
            return errors
        return errors
        

class User(models.Model):
    fName = models.CharField(max_length=255)
    lName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    hId = models.CharField(max_length=255, default = None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()