from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import Collection, Folder, Document, Note, Tag


class TagSerializer(serializers.ModelSerializer):
    tags = SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Tag
        fields = ('text', 'tags')


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='title'
    )

    class Meta:
        model = Note
        fields = '__all__'
