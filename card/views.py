from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import DestroyAPIView
from rest_framework import status
from .serializers import LinkRequestSerializer, DeleteSerializers
from main import Downloader
from .models import LinkSciol

class DownloadLinkAPIView(APIView):
    serializer_class = LinkRequestSerializer
    
    def post(self, request):
        serializer = LinkRequestSerializer(data=request.data)
        if serializer.is_valid():
            link_type = serializer.validated_data['link_type']
            link_url = serializer.validated_data['link_url']

            downloader = Downloader()
            if link_type == 'instagram':
                file_path = downloader.insta_downloader(link_url)
            elif link_type == 'facebook':
                file_path = downloader.facebook_downloader(link_url)
            elif link_type == 'twitter':
                file_path = downloader.twitter_downloader(link_url)
            else:
                return Response({'error': 'Invalid link type'}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'download_link': file_path}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class deleteLinkApiView(DestroyAPIView):
    """delete file download
    """
    serializer_class = DeleteSerializers
    queryset = LinkSciol.objects.all()