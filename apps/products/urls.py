from django.urls import path
from .views import createSuperUser

from rest_framework import routers
from .api.viewsets import ProductViewSet

router = routers.SimpleRouter()
router.register('products', ProductViewSet, basename='products-list')

urlpatterns = router.urls + [
    path('create/', createSuperUser, name='create-superuser')
]