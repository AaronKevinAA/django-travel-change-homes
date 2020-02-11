import datetime
import json
import os

from django.core import serializers
from django.db.models import Q
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.

from Mydjweb import settings
from XXX.models import LoginUser, UserInfo, RealName, UserHome, UserPublish, HomeImage, BannerImage


def index(request):
    global publish, home
    num = 0
    data = {'data': '', 'num': '', 'banner': ''}
    banner = BannerImage.objects.filter(status=1)
    data['banner'] = banner.all()
    city = request.GET.get('hcity', default='1')
    dicts = []
    if city == '1':
        home = UserHome.objects.filter(location__contains='上海')
    elif city == '2':
        home = UserHome.objects.filter(location__contains='南京')
    elif city == '3':
        home = UserHome.objects.filter(location__contains='杭州')
    elif city == '4':
        home = UserHome.objects.filter(location__contains='北京')
    elif city == '5':
        home = UserHome.objects.filter(location__contains='苏州')
    elif city == '6':
        home = UserHome.objects.filter(location__contains='重庆')
    elif city == '7':
        home = UserHome.objects.filter(location__contains='苏州')
    if home:
        for i in range(0, len(home.all())):
            publish = UserPublish.objects.filter(home_name=home[i].name, status=0)
            if publish:
                num = num + publish.all().__len__()
                for k in range(0, len(publish.all())):
                    dict = model_to_dict(publish[k])
                    dict['home_type'] = home[i].type
                    dict['location'] = home[i].location
                    img = HomeImage.objects.filter(pid_id=publish[k].pid, image_id=1)
                    if img:
                        dict['img'] = img[0].image
                    dicts.append(dict)
        data['num'] = num
        data['data'] = dicts
    return render(request, "index.html", data)


def post_login(request):
    if request.method == "POST":
        req = json.loads(request.body.decode())
        email = req["email"]
        password = req["password"]
        user = LoginUser.objects.filter(email=email, pwd=password)
        if user:
            request.session["login_user"] = email
            res = {"status": "true", "err": "", "data": serializers.serialize('python', user)}
        else:
            res = {"status": "false", "err": "邮箱或密码错误"}
        return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json,charset=utf-8")
    return 0


def post_exit_login(request):
    if request.method == "POST":
        request.session["login_user"] = ""
        res = {"status": "true", "err": ""}
        return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json,charset=utf-8")
    return 0


def post_register(request):
    if request.method == "POST":
        req = json.loads(request.body.decode())
        email = req["email"]
        password = req["password"]
        user = LoginUser.objects.filter(email=email)
        if user:
            res = {"status": "false", "err": "该邮箱已经被注册"}
        else:
            LoginUser.objects.create(email=email, pwd=password)
            res = {"status": "true", "err": ""}
        return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json,charset=utf-8")
    return 0


# 验证是否登录的装饰器
def check_user(func):
    def inner(*args, **kwargs):
        # 判断是否登录
        email = args[0].session.get("login_user", "")
        if email == "":
            # 保存当前的url到session中
            args[0].session["path"] = args[0].path
            # 重定向到登录页面
            return redirect('/')
        return func(*args, **kwargs)

    return inner


@check_user
# 个人信息
def personinfo(request):
    data = {'account': '', 'head_img': '', 'credit': '', 'is_rn': ''}
    email = request.session.get("login_user", "")
    user = UserInfo.objects.get(email=email)
    data['account'] = user.account
    data['head_img'] = user.head_img
    data['credit'] = user.credit
    user_rn = RealName.objects.filter(email=email, status=1)
    if user_rn:
        data['is_rn'] = "true"
        data['rn_name'] = user_rn[0].name
        data['rn_phone'] = user_rn[0].phone[0:3]
        data['rn_sex'] = user_rn[0].sex
        data['rn_age'] = user_rn[0].age
        data['rn_idnumber'] = user_rn[0].idnumber[-7:-1]
    else:
        data['is_rn'] = "false"
    return render(request, "p_info.html", data)


@check_user
# 编辑个人信息
def modify_personinfo(request):
    return render(request, "modify_p_info.html")


def post_modify_personinfo(request):
    if request.method == "POST":
        email = request.session.get("login_user", "")
        account = request.POST.get('account')
        head_img = request.FILES.get('head_img')
        head_img.name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
        if account is not None:
            UserInfo.objects.filter(email=email).update(account=account)
        if head_img is not None:
            UserInfo.objects.filter(email=email).update(head_img=head_img)
        res = {"status": "true", "err": ""}
        return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json,charset=utf-8")
    return 0


def post_realname(request):
    if request.method == "POST":
        email = request.session.get("login_user", "")
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        idnumber = request.POST.get('idnumber')
        phone = request.POST.get('phone')
        idfront = request.FILES.get('idfront')
        idfront.name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
        idbehind = request.FILES.get('idbehind')
        idbehind.name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
        date = datetime.datetime.now()
        user = RealName.objects.filter(Q(email_id=email, status=1) | Q(email_id=email, status=0))
        if user:
            res = {"status": "false", "err": "该用户已经申请实名注册或已成功实名注册"}
        else:
            RealName.objects.create(email_id=email, name=name, sex=sex, age=age, idnumber=idnumber,
                                    date=date.strftime("%Y-%m-%d %H:%M:%S"), idfront=idfront, idbehind=idbehind,
                                    phone=phone, status=0)
            res = {"status": "true", "err": ""}
        return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json,charset=utf-8")
    return 0


