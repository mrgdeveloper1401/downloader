from rest_framework import serializers
from .models import LinkSciol


# class LinkRequestSerializer(serializers.Serializer):
#     link_url = serializers.URLField()
        
        
class LinkSerializers(serializers.ModelSerializer):
    class Meta:
        model = LinkSciol
        fields = '__all__'
        