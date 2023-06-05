from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Collection
from .serializer import CollectionSerializer


def collection_list(request):
    print('Gel in')
    if request.method == 'GET':
        data = Collection.objects.all()
        serializer = CollectionSerializer(data)
        return Response(serializer.data)
    elif request.method == "POST":
        print('post')
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)