from djoser.serializers import UserCreateSerializer, UserSerializer

from users.models import CustomUser


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','password','sex','first_name','last_name','role')

      
class CustomUserSerializer(UserSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','username','sex','first_name','last_name','role')
