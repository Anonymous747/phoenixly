from django.urls import path, include
from rest_framework import routers

from src.library.views import CollectionsView

router = routers.DefaultRouter()
router.register('collections', CollectionsView, basename='collections')

urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += router.urls
