from rest_framework import serializers

# from .models import WorkspaceModel
from .models import HomeModel
# from accounts.serializers import ProfileSerializers
# from card.serializers import CardSerializers


# class WorkspaceSerializers(serializers.ModelSerializer):
#     workspace_user = ProfileSerializers()
#     card = CardSerializers
#     class Meta:
#         model = WorkspaceModel
#         fields = '__all__'
        
#         extra_kwargs = {
#             # 'workspace_user': {'required': True},
#             'is_active': {'read_only': True},
            
#         }

class SciolSerializers(serializers.ModelSerializer):
    class Meta:
        model = HomeModel
        fields = '__all__'