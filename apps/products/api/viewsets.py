from rest_framework import viewsets

from apps.products.models import ProductsModel
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer
