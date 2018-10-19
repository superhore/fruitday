from django.contrib import admin
from .models import *
# Register your models here.


class GoodsAdmin(admin.ModelAdmin):
    list_filter = ['goodsType']
    search_fields = ['title']


class UsersAdmin(admin.ModelAdmin):
    search_fields = ['uphone', 'uname', 'uemail']


class CarInfoAdmin(admin.ModelAdmin):
    list_filter = ['user','goods']
    search_fields = ['user','goods']



admin.site.register(Users, UsersAdmin)
admin.site.register(GoodsType)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(CarInfo,CarInfoAdmin)
