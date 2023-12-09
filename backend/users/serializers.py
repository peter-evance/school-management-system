from djoser.serializers import UserCreateSerializer, UserSerializer

from users.models import CustomUser


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','password','sex','first_name','last_name','role', 'date_of_birth','address','email')

      
class CustomUserSerializer(UserSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','username','first_name','last_name','sex','date_of_birth','address','email','role')
