from rest_framework import generics

from rest_framework_simplejwt.views import TokenObtainPairView

from drf_spectacular.utils import extend_schema

from users.serializers import RegistrationSerializer


# Create your views here.
@extend_schema(summary="Зарегистрироваться.")
class RegistrationApiView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

    def perform_create(self, serializer):
        new_user = serializer.save()
        new_user.set_password(new_user.password)
        new_user.save()


@extend_schema(summary="Войти.")
class AuthApiView(TokenObtainPairView):
    pass
