from rest_framework import serializers
from .models import LinkSciol


class LinkSciolSerializers(serializers.ModelSerializer):
    class Meta:
        model = LinkSciol
        fields = '__all__'