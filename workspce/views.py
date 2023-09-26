from rest_framework.generics import ListCreateAPIView
from .serializers import SciolSerializers
from .models import HomeModel


class SciolListCreateApiview(ListCreateAPIView):
    """
    See all social network names in the get method,,,,,,,
    In the post method, the user first selects one of the social networks and then by entering the link, she can download it
    """
    
    serializer_class = SciolSerializers
    
    def get_queryset(self):
        return HomeModel.objects.all()


