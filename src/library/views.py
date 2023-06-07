from rest_framework import status, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Collection
from .serializer import CollectionSerializer
from src.core.permissions import CollectionPermission


class CollectionsView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    permission_classes = (CollectionPermission,)
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
