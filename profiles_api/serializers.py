from rest_framework import serializers
from profiles_api import models



class HelloSerializer(serializers.Serializer):
    """Serializes a name filed for testin our APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes User profile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name','password')
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def create(self, validated_data):
         """create and return a new user"""
         user = models.UserProfile.objects.create_user(**validated_data)
         return user

    def update(self, instance, validated_data):
        """Used to update user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
            return super().update(instance,validated_data)
