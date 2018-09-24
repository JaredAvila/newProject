from __future__ import unicode_literals
from django.db import models
from apps.login.models import User

class WishManager(models.Manager):
    def validator(self, postData):
        errors={}
        if postData['desc'] == '':
            errors['valid'] = 'Must enter a description'
            return errors
        if len(postData['wish'] ) < 4:
            errors['valid'] ='Wish must be at least 3 characters'
            return errors
        if len(postData['desc'] ) < 4:
            errors['valid'] ='Description must be at least 3 characters'
            return errors
        # print(postData['wish'])
        return errors

class Wish(models.Model):
    wish = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    userWish = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name='userLikes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WishManager()

class Granted(models.Model):
    granted = models.CharField(max_length=255)
    grantedDesc = models.TextField(max_length=1000)
    wishCreatedAt = models.CharField(max_length=255, default=None)
    wisher = models.CharField(max_length=255, default=None)
    grantedLikes = models.ManyToManyField(User, related_name='user_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)