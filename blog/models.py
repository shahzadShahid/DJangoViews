from typing import Text
from django.db import models
from django.db.models.fields import CharField, TextField
from django.shortcuts import render
from django.urls import reverse
class Article(models.Model):
    title   = CharField(max_length=70)
    content = TextField()
    active  = models.BooleanField(default=True)


    def get_absolute_url(self):
        return reverse('articles:article_detail', kwargs={'id':self.id})