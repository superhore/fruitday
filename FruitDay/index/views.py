import datetime
import hashlib
import json

import logging
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
# Create your views here.


def mymd5(upwd):
    m = hashlib.md5()
    m.update(upwd.encode('utf8'))
    pwd = m.hexdigest()
    return pwd

def index_views(request):
    goodstype = GoodsType.objects.all()
    goods = Goods.objects.all()
    if 'uphone' in request.session:
        uphone = request.session.get('uphone')
        msg = 'a' + uphone + 'a'
        quit = '[a]'
        return render(request, 'index.html', locals())
    else:
        if 'id' in request.COOKIES and 'uphone' in request.COOKIES:
            uphone = request.COOKIES['uphone']
            request.session['uphone'] = uphone
            msg = 'a' + uphone
            quit = 'a'
            return render(request, 'index.html', locals())
        else:
            login = 'a'
            return render(request, 'index.html', locals())

from django.views import View
class Login(View):
    def get(self,request):

        if 'uphone' not in request.session:
            if 'id' in request.COOKIES and 'uphone' in request.COOKIES:
                val = request.COOKIES['uphone']
                msg = 'a:' + val
                return HttpResponseRedirect('/', locals())
            else:
                return render(request, 'login.html')
        else:
            uphone = request.session.get('uphone')
            msg = 'a' + uphone + 'a'
            quit = 'a'
            return HttpResponseRedirect('/', locals())
    def post(self,request):
            uphone = request.POST.get('uphone', '')
            upwd = request.POST.get('upwd', '')
            user = Users.objects.filter(uphone=uphone, upwd=mymd5(upwd))
            print('user:', type(user), user)
            print(user)
            if user:
                request.session['uphone'] = uphone
                request.session['user_id'] = user[0].id
                request.session.set_expiry(0)
                isSaved = request.POST.get('isSaved', '')
                resp = HttpResponseRedirect('/')
                if isSaved:
                    resp.set_cookie('id', user[0].id, 60 * 60 * 24 * 365)
                    resp.set_cookie('uphone', uphone, 60 * 60 * 24 * 365)
                return resp
            else:
                err = 'a'
                return render(request, 'login.html', locals())


# def login_views(request):
#     if request.method == 'GET':
#         if 'uphone' not in request.session:
#             if 'id' in request.COOKIES and 'uphone' in request.COOKIES:
#                 val = request.COOKIES['uphone']
#                 msg = 'a:' + val
#                 return HttpResponseRedirect('/',locals())
#             else:
#                 return render(request,'login.html')
#         else:
#             uphone = request.session.get('uphone')
#             msg = 'a' + uphone + 'a'
#             quit = 'a'
#             return HttpResponseRedirect('/',locals())
#     else:
#         uphone = request.POST.get('uphone', '')
#         upwd = request.POST.get('upwd', '')
#         user = Users.objects.filter(uphone=uphone,upwd=mymd5(upwd))
#         print('user:', type(user), user)
#         print(user)
#         if user:
#             request.session['uphone'] = uphone
#             request.session['user_id'] = user[0].id
#             request.session.set_expiry(0)
#             isSaved = request.POST.get('isSaved', '')
#             resp = HttpResponseRedirect('/')
#             if isSaved:
#                 resp.set_cookie('id', user[0].id, 60*60*24*365)
#                 resp.set_cookie('uphone', uphone, 60*60*24*365)
#             return resp
#         else:
#             err = 'a'
#             return render(request, 'login.html', locals())


