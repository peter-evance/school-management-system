from djoser.serializers import UserCreateSerializer, UserSerializer

from auth.models import CustomUser


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

      
class CustomUserSerializer(UserSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
