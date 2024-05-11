from django.contrib.auth import get_user_model, logout, login
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.views import APIView
from .permissions import IsOwner
from .serializers import UserSerializer, UserLoginSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from rest_framework import status
from rest_framework.response import Response

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    """
    post:
        Create new user instance. Returns username, email of the created user.

        parameters: [username, email, password]
    """

    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class UserListAPIView(ListAPIView):
    """
    get:
        Returns list of all exisiting users
    """

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Returns the detail of a user instance

        parameters: [id]

    put:
        Update the detail of a user instance

        parameters: [id, username, email, password]

    delete:
        Delete a user instance

        parameters: [id]
    """

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


@method_decorator(csrf_protect, name='dispatch')
class UserLoginAPIView(APIView):
    """
    post:
        Login user instance. Returns username, email of the logged in user.

        parameters: [username, password]
    """

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            return Response({'message': 'Login Successful for user: {}'.format(user.username)},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutAPIView(APIView):
    """
    post:
        Logout user instance. Returns message of logout.
    """

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'Logout Successful'}, status=status.HTTP_200_OK)