def register_views(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        uphone = request.POST.get('uphone', None)
        user = Users.objects.filter(uphone=uphone)
        print('user:',type(user),user)
        if user:
            err = 'a'
            return render(request,'register.html',locals())
        else:
            upwd = request.POST.get('upwd', '')
            uname = request.POST.get('uname', '')
            uemail = request.POST.get('uemail', '')
            cpwd = request.POST.get('cpwd', '')
            if uphone and upwd:
                if upwd == cpwd:
                    try:
                        Users.objects.create(uphone=uphone, upwd=mymd5(upwd),
                                         uname=uname, uemail=uemail)
                        return HttpResponseRedirect('/login/')
                    except:
                        err = 'a'
                        return render(request,'register.html',locals())
                else:
                    err = 'a'
                    return render(request,'register.html',locals())
            else:
                err = 'a'
                return render(request,'register.html',locals())


def login_out_views(request):
    resp = HttpResponseRedirect('/')
    if 'uphone' in request.session:
        del request.session['uphone']
    if 'id' in request.COOKIES and 'uphone' in request.COOKIES:
        resp.delete_cookie('uphone')
        resp.delete_cookie('id')
    return resp


def prode_views(request,goodsid):
    if 'uphone' in request.session:
        uphone = request.session.get('uphone')
        msg = 'a' + uphone + 'a'
        quit = '[a]'
    else:
        login = 'a'
    # print(type(goodsid))
    goods = Goods.objects.get(id=goodsid)
    # print(goods.title)
    return render(request,'prode.html',locals())


def addcart_views(request):
    # a
    new_car = CarInfo()
    goods_count = request.GET.get('gcount','aa')
    # print(goods_count)
    goods_id = request.GET.get('goodsid','bb')
    # print(type(goods_id))
    # print(goods_id)
    # a
    goods = Goods.objects.filter(id=goods_id)
    # print(goods)
    if len(goods) > 0:
        new_car.goods = goods[0]
    else:
        return render(request,'cart.html',locals())
    # print('asd')
    uphone = request.session.get('uphone','')
    # print(uphone)
    if not uphone:
        return HttpResponseRedirect('/login/')
    user = Users.objects.get(uphone=uphone)
    # print(user)
    new_car.user = user
    #  a
    new_car.gcount = int(goods_count)
    oldgo = CarInfo.objects.filter(user_id=user.id,goods_id=goods_id)
    # a
    if len(oldgo)>0:
        oldgo[0].gcount=oldgo[0].gcount+new_car.gcount
        oldgo[0].save()
    else:
        # a
        new_car.save()
    # a
    # return render(request,'cart.html',locals())
    return HttpResponseRedirect('/cart')


def cart_views(request):
    if 'uphone' in request.session:
        uphone = request.session.get('uphone')
        user = Users.objects.get(uphone=uphone)
        msg = 'a' + uphone + 'a'
        quit = '[a]'
        carts = CarInfo.objects.filter(user_id=user.id)
        goods = Goods.objects.all()
        return render(request,'cart.html',locals())
    else:
        return HttpResponseRedirect('/login/')


def delcart_views(request):
    uphone = request.session.get('uphone')
    # print('uphone',uphone)
    cart_id = request.GET.get('cart_id')
    # print('cart_id',cart_id)
    user = Users.objects.get(uphone=uphone)
    # print('user',user)
    user_id = user.id
    delcart = CarInfo.objects.filter(id=cart_id,user_id=user_id)
    delcart.delete()
    content = {'msg':'del ok'}
    return HttpResponse(json.dumps(content))
    # a
    # return HttpResponse(json.dumps(data))


def ads_views(request):
    if 'uphone' not in request.session:
        return HttpResponseRedirect('/login')
    else:
        uphone = request.session.get('uphone')
        user = Users.objects.get(uphone=uphone)
        cartids = request.GET.get('cartids')
        cartidslist = cartids.split(',')
        carts = []
        goods = Goods.objects.all()
        for cartid in cartidslist:
            cart = CarInfo.objects.get(id=int(cartid))
            carts.append(cart)
        adss = Address.objects.filter(user_id=user.id)
        return render(request, 'ads.html', locals())




def add_ads_views(request):
    if 'uphone' not in request.session:
        return HttpResponseRedirect('/login')
    else:
        uphone = request.session.get('uphone')
        user = Users.objects.get(uphone=uphone)
        aname = request.GET.get('aname')
        print(aname)
        address = request.GET.get('address')
        print(address)
        cellphone = request.GET.get('cellphone')
        print(cellphone)
        try:
            ads = Address.objects.create(aname=aname,
                                   address=address,
                                   cellphone=cellphone,
                                   user=user)
        except BaseException as e:
            logging.warning(e)
        # msg = {'adsid':ads.id}
        return HttpResponse(ads.id)



def del_ads_views(request):
    user_id = request.session.get('user_id')
    print(user_id)
    adsid = request.GET.get('adsid')
    print(adsid)
    try:
        delads = Address.objects.get(user_id=user_id, id=adsid)
        delads.delete()
    except BaseException as e:
        logging.warning(e)

    return render(request, 'ads.html')
    # return redirect()  Httpresponse()


def edit_ads_views(request):
    user_id = request.session.get('user_id')
    print(user_id)
    user = Users.objects.get(id=user_id)
    adsid = request.POST.get('adsid')
    print(adsid)
    address = request.POST.get('address')
    print(address)
    cellphone = request.POST.get('cellphone')
    print(cellphone)
    aname = request.POST.get('aname')
    print(aname)
    try:
        ads = Address.objects.get(id=adsid, user_id=user.id)
        ads.aname = aname
        ads.cellphone = cellphone
        ads.address = address
        ads.save()
    except BaseException as e:
        logging.warning(e)
    # try:
    #     Address.objects.get(id=adsid, user_id=user.id).update(aname=aname,address=address,cellphone=cellphone)
    # except BaseException as e:
    #     logging.warning(e)

    return render(request, 'ads.html')


def adrlist(request):
    user_id = request.session.get('user_id')
    adr = Address.objects.filter(user_id=user_id)
    return render(request,'order.html',locals())


def add_order(request):
    # a
    user_id = request.session.get('user_id')

    # a
    try:
        user = Users.objects.get(id=user_id)
        acount = request.GET.get('acount')
        cals = request.GET.get('cals')
        aprice = request.GET.get('aprice')
        ads = request.GET.get('ads')
        orderNo = datetime.datetime.now()
        orderStatus = request.GET.get()
        # a
        Order.objects.create(orderNo=orderNo,
                             user=user_id,
                             acount=acount,
                             cals=cals,
                             aprice=aprice,
                             ads=ads,
                             orderStatus=orderStatus
                             )
    except BaseException as e:
        logging.warning(e)
    # a
    content={'status':'ok','orderid':orderid}
    return HttpResponse(json.dumps(content))






import random
import http.client
from urllib import parse
from django.http import JsonResponse

host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

account = "C11679655"

password = "0c13353a3af9ed0e81c0abddf5c94597"

def send_message(request):

    mobile = request.GET.get('mobile')

    user = Users.objects.filter(uphone=mobile)
    if len(user) == 1:
        return JsonResponse({'msg': "this uphone is No"})

    message_code = ''
    for i in range(6):
        i = random.randint(0, 9)
        message_code += str(i)

    text = "您的验证码是："+ message_code +"。请不要把验证码泄露给其他人。"

    params = parse.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})

    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

    conn = http.client.HTTPConnection(host, port=80, timeout=30)

    conn.request("POST", sms_send_uri, params, headers)

    response = conn.getresponse()

    response_str = response.read()

    conn.close()

    request.session['message_code'] = message_code
    print(eval(response_str.decode()))

    return JsonResponse(eval(response_str.decode()))




