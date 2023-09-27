from rest_framework import serializers
from .models import LinkSciol

        
class LinkSerializers(serializers.ModelSerializer):
    class Meta:
        model = LinkSciol
        fields = '__all__'
        