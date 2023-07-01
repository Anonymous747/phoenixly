from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import Collection, Folder, Document, Note, Tag


class TagSerializer(serializers.ModelSerializer):
    # text = SlugRelatedField(
    #     many=True,
    #     queryset=Tag.objects.all(),
    #     slug_field='text'
    # )

    class Meta:
        model = Tag
        fields = ('text',)


class NoteSerializer(serializers.ModelSerializer):
    # tags = serializers.SlugRelatedField(
    #     many=True,
    #     queryset=Note.objects.filter(tags__text='text'),
    #     slug_field='notes'
    # )

    class Meta:
        ordering = ['-id']
        model = Note
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'
