from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import DestroyAPIView, ListAPIView
from rest_framework import status
from .serializers import  LinkSerializers
from main import Downloader
from rest_framework.request import Request
from .models import LinkSciol



class ShowLinkApiView(ListAPIView):
    serializer_class = LinkSerializers
    queryset = LinkSciol.objects.all()

class InstagramDownloadView(APIView):
    def post(self, request: Request):
        try:
            request_link = request.data['link_url']
            fname = request.data.get('fname')  # Using get to handle None if 'fname' is not present
        except KeyError:
            return Response(data={'messages': 'please enter a valid link'})
        
        # Create an instance of the Downloader class
        downloader = Downloader()
        
        # Call the insta_downloader method on the instance
        downloader_link = downloader.insta_downloader(link=request_link)
        
        data = {
            'download_link': downloader_link
        }
        return Response(data=data, status=status.HTTP_201_CREATED)

    
class deleteLinkApiView(DestroyAPIView):
    """delete file download
    """
    serializer_class = LinkSerializers
    queryset = LinkSciol.objects.all()