from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from .serializers import *
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import BaseAuthentication


class GoodsPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 5

class GoodsListView(generics.ListAPIView):
    pagination_class = GoodsPagination
    queryset = Goods.objects.all()
    serializer_class= GoodsModelSerializers
    search_fields = ('=name', 'goods_brief')




