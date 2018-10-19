from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index_views),

    # url(r'^login/$', login_views, name='login'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^register/$', register_views, name='register'),
    url(r'^login_out/$', login_out_views),
    url(r'^prodetail/index/(\d+)/', prode_views, name='prode'),
    url(r'^cart/$', cart_views, name='cart'),
    url(r'^cart/addcart', addcart_views),
    url(r'^delcart', delcart_views),
    url(r'^address/$', ads_views),
    url(r'^address/addads', add_ads_views),
    url(r'^address/delads', del_ads_views),
    url(r'^address/editads', edit_ads_views),
    url(r'^register/send_message', send_message, name='send_message'),
]