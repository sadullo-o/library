from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_at =  models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    data = models.CharField(max_length=999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    # data = models.ImageField()




class Types(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Tovarlar(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=250)
    cost = models.CharField(max_length=100)
    type = models.ForeignKey(Types, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Korzina(models.Model):
    username = models.CharField(max_length=100)
    tovarnomi = models.CharField(max_length=100)
    tovarnarxi = models.CharField(max_length=100)
    tovarsoni = models.IntegerField()
    tovarumumiynarx = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.username)+ ' ' + str(self.tovarnomi)


class Zakaz(models.Model):
    username = models.CharField(max_length=100)
    tovarnomi = models.CharField(max_length=100)
    tovarnarxi = models.CharField(max_length=100)
    tovarsoni = models.IntegerField()
    tovarumumiynarx = models.CharField(max_length=100)

    def __str__(self):
        return str(self.username) + ' ' + str(self.tovarnomi)
