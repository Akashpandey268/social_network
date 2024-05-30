from rest_framework import serializers
from .models import FriendRequest,CustomUser
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name')


def validate_user_exists(value):
    """
    Validator function to check if the user with the specified ID exists in the database.
    """
    if not CustomUser.objects.filter(id=value).exists():
        raise serializers.ValidationError("User does not exist.")

class FriendRequestSerializer(serializers.ModelSerializer):
    from_user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    to_user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), validators=[validate_user_exists])

    class Meta:
        model = FriendRequest
        fields = ('id', 'from_user', 'to_user', 'created_at')


