from rest_framework.views import APIView
from .serializers import BrandCreateUpdateSerializer, BrandListSerializer
from uavs.models import Brand, create_slug
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework import status, viewsets


class BrandViewSet(viewsets.ViewSet):
    """
    list:
        Returns list of all existing brands
    """

    def post(self, request, *args, **kwargs):
        serializer = BrandCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            slug = create_slug(request.data.get("name"))
            serializer.save(name=request.data.get("name"), slug=slug)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        draw = int(request.GET.get('draw', 1))
        start = int(request.GET.get('start', 0))
        length = int(request.GET.get('length', 10))
        search_value = request.GET.get('search[value]', '')

        query = Brand.objects.all()
        if search_value:
            query = query.filter(name__icontains=search_value)

        total = query.count()
        query = query[start:start + length]
        serializer = BrandListSerializer(query, many=True)
        return Response({
            "draw": draw,
            "recordsTotal": total,
            "recordsFiltered": total,
            "data": serializer.data
        })

    def destroy(self, request, *args, **pk):
        try:
            brand = Brand.objects.get(pk=int(pk['pk']))
            brand.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Brand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


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
