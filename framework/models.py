from email.policy import default
from platform import release
from pyexpat import model
from tkinter import CASCADE
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

class Artiste(models.Model):
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name 

class Song(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(default=datetime.today)
    likes = models.IntegerField()
    artist_id = models.ForeignKey(Artiste, on_delete= models.CASCADE)

    def __str__(self):
        return self.title

class Lyrics(models.Model):
    content = models.CharField(max_length=1000)
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)

    def __str__(self):
        return self.content