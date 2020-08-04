from django.shortcuts import render

from django.contrib.auth import get_user_model, logout
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets, status
# from rest_framework.decorators import action
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view, permission_classes

from . import serializers
from .utils import get_and_authenticate_user, create_adopter_account, create_seller_account

User = get_user_model()

@csrf_exempt
@api_view(["GET"])
# @permission_classes((IsAuthenticated))
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=status.HTTP_200_OK)

class AuthViewSet(viewsets.GenericViewSet):
    queryset=User.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = serializers.EmptySerializer
    serializer_classes = {
        'login': serializers.UserLoginSerializer,
        'adopter_register': serializers.UserRegisterSerializer,
        'seller_register': serializers.UserRegisterSerializer,
        'password_change': serializers.PasswordChangeSerializer,
    }


    # add permission here
    # only superuser can view (me) for development purpose
    # And This whole thing should be move to another ViewSet that is only privately accessible
    def list(self, request):
        queryset = User.objects.all()
        permission_classes = []
        # print(queryset)
        serializer = serializers.UserSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['POST', ], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        # return token
        return Response(data={'token': data["auth_token"]}, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False)
    def adopter_register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_adopter_account(**serializer.validated_data)
        # data = serializers.AuthUserSerializer(user).data
        return Response(status=status.HTTP_201_CREATED)
    
    @action(methods=['POST', ], detail=False)
    def seller_register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_seller_account(**serializer.validated_data)
        # data = serializers.AuthUserSerializer(user).data
        return Response(status=status.HTTP_201_CREATED)

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
    
