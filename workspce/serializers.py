from rest_framework import serializers
from .models import WorkspaceModel


class WorkspaceSerializers(serializers.ModelSerializer):
    workspace_user = serializers.StringRelatedField()
    class Meta:
        model = WorkspaceModel
        fields = '__all__'
        
        extra_kwargs = {
            'workspace_user': {"read_only": True},
            'is_active': {'read_only': True},
            
        }