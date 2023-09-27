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
            fname = request.data['fname']
        except KeyError:
            return Response(data={'messages': 'please enter valid link'})
        
        downloader = Downloader()
        downloader_link = downloader.download_file(
            Downloader.insta_downloader(
                link=request_link
            ),
            fname
        )
        
        data = {
            'download_link': downloader_link
        }
        return Response(data=data, status=status.HTTP_201_CREATED)
    
class deleteLinkApiView(APIView):
    """delete file download
    """
    serializer_class = LinkSerializers
    
    def delete(self, request: Request, pk):
        try:
            link = LinkSciol.objects.get(pk=pk)
            link.delete()
            return Response({"messages": 'successfly deleted link'})
        except LinkSciol.DoesNotExist:
            return Response({"messages": 'not found'})