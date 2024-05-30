from rest_framework import serializers

from .models import Root

# class RootTreeSerializer(serializers.ModelSerializer):
#     children = serializers.SerializerMethodField()

#     class Meta:
#         model = Root
#         fields = ['id', 'name', 'children']

#     def get_children(self, obj):
#         children = obj.tn_children.all()
#         return RootTreeSerializer(children, many=True).data


class RootSerializers(serializers.ModelSerializer):
    class Meta:
        model = Root
        fields = "__all__"
