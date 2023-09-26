# from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.request import Request
# from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404
# from .models import WorkspaceModel
# from .serializers import WorkspaceSerializers
# from permission import IsOwner
# from django.db import reset_queries, connection


# class WorkspaceCreateApiView(CreateAPIView):
#     serializer_class = WorkspaceSerializers
#     permission_classes = (IsAuthenticated, IsOwner)

#     def get_queryset(self):
#         print(reset_queries)
#         return WorkspaceModel.objects.filter(is_active=True, workspace_user = self.request.user)

# class WorkspaceListApiView(ListAPIView):
#     reset_queries()
#     serializer_class = WorkspaceSerializers
#     permission_classes = (IsAuthenticated, IsOwner)
    
#     def get_queryset(self):
#         print(connection.queries)
#         return WorkspaceModel.objects.filter(is_active=True, workspace_user = self.request.user).select_related('workspace_user', )


# class WorkspaceEditApiView(RetrieveUpdateAPIView):
#     serializer_class = WorkspaceSerializers
#     permission_classes = (IsAuthenticated, IsOwner)
    
#     def get_queryset(self):
#         return WorkspaceModel.objects.filter(is_active=True, workspace_user = self.request.user)


# class WorkspaceDeleteApiView(APIView):
#     permission_classes = (IsAuthenticated, IsOwner)
    
#     def delete(self, request: Request, pk):
#         workspace = get_object_or_404(WorkspaceModel, pk=pk)
#         self.check_object_permissions(request, workspace)
#         if workspace.is_active == False:
#             return Response({'message': 'workspace not found'})
#         workspace.is_active = False
#         workspace.save()
#         return Response({"message": 'succesfly delete workspace'}, status=status.HTTP_200_OK)
        