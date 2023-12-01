from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

Users = get_user_model()

class User(models.Model):
    user_name = models.ForeignKey(Users, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    password = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    created_at = models.DateTimeField(default=datetime.now)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user_name.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    created_at = models.DateTimeField(default=datetime.now)
    like = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user
    
class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    user_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user_name

class Follower(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user

class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    location_name = models.CharField(max_length=500, blank=False)
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)
    
    def __str__(self):
        return (f'{self.location_name} {self.latitude} {self.longitude}')