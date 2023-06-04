from django.db import models


# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=20)
    shareLink = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Folder(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
