from rest_framework.generics import ListCreateAPIView

from .models import Product
from .serializers import ProductSerializer


class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
