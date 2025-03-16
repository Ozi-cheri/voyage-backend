from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'is_owner'
        ]

    def get_is_owner(self, obj):
        request = self.context.get('request')  
        if request and request.user.is_authenticated:
            return request.user == obj.owner  # Returns True if the user owns the profile
        return False  # Returns False for all other profiles