from django.shortcuts import render

from django.contrib.auth import get_user_model, logout
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets, status
# from rest_framework.decorators import action
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view, permission_classes

from . import serializers
from .utils import get_and_authenticate_user, create_account, activate_seller
from .models import Seller

User = get_user_model()

@csrf_exempt
@api_view(["GET"])
# @permission_classes((IsAuthenticated))
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=status.HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = serializers.UserSerializer

class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = serializers.SellerSerializer

class AuthViewSet(viewsets.GenericViewSet):
    queryset=User.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = serializers.EmptySerializer
    serializer_classes = {
        'login': serializers.UserLoginSerializer,
        'register': serializers.UserRegisterSerializer,
        'activate_seller': serializers.ActivateSellerSerializer,
        'password_change': serializers.PasswordChangeSerializer,
    }

    @action(methods=['POST', ], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        # return token
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_account(**serializer.validated_data)
        # data = serializers.AuthUserSerializer(user).data
        return Response(status=status.HTTP_201_CREATED)
    
    @action(methods=['POST', ], detail=False, permission_classes=[IsAuthenticated, ])
    def activate_seller(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = activate_seller(request.data["email"])
        # user = create_seller_account(**serializer.validated_data)
        # data = serializers.AuthUserSerializer(user).data
        return Response(status=status.HTTP_201_CREATED)

    @action(methods=['DELETE', ], detail=False, permission_classes=[IsAuthenticated, ])
    def deactivate_seller(self, request):
        # TODO
        pass

    @action(methods=['POST', ], detail=False, permission_classes=[IsAuthenticated, ])
    def logout(self, request):
        print(request.user.auth_token)
        request.user.auth_token.delete()
        logout(request)
        data = {'success': 'Sucessfully logged out'}
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False, permission_classes=[IsAuthenticated, ])
    def password_change(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        data = {'success': 'Sucessfully logged out'}
        return Response(status=status.HTTP_200_OK)

    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()
    
