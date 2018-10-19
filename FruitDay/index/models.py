from django.db import models

# Create your models here.
#coding=utf-8

class Users(models.Model):
    uphone = models.CharField(max_length=11, verbose_name='a')
    upwd = models.CharField(max_length=32, verbose_name='a')
    uname = models.CharField(max_length=30, default='a', verbose_name='a')
    uemail = models.EmailField(null=True, verbose_name='a')
    isActive = models.BooleanField(default=True, verbose_name='a')

    def __str__(self):
        return self.uname

    class Meta:
        verbose_name = 'a'
        verbose_name_plural = verbose_name


class GoodsType(models.Model):
    title = models.CharField(max_length=30, verbose_name='a')
    desc = models.TextField(null=True, verbose_name='a')
    picture = models.ImageField(
        upload_to='static/upload/goodsType', verbose_name='a')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'a'
        verbose_name_plural = verbose_name


class Goods(models.Model):
    title = models.CharField(max_length=30, verbose_name='a')
    price = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name='a')
    spec = models.CharField(max_length=30, verbose_name='a')
    picture = models.ImageField(
        upload_to='static/upload/goods', verbose_name='a')
    goodsType = models.ForeignKey(GoodsType, null=True, verbose_name='a')
    isActive = models.BooleanField(default=True, verbose_name='a')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'a'
        verbose_name_plural = verbose_name


    # def get_sbsolute_url(self):
    #     return 'prodetail/index/?goodsid={}'.format(self.id)




class CarInfo(models.Model):
    user = models.ForeignKey(Users,verbose_name='a')
    goods = models.ForeignKey(Goods,verbose_name='a')
    gcount = models.IntegerField(verbose_name='a')

    def __str__(self):
        return self.gcount

    class Meta:
        verbose_name = 'a'
        verbose_name_plural = verbose_name


class Address(models.Model):
    """
    aname a
    """
    aname = models.CharField('a', max_length=30)
    address = models.CharField('a', max_length=150, null=False)
    cellphone = models.CharField('a', max_length=20, null=False)
    user = models.ForeignKey(Users)

    def __str__(self):
        return self.aname

    class Meta:
        verbose_name = 'a'
        verbose_name_plural = verbose_name

ORDERSTATUS = (
    (1, 'a'),
    (2, 'a'),
    (3, 'a'),
    (4, 'a')
)


class Order(models.Model):
    orderNo = models.CharField('a', max_length=32)
    user = models.ForeignKey(Users)
    acount = models.CharField('a', max_length=50)
    cals = models.TextField('a', null=True)
    aprice = models.CharField('a', max_length=50)
    ads = models.CharField('a', max_length=100)
    orderTime = models.DateTimeField('a', auto_now_add=True)
    orderStatus = models.IntegerField('a', choices=ORDERSTATUS)

    def get_orderStatusDisplay(self):
        if self.orderStatus == 1:
            return u'a'
        elif self.orderStatus == 2:
            return u'a'
        elif self.orderStatus == 3:
            return u'a'
        elif self.orderStatus == 4:
            return u'a'
        else:
            return u'a'