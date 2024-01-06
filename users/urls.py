from django.urls import path

from users.apps import UserConfig
from users.views import RegistrationApiView, AuthApiView

app_name = UserConfig.name

urlpatterns = [
   path('register', RegistrationApiView.as_view(), name='register'),
   path('auth', AuthApiView.as_view(), name='token_obtain_pair'),
]
