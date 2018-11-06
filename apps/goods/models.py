from django.db import models


class GoodsCategory(models.Model):
    name = models.CharField('类别名',max_length=32)


    class Meta:
        verbose_name = '商品类别'
        verbose_name_plural = '商品类别'
    def __str__(self):
        return self.name


class Goods(models.Model):
    category = models.ForeignKey(GoodsCategory,verbose_name='商品类别',on_delete=models.CASCADE)
    name = models.CharField('商品名',max_length=64)
    goods_num = models.IntegerField('库存数')
    sold_num = models.IntegerField('销量')

    class Meta :
        verbose_name = '商品信息'
        verbose_name_plural = '商品信息'


    def __str__(self):
        return self.name