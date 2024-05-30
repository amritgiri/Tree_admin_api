from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RootListCreateAPIView

router = DefaultRouter()
# router.register(r'api/tree', RViewSet, basename='tree')
router.register(r"api/roots", RootListCreateAPIView, basename="roots")


urlpatterns = [
    # path('api/tree', TreeView.as_view(), name='tree-view'),
    path("", include(router.urls)),
]
