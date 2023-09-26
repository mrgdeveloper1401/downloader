# from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
# from rest_framework.permissions import IsAuthenticated
# from .serializers import CardSerializers
# from .models import CardModel
# from permission import IsOwner


# class CardListApiview(ListAPIView):
#     serializer_class = (CardSerializers)
#     permission_classes = (IsAuthenticated, )
    
#     def get_queryset(self):
#         return CardModel.objects.filter(is_active=True, user=self.request.user)
    
    
# class CardCreateApiView(CreateAPIView):
#     serializer_class = CardSerializers
#     permission_classes = (IsAuthenticated, )
    
#     def get_queryset(self):
#         return CardModel.objects.filter(user = self.request.user)
    

# class CardShowUpdate(RetrieveUpdateAPIView):
#     serializer_class = CardSerializers
#     permission_classes = (IsAuthenticated, )
    
#     def get_queryset(self):
#         return CardModel.objects.filter(user = self.request.user, is_active=True)