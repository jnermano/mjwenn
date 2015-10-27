# -*- coding: utf8 -*-
from django.db import models
from django.template.defaultfilters import default
import os
from datetime import datetime
from django.contrib.auth.models import User
from mjwenn.settings import MEDIA_ROOT

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "IMG_" + datetime.now().strftime("%Y%m%d%H%M%S")+"."+ext
    return 'uploads/'+filename

def get_avatar_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "IMG_" + datetime.now().strftime("%Y%m%d%H%M%S")+"."+ext
    return 'avatars/'+filename

    
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    site_web = models.URLField()
    avatar = models.FileField(blank=True, null=True, upload_to=get_avatar_path, default='avatars/user1.png')
    is_active = models.BooleanField(default=False)
    hach = models.CharField(default="", null=True, blank=True, max_length=255)

    def __str__(self):
        return self.user.username

class Address(models.Model):
    user = models.ForeignKey(Profile)
    contact_name = models.CharField(max_length=100, default=" ")
    contact_tel = models.CharField(max_length=20, default=" ")
    contact_email = models.EmailField(default=" ")
    contact_place = models.CharField(max_length=255, default=" ")
    desc = models.CharField(max_length=255, default=" ")
    lat = models.DecimalField(null=True, blank=True, decimal_places=10, max_digits=18)
    lon = models.DecimalField(null=True, blank=True, decimal_places=10, max_digits=18)
    add_date = models.DateTimeField()
    
    def __str__(self):
        return models.Model.__str__(self)
    

class Category(models.Model):
    category = models.CharField(max_length=50)
    desc = models.CharField(max_length=255)
    #date_add
    
    def __str__(self):
        return self.category

class Type(models.Model):
    type = models.CharField(max_length=50)
    desc = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    
    def __str__(self):
        return self.type

    
class Annonce(models.Model):
    user = models.ForeignKey(Profile, null=True)
    address = models.ForeignKey(Address, null=True)
    type_annonce = models.IntegerField()
    category = models.ForeignKey(Category)
    type = models.ForeignKey(Type)
    owner_first_name = models.CharField(max_length=50)
    owner_last_name = models.CharField(max_length=50)
    owner_email = models.EmailField()
    picture = models.FileField(upload_to=get_file_path)
    pub_date = models.DateTimeField()
    returned = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    
    
    
    def __str__(self):
        return self.owner_first_name + ' ' + self.owner_last_name
    

