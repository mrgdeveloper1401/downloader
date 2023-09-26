# from requests import request
# from rest_framework import serializers
# from .models import CardModel
# from workspce.models import WorkspaceModel


# class CardSerializers(serializers.ModelSerializer):
#     workspce = serializers.PrimaryKeyRelatedField(queryset=WorkspaceModel.objects.all())
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault())

#     class Meta:
#         model = CardModel
#         fields = '__all__'
        
#         extra_kwargs = {
#             'is_active': {'read_only': True},
#         }