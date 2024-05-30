from rest_framework import serializers

from .models import Root

class RootSerializers(serializers.ModelSerializer):
    class Meta:
        model = Root
        field = '__all__'