import xadmin
from .models import *


class GoodsCategoryAdmin(object):
    list_display = ['name']


class GoodsAdmin(object):
    list_display = ['category','name','goods_num','sold_num']
    list_filter = ["category","name", "goods_num", "sold_num"]


xadmin.site.register(GoodsCategory,GoodsCategoryAdmin)
xadmin.site.register(Goods,GoodsAdmin)