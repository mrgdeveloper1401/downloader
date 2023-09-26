from rest_framework.generics import ListCreateAPIView, DestroyAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import LinkSciolSerializers
from .models import LinkSciol
from main import Downloader


class LinkListApiView(APIView):
    serializer_class = LinkSciolSerializers
    
    def post(self, request: Request):
        link_type = request.data.get('link_type')
        link_url = request.data.get('link_url')

        # Check the link type and call the appropriate download method
        downloader = Downloader()

        if link_type == 'instagram':
            file_path = downloader.insta_downloader(link_url)
        elif link_type == 'facebook':
            file_path = downloader.facebook_downloader(link_url)
        elif link_type == 'twitter':
            file_path = downloader.twitter_downloader(link_url)
        else:
            return Response({'error': 'Invalid link type'}, status=status.HTTP_400_BAD_REQUEST)

        # Save the file path or link to the database (assuming LinkSciol model has a 'file_path' field)
        link_sciol = LinkSciol.objects.create(file_path=file_path)

        # Serialize the response
        serializer = LinkSciolSerializers(link_sciol)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
