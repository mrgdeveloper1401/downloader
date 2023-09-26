from rest_framework.generics import ListCreateAPIView
from .serializers import LinkSciolSerializers
from .models import LinkSciol


class LinkSciolListCreateApiView(ListCreateAPIView):
    serializer_class = LinkSciolSerializers
    queryset = LinkSciol.objects.all()