from django.urls import path

from library import views

urlpatterns = [
    path('collections/', views.collection_list)
]
