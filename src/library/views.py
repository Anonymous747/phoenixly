from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import Collection, Folder, Document, Note, Tag
from .serializer import CollectionSerializer, FolderSerializer, \
    DocumentSerializer, NoteSerializer, TagSerializer
from src.core.permissions import CollectionPermission


class TagViewSet(ModelViewSet):
    permission_classes = (CollectionPermission,)
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class CollectionsView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    permission_classes = (CollectionPermission,)
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FoldersView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    permission_classes = (CollectionPermission,)
    serializer_class = FolderSerializer
    queryset = Folder.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DocumentsView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    permission_classes = (CollectionPermission,)
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NotesView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