@check_user
# 房屋信息
def myhome_info(request):
    data = {'num': -1, 'data': ''}
    email = request.session.get("login_user", "")
    homes = UserHome.objects.filter(email_id=email, status=1)
    data['num'] = len(homes)
    if homes:
        data['data'] = homes.all()
    return render(request, "myhome_info.html", data)


def post_home_add(request):
    if request.method == "POST":
        email = request.session.get("login_user", "")
        name = request.POST.get('name')
        area = request.POST.get('area')
        type = request.POST.get('type')
        location = request.POST.get('location')
        prove = request.FILES.get('prove')
        prove.name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
        is_name = UserHome.objects.filter(email_id=email, name=name)
        if is_name:
            res = {'status': 'false', 'err': '该房屋已经上传过了'}
        else:
            UserHome.objects.create(email_id=email, name=name, area=area, type=type, location=location, prove=prove,
                                    status=0)
            res = {'status': 'true', 'err': ''}
        return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json,charset=utf-8")
    return 0


@check_user
# 发布详细
def mypublish_detail_info(request):
    req = request.GET.get('id', default=-1)
    email = request.session.get("login_user", "")
    date = {'publish_date': '', 'img': '', 'home_date': ''}
    publish = UserPublish.objects.filter(pid=req)
    if publish:
        date['publish_date'] = publish[0]
        img = HomeImage.objects.filter(pid_id=req)
        date['img'] = img.all()
    home = UserHome.objects.filter(email_id=email, name=publish[0].home_name)
    date['home_date'] = home[0]
    return render(request, "mypubish_detail_info.html", date)


@check_user
# 认证房屋信息
def myhome_add_info(request):
    return render(request, "myhome_add_info.html")


@check_user
# 交易信息
def mydeal_info(request):
    return render(request, "mydeal_info.html")


@check_user
# 发布房屋信息
def mypublish_add_info(request):
    data = {'data': ''}
    email = request.session.get("login_user", "")
    home = UserHome.objects.filter(email_id=email, status=1)
    data['data'] = home.all()
    return render(request, "mypublish_add_info.html", data)


def post_publish_add(request):
    if request.method == "POST":
        email = request.session.get("login_user", "")
        title = request.POST.get('title')
        home_name = request.POST.get('home_name')
        role = request.POST.get('role')
        price = request.POST.get('price')
        date = datetime.datetime.now()
        situation_desc = request.POST.get('situation_desc')
        facilities = request.POST.get('facilities')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        images = request.FILES.getlist('images[]')
        user = UserPublish.objects.create(email_id=email, title=title, home_name=home_name, role=role, price=price,
                                          situation_desc=situation_desc,
                                          facilities=facilities, start_date=start_date, date=date.strftime("%Y-%m-%d"),
                                          end_date=end_date, image_num=images.__len__(), status=0)
        i = 1
        for img in images:
            HomeImage.objects.create(pid_id=user.pid, image_id=i, image=img)
            i = i + 1
        res = {'status': 'true', 'err': ''}
        return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json,charset=utf-8")
    return 0


# 查找
def search(request):
    city = request.GET.get('city', '')
    date = request.GET.get('date', '')
    dicts = []
    num = 0
    data = {'data': '', 'num': 0, 'city': city}
    home = UserHome.objects.filter(location__contains=city)
    if home:
        for i in range(0, len(home.all())):
            if date == 'undifined' or date == '':
                publish = UserPublish.objects.filter(home_name=home[i].name, status=0)
            else:
                publish = UserPublish.objects.filter(home_name=home[i].name, start_date__lte=date, status=0)
            if publish:
                num = num + publish.all().__len__()
                for k in range(0, len(publish.all())):
                    dict = model_to_dict(publish[k])
                    dict['home_type'] = home[i].type
                    dict['location'] = home[i].location
                    img = HomeImage.objects.filter(pid_id=publish[k].pid, image_id=1)
                    if img:
                        dict['img'] = img[0].image
                    dicts.append(dict)
        data['num'] = num
        data['data'] = dicts
    return render(request, "search.html", data)


# 房屋信息详情
def home_detail(request):
    home_id = request.GET.get('homeid', -1)
    data = {'data': '','image':'','home_owner':'','is_rn':'false'}
    publish = UserPublish.objects.filter(pid=home_id)
    if publish:
        dict = model_to_dict(publish[0])
        home = UserHome.objects.filter(email_id=publish[0].email_id,name=publish[0].home_name)
        dict['home_type'] = home[0].type
        dict['location'] = home[0].location
        img = HomeImage.objects.filter(pid_id=publish[0].pid)
        data['image'] = img.all()
        data['data'] = dict
        owner = UserInfo.objects.filter(email_id=publish[0].email_id)
        data['home_owner'] = owner[0]
        owner_rn =RealName.objects.filter(email_id=publish[0].email_id)
        if owner_rn:
            data['is_rn']='true'
    return render(request, "home_detail.html",data)


@check_user
def mypublish_info(request):
    data = {'data': ''}
    dicts = []
    email = request.session.get("login_user", "")
    publish = UserPublish.objects.filter(email_id=email, status=0)
    data['data'] = publish.all()
    for k in range(0, len(publish.all())):
        dict = model_to_dict(publish[k])
        img = HomeImage.objects.filter(pid_id=publish[k].pid, image_id=1)
        if img:
            dict['img'] = img[0].image
        dicts.append(dict)
    data['data'] = dicts
    return render(request, "mypublish_info.html", data)
