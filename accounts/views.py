from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from .serializers import UserCreateAccountSerializers, ProfileSerializers


class UserCreateApiView(CreateAPIView):
    """
    creat user
    """
    queryset = User.objects.all()
    serializer_class = UserCreateAccountSerializers
    

class ProfileApiview(RetrieveUpdateDestroyAPIView):
    """
    update and show and delete user
    and user must authenticated 
    """
    queryset = User.objects.all()
    serializer_class = ProfileSerializers
    # permission_classes = (IsAuthenticated, )