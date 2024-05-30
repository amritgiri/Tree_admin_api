from django.urls import path, include

from .views import RootListCreateAPIView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'api/tree', RViewSet, basename='tree')
router.register(r'api/roots', RootListCreateAPIView, basename='roots')


urlpatterns = [
    # path('api/tree', TreeView.as_view(), name='tree-view'),
    path('', include(router.urls)),
]
