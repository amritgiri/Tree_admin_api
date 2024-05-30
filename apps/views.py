# from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Root
from .serializers import RootSerializers


def build_tree(node):
    children = node.get_children()
    tree = {
        "id": node.id,
        "name": node.name,
        "children": [build_tree(child) for child in children],
    }
    return tree


class RootListCreateAPIView(viewsets.ModelViewSet):
    queryset = Root.objects.all()
    serializer_class = RootSerializers

    def list(self, request, *args, **kwargs):
        root_nodes = Root.objects.filter(tn_parent=None)
        tree = [build_tree(node) for node in root_nodes]

        return Response(tree)
