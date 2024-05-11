from .serializers import BrandSerializer, CategorySerializer, UavSerializer
from uavs.models import Brand, create_slug, Category, Uav
from rest_framework.response import Response
from rest_framework import status, viewsets


class BrandViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for viewing, adding, and deleting brands.

    This ViewSet provides `list`, `create`, and `destroy` actions.
    """

    def post(self, request, *args, **kwargs):
        data = {
            "name": request.data.get("name"),
            "slug": create_slug(request.data.get("name"))
        }
        serializer = BrandSerializer(data=data)
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
        serializer = BrandSerializer(query, many=True)
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


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for viewing, adding, and deleting categories.

    This ViewSet provides `list`, `create`, and `destroy` actions.
    """

    def post(self, request, *args, **kwargs):
        data = {
            "name": request.data.get("name"),
            ""
            "slug": create_slug(request.data.get("name"))
        }
        serializer = CategorySerializer(data=data)
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

        query = Category.objects.all()
        if search_value:
            query = query.filter(name__icontains=search_value)

        total = query.count()
        query = query[start:start + length]
        serializer = CategorySerializer(query, many=True)
        return Response({
            "draw": draw,
            "recordsTotal": total,
            "recordsFiltered": total,
            "data": serializer.data
        })

    def destroy(self, request, *args, **pk):
        try:
            category = Category.objects.get(pk=int(pk['pk']))
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UavViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for viewing, adding, and deleting UAVs.

    This ViewSet provides `list`, `create`, and `destroy` actions.
    """

    def post(self, request, *args, **kwargs):
        data = {
            "name": request.data.get("name"),
            "model": request.data.get("model"),
            "weight": request.data.get("weight"),
            "brand": request.data.get("brand"),
            "category": request.data.get("category"),
            "image": request.data.get("image")
        }
        serializer = UavSerializer(data=data)
        if serializer.is_valid():
            serializer.save(
                name=request.data.get("name"),
                model=request.data.get("model"),
                weight=request.data.get("weight"),
                brand_id=request.data.get("brand"),
                category_id=request.data.get("category"),
                image=request.data.get("image")
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        draw = int(request.GET.get('draw', 1))
        start = int(request.GET.get('start', 0))
        length = int(request.GET.get('length', 10))
        search_value = request.GET.get('search[value]', '')

        query = Uav.objects.all()
        if search_value:
            query = query.filter(name__icontains=search_value)

        total = query.count()
        query = query[start:start + length]
        serializer = UavSerializer(query, many=True)
        return Response({
            "draw": draw,
            "recordsTotal": total,
            "recordsFiltered": total,
            "data": serializer.data
        })

    def destroy(self, request, *args, **pk):
        try:
            uav = Uav.objects.get(pk=int(pk['pk']))
            uav.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Uav.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
