from rest_framework import serializers
from .models import LinkSciol


class LinkSciolSerializers(serializers.ModelSerializer):
    class Meta:
        model = LinkSciol
        fields = ('link_sciol', )
        
        
# class LinkCreateSerialiers(serializers.ModelSerializer):
#     class Meta:
#         model = LinkSciol
#         fields = ('link_sciol', )
        