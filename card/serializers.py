from rest_framework import serializers
from .models import LinkSciol


class LinkRequestSerializer(serializers.Serializer):
    link_type = serializers.ChoiceField(choices=[('instagram', 'Instagram'), ('facebook', 'Facebook'), ('twitter', 'Twitter')])
    link_url = serializers.URLField()
        
        
class DeleteSerializers(serializers.ModelSerializer):
    class Meta:
        model = LinkSciol
        fields = '__all__'
        