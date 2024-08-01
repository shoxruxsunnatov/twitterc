from django.db import models
from django.contrib.auth.models import User

from main.utils import generate_filename


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    bio = models.CharField(max_length=200, default='', blank=True)
    profile_image = models.ImageField(upload_to='media/images/', blank=True, null=True)
    header_image = models.ImageField(upload_to='media/images/', blank=True, null=True)

    def __str__(self):
        return self.fullname


class Tweet(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    text = models.TextField(max_length=280)
    date = models.DateTimeField(auto_now_add=True)
    views = models.BigIntegerField(default=0)
    likes = models.BigIntegerField(default=0)

    class Meta:
        ordering = ['-id']

        
    def __str__(self):
        return f'{self.account.user.username} {self.date}'


class TweetImage(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='tweet')
    image = models.ImageField(upload_to=generate_filename)


    def __str__(self):
        return self.image.name
