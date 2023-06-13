from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from . import views
from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView

# router = DefaultRouter()
# router.register('registration', RegisterView)

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user', UserRetrieveUpdateAPIView.as_view()),
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view())
]
