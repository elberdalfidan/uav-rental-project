from rest_framework import serializers
from uavs.models import Brand


class BrandCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]

    def validate_name(self, value):
        if 2 > len(value) > 100:
            raise serializers.ValidationError("This field must be between 2 and 100 characters.")
        qs = Brand.objects.filter(name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This brand already exists.")
        return value


class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'