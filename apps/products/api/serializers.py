
from rest_framework import serializers
from apps.products.models import ProductsModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = '__all__'