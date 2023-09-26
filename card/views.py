from rest_framework.generics import ListCreateAPIView, DestroyAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import LinkSciolSerializers
from .models import LinkSciol
from main import Downloader


class LinkListApiView(APIView):
    def post(self, request: Request):
        link = LinkSciolSerializers(data=request.data)
        if link.is_valid():
            return Response(link.data, status=status.HTTP_201_CREATED)
        return Response(link.errors,status=status.HTTP_400_BAD_REQUEST)