from django.contrib.auth import get_user_model, password_validation
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import BaseUserManager
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser' ,'auth_token', 'user_permissions', 'date_joined', 'photo')
        read_only_fields = ('id', 'is_active', 'is_staff', 'is_superuser', 'auth_token', 'user_permissions', 'date_joined')
    # email = serializers.EmailField()
    # first_name = serializers.CharField(max_length=100)
    # last_name =serializers.CharField(max_length=100)

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
        #  fields = '__all__'
         fields = ('id', 'email', 'first_name', 'last_name', 'is_adopter', 'is_seller','is_active', 'is_staff', 'is_superuser' ,'auth_token', 'user_permissions', 'date_joined', 'photo')
         read_only_fields = ('id', 'is_adopter', 'is_seller','is_active', 'is_staff', 'is_superuser', 'auth_token', 'user_permissions', 'date_joined')

class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
         model = User
         fields = ('id', 'email', 'first_name', 'last_name', 'is_adopter', 'is_seller', 'is_active', 'is_staff', 'is_superuser' ,'auth_token')
         read_only_fields = ('id', 'is_adopter', 'is_seller','is_active', 'is_staff', 'is_superuser', 'auth_token')
    
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