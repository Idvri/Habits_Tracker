from rest_framework import generics

from users.serializers import RegistrationSerializer


# Create your views here.
class RegistrationApiView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

    def perform_create(self, serializer):
        new_user = serializer.save()
        new_user.set_password(new_user.password)
        new_user.save()
