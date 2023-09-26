from rest_framework.generics import ListCreateAPIView
from .serializers import SciolSerializers
from .models import HomeModel


class SciolListCreateApiview(ListCreateAPIView):
    serializer_class = SciolSerializers
    
    def get_queryset(self):
        return HomeModel.objects.all()


