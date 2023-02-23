from django.db import models

# Create your models here.


class Passwords(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    siteurl = models.URLField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username
