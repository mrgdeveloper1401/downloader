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
    """start download when link is valid
    """
    
    def post(self, request: Request):
        try:
            # استفاده از request.data.get برای دسترسی به داده‌ها و جلوگیری از خطا در صورت عدم وجود فیلد
            request_link = request.data.get('link_url', None)
            print(request_link)
            fname = request.data.get('fname', None)
            
            # اگر فیلد‌ها وجود دارند، ادامه اجرا
            if request_link or fname:
                downloader = Downloader()
                downloader_link = downloader.download_file(downloader.insta_downloader(link=request_link), fname)
                data = {'downloader_link': downloader_link}
                return Response(data=data, status=status.HTTP_201_CREATED)
            else:
                # در صورت عدم وجود فیلد‌ها، پیام خطا مناسب را برمی‌گردانیم
                return Response(data={'messages': 'please enter valid link'}, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            # در صورت بروز خطا، ارسال پیام خطا و کد وضعیت مناسب
            return Response(data={'messages': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TwitterDownloadView(APIView):
    """start download when link is valid
    """
    
    def post(self, request: Request):
        try:
            # استفاده از request.data.get برای دسترسی به داده‌ها و جلوگیری از خطا در صورت عدم وجود فیلد
            request_link = request.data.get('link_url', None)
            print(request_link)
            fname = request.data.get('fname', None)
            
            # اگر فیلد‌ها وجود دارند، ادامه اجرا
            if request_link or fname:
                downloader = Downloader()
                downloader_link = downloader.download_file(downloader.twitter_downloader(link=request_link), fname)
                data = {'downloader_link': downloader_link}
                return Response(data=data, status=status.HTTP_201_CREATED)
            else:
                # در صورت عدم وجود فیلد‌ها، پیام خطا مناسب را برمی‌گردانیم
                return Response(data={'messages': 'please enter valid link'}, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            # در صورت بروز خطا، ارسال پیام خطا و کد وضعیت مناسب
            return Response(data={'messages': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class FacebookDownloadView(APIView):
    """start download when link is valid
    """
    
    def post(self, request: Request):
        try:
            # استفاده از request.data.get برای دسترسی به داده‌ها و جلوگیری از خطا در صورت عدم وجود فیلد
            request_link = request.data.get('link_url', None)
            print(request_link)
            fname = request.data.get('fname', None)
            
            # اگر فیلد‌ها وجود دارند، ادامه اجرا
            if request_link or fname:
                downloader = Downloader()
                downloader_link = downloader.download_file(downloader.facebook_downloader(link=request_link), fname)
                data = {'downloader_link': downloader_link}
                return Response(data=data, status=status.HTTP_201_CREATED)
            else:
                # در صورت عدم وجود فیلد‌ها، پیام خطا مناسب را برمی‌گردانیم
                return Response(data={'messages': 'please enter valid link'}, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            # در صورت بروز خطا، ارسال پیام خطا و کد وضعیت مناسب
            return Response(data={'messages': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    
    
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