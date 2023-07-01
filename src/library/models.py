from django.db import models
from django.db.models import CASCADE


class Tag(models.Model):
    text = models.CharField(max_length=64)

    def __str__(self):
        return 'Tag[id: {id}, text: {text}]'.format(
            id=self.id, text=self.text
        )


class Collection(models.Model):
    name = models.CharField(max_length=20)
    shareLink = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Folder(models.Model):
    name = models.CharField(max_length=20)
    parent_collection_id = models.ManyToManyField(Collection, related_name="folder")
    parent_folder = models.TextField(max_length=20)

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.TextField(max_length=50)
    parent_folder_id = models.TextField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True, auto_created=True)
    date_modified = models.DateTimeField(auto_now_add=True, auto_created=True)
    language = models.CharField(max_length=4)
    tags = models.ManyToManyField(Tag)
    related_folder = models.ManyToManyField(Folder)

    def __str__(self):
        return self.name


class Note(models.Model):
    parent_document_id = models.TextField(max_length=20)
    title = models.TextField(max_length=30, default='')
    body = models.TextField(default='')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return 'Note[id: {id}, name: {title}]'.format(id=self.id, title=self.title)
