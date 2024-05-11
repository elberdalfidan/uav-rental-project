from rest_framework.views import APIView
from .serializers import BrandCreateUpdateSerializer
from uavs.models import Brand
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework import status


class CreateBrandAPIView(APIView):
    """
    post:
       Creates a new brand instance. Returns created post data
       parameters: [name
    """

    queryset = Brand.objects.all()
    serializer_class = BrandCreateUpdateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = BrandCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListBrandAPIView(APIView):
    """
    get:
        Returns list of all existing brands
    """

    queryset = Brand.objects.all()
    serializer_class = BrandCreateUpdateSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        brands = Brand.objects.all()
        serializer = BrandCreateUpdateSerializer(brands, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
