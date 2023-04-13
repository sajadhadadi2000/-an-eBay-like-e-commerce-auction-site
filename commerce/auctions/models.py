from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    pass

class List(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField()
    categories = (
        ('E', 'Electronics'),
        ('F', 'Fashion'),
        ('T', 'Toys'),
        ('H', 'Home'),
        ('S', 'Sport'),
        ('O', 'Other')
    )
    category = models.CharField(max_length=1, choices=categories)
    start_bid = models.FloatField(max_length=4)
    url_image = models.URLField(max_length=1000,blank=True)
    status = models.BooleanField(default=True)
    #wonlist = models.ForeignKey(User, on_delete=models.CASCADE, related_name="won", default='')
    def __str__(self):
        return f"{self.title}--{self.category}--{self.start_bid}"

class Coments(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name="comments")
    coment = models.TextField()
    def __str__(self):
        return f"{self.list}"

class Bid(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    bid = models.DecimalField(max_digits=4, decimal_places=2)
    
    

class Watchlist(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name="watchlist")
