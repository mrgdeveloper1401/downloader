from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from .serializers import LinkSciolSerializers
from .models import LinkSciol


class LinkSciolListCreateApiView(ListCreateAPIView):
    """
    You can see the download link,,,,
    In the post method, it can create a download link
    """
    
    serializer_class = LinkSciolSerializers
    queryset = LinkSciol.objects.all()
    

class LinkSciolDelete(DestroyAPIView):
    """
    
    """
    queryset = LinkSciol.objects.all()
    serializer_class = LinkSciolSerializers