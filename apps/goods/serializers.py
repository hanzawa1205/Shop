from .models import *
from rest_framework import serializers


class GoodsModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = "__all__"


class GoodsCategoryModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"

