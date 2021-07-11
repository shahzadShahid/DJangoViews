from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) #max_length = required
    description = models.TextField(blank=True, null=True)
    price       = models.FloatField() #both input inside class required
    summary     = models.TextField()
    feature     = models.BooleanField(default=True) #null=True default=True

    def get_url(self):
        return reverse('products:product-detail',kwargs={'id':self.id})