from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return str(self.pk)

class Comments(models.Model):
    comment = models.CharField(max_length=300)
    post_id = models.CharField(max_length=200)

    def __str__(self):
        return self.comment