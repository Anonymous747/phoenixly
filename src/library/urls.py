from django.urls import path, include
from rest_framework import routers

from src.library.views import CollectionsView, FoldersView,\
    DocumentsView, NotesView

router = routers.DefaultRouter()
router.register('collections', CollectionsView, basename='collections')
router.register('folders', FoldersView, basename='folders')
router.register('documents', DocumentsView, basename='documents')
router.register('notes', NotesView, basename='notes')

urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += router.urls
