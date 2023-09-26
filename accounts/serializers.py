from rest_framework import serializers

from accounts.models import User



class UserCreateAccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # extra_kwargs = {
        #     'email': {"required": True},
        #     'password': {"write_only": True},
        #     'last_login': {"write_only": True},
        #     'is_superuser': {"write_only": True},
        #     'is_staff': {"write_only": True},
        #     'is_active': {'read_only': True},
        #     'date_joined': {"write_only": True},
        #     'groups': {"write_only": True},
        #     'user_permissions': {"write_only": True},

        # }
        
class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'write_only': True},
            'is_staff': {'write_only': True},
            'is_superuser': {'write_only': True},
            'groups': {'write_only': True},
            'user_permissions': {'write_only': True},
            'date_joined': {'write_only': True},
            'email_active_code': {'write_only': True, 'required': False},
            'password': {'write_only': True, 'required': False},
            'username': {'required': False},
            'gender': {'required': False},
            }
