from django.contrib.auth import get_user_model, password_validation
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import BaseUserManager
from rest_framework import serializers
from .models import Seller
from petAdoption.models.pet import Pet
from petAdoption.serializers import PetSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    seller_profile = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all())
    class Meta:
         model = User
         fields = ['url','id', 'email', 'first_name', 'last_name', 'is_seller', 'seller_profile' ,'is_active', 'is_staff', 'is_superuser' ,'auth_token', 'user_permissions', 'date_joined', 'photo']

class SellerSerializer(serializers.ModelSerializer):
    user = UserSerializer(instance=User.objects.all())
    # user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    pets = serializers.PrimaryKeyRelatedField(many=True, queryset=Pet.objects.all())
    # print(PetSerializer(instance=Pet.objects.all()))
    # pets = PetSerializer(instance=Pet.objects.all()[0])
    class Meta:
        model = Seller
        fields=['pk','user', 'pets']


class ActivateSellerSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)

class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
         model = User
         fields = ('id', 'email', 'first_name', 'last_name', 'is_seller', 'is_active', 'is_staff', 'is_superuser', 'auth_token')
         read_only_fields = ('id', 'is_seller','is_active', 'is_staff', 'is_superuser', 'auth_token')
    
    def get_auth_token(self, obj):
        # print(111)
        token = Token.objects.create(user=obj)
        # print(111)
        return token.key

class EmptySerializer(serializers.Serializer):
    pass

class UserRegisterSerializer(serializers.ModelSerializer):
    """
    A user serializer for registering the user
    """

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'photo')

    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if user:
            raise serializers.ValidationError("Email is already taken")
        # validate email here
        # but let the CustomUserManager normalize the email
        return value
        # return BaseUserManager.normalize_email(value)

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('Current password does not match')
        return value

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value