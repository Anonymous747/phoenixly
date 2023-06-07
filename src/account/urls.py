from django.urls import path, include

urlpatterns = [
    path('login/', include('rest_framework.urls'))
]
