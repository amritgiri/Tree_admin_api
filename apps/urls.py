from django.urls import path, include

from .views import RootListCreateAPIView

urlpatterns = [
    path('api/root', RootListCreateAPIView.as_view({'get':'list'})),
]
