from rest_framework.serializers import ModelSerializer
from .models import Collection, Folder, Document, Note


class CollectionSerializer(ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


class FolderSerializer(ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'


class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
