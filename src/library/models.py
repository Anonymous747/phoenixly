from django.db import models
from django.db.models import CASCADE

from src.account.models import User


class Tag(models.Model):
    text = models.CharField(max_length=64)

    def __str__(self):
        return self.text


class Collection(models.Model):
    user = models.ForeignKey(User, related_name='users_collection', on_delete=CASCADE, null=True)
    name = models.CharField(max_length=20)
    shareLink = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Folder(models.Model):
    name = models.CharField(max_length=20)
    parent_collection_id = models.ForeignKey(Collection, related_name="folders_parent_collection",
                                             on_delete=CASCADE, null=True,)
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
    related_folder = models.ForeignKey(Folder, related_name='document_related_folder', on_delete=CASCADE, null=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    parent_document_id = models.TextField(max_length=20)
    title = models.TextField(max_length=30, default='')
    body = models.TextField(default='')
    tags = models.ForeignKey(Tag, related_name='note_tags', on_delete=CASCADE, null=True)

    def __str__(self):
        return 'Note[id: {id}, name: {title}]'.format(id=self.id, title=self.title)
