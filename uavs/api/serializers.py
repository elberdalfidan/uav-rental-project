from rest_framework import serializers
from uavs.models import Brand, Category, Uav, Reservation


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UavSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Uav
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    uav = UavSerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = '__all__'
