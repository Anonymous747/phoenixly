from django.db import models


# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=20)
    shareLink = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Folder(models.Model):
    name = models.CharField(max_length=20)
    parent_collection_id = models.TextField(max_length=20, null=True)
    parent_folder = models.TextField(max_length=20, null=True)

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.TextField(max_length=50)
    parent_folder_id = models.TextField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True, auto_created=True)
    date_modified = models.DateTimeField(auto_now_add=True, auto_created=True)
    language = models.CharField(max_length=4)

    # TODO: tags
    # TODO: related

    def __str__(self):
        return self.name


class Note(models.Model):
    parent_document_id = models.TextField(max_length=20)
    title = models.TextField(max_length=30)
    body = models.TextField()

    def __str__(self):
        return self.title