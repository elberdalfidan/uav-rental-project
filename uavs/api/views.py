from .serializers import BrandSerializer, CategorySerializer, UavSerializer, ReservationSerializer
from uavs.models import Brand, create_slug, Category, Uav, Reservation
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.core.exceptions import ValidationError


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


class ReservationViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing, adding, updating, and deleting reservations.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated is False:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_400_BAD_REQUEST)
        data = {
            "uav": request.data.get("uav"),
            "user": request.user.id,
            "start_date": request.data.get("start_date"),
            "end_date": request.data.get("end_date")
        }
        serializer = ReservationSerializer(data=data)
        if serializer.is_valid():
            try:
                serializer.save(
                    uav_id=request.data.get("uav"),
                    user_id=request.user.id,
                    start_date=request.data.get("start_date"),
                    end_date=request.data.get("end_date")
                )
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        draw = int(request.GET.get('draw', 1))
        start = int(request.GET.get('start', 0))
        length = int(request.GET.get('length', 10))
        search_value = request.GET.get('search[value]', '')

        query = Reservation.objects.all()
        if search_value:
            query = query.filter(uav__name__icontains=search_value)

        total = query.count()
        query = query[start:start + length]
        serializer = ReservationSerializer(query, many=True)
        return Response({
            "draw": draw,
            "recordsTotal": total,
            "recordsFiltered": total,
            "data": serializer.data
        })
