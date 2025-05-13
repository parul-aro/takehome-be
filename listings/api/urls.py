from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .views import HouseViewSet

router = SimpleRouter()
router.register(r'houses', HouseViewSet, basename='house')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]