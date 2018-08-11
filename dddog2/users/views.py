from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.db import DatabaseError
import logging

from users.models import Users


def test(request):
    """测试通迅"""
    return HttpResponse('this is user test,is ok')


def registers(request):
    """用户注册"""
    # 判断选项是否为空
    if request.POST.get('uname', '') and request.POST.get('password', '') and request.POST.get('password_1', ''):
        # 判断两次密码是否一致
        if request.POST['password'] == request.POST['password_1']:
            # 判断用户名是否存在
            if Users.objects.filter(uname=request.POST['uname']).exists():
                result = {'response': '用户名已存在'}
                return JsonResponse(result)
            else:
                password = make_password(request.POST['password'], None, 'pbkdf2_sha1')
                new_user = Users(uname=request.POST['uname'], password=password)
                try:
                    new_user.save()
                except DatabaseError as e:
                    logging.warning(e)
                    result = {'response': '注册用户异常'}
                    return JsonResponse(result)
                result = {'response': '注册用户成功'}
                return JsonResponse(result)
        else:
            result = {'response': '密码不一致'}
            return JsonResponse(result)
    else:
        result = {'response': '选项不能为空'}
        return JsonResponse(result)


def logins(request):
    """用户登陆"""
    # 判断选项是否为空
    if request.POST.get('uname', '') and request.POST.get('password', ''):
        # 判断用户是否存在
        if Users.objects.filter(uname=request.POST['uname']).exists():
            user = Users.objects.filter(uname=request.POST['uname'])
            # 判断用户密码是否正确
            if check_password(request.POST['password'], user[0].password):
                user_all_limits = []
                # 序列化用户自身权限
                for user_limit in user[0].ulimits.all():
                    user_all_limits.append(user_limit.limit)
                print(user_all_limits)
                # 序列化用户所处所有有效组权限
                for user_group in user[0].groups_set.filter(is_active=1):
                    for limit in user_group.glimits.all():
                        user_all_limits.append(limit.limit)
                print(user_all_limits)
                # 将用户id,uname,limits写入session内
                request.session['id'] = user[0].id
                request.session['uname'] = user[0].uname
                request.session['limits'] = user_all_limits
                result = {'response': '用户登陆成功'}
                return JsonResponse(result)
            else:
                result = {'response': '密码不正确'}
                return JsonResponse(result)
        else:
            result = {'response': '用户不存在'}
            return JsonResponse(result)
    else:
        result = {'response': '选项不能为空'}
        return JsonResponse(result)


def quits(request):
    """退出登陆"""
    # 判断是否有用户登陆
    if request.session.get('id', '') and request.POST.get('uname', ''):
        # 删除登陆用户相关信息
        del request.session['id']
        del request.session['uname']
        del request.session['limits']
        # 重定向到登陆页面
        # return redirect('/users/login')
        result = {'response': '退出成功'}
        return JsonResponse(result)
    else:
        # 重定向到登陆页面
        # return redirect('/users/login')
        result = {'response': '未登陆'}
        return JsonResponse(result)


def inquire_logins(request):
    """查询登陆情况"""
    # 获取session内的值
    result = {'id': request.session.get('id', ''), 'uname': request.session.get('uname', ''),
              'limits': request.session.get('limits', '')}
    return JsonResponse(result)


def inquire_user_infos(request):
    """查询用户信息"""
    # 判断是否登陆
    if request.session.get('id', ''):
        # 获取用户对象
        user = Users.objects.filter(id=request.session['id'])
        # 获取用户相关信息
        result = {'uname': user[0].uname, 'avatar': user[0].avatar, 'ctime': user[0].ctime, 'phone': user[0].phone}
        return JsonResponse(result)
    else:
        result = {'response': '未登陆'}
        return JsonResponse(result)


def update_user_infos(request):
    """用户信息修改"""
    # 判断是否登陆
    if request.session.get('id', ''):
        # 获取用户对象
        user = Users.objects.get(id=request.session['id'])
        # 判断前端传入的相关信息并修改
        if request.POST.get('phone', ''):
            user.phone = request.POST['phone']
        if request.POST.get('address', ''):
            user.address = request.POST['address']
        try:
            user.save()
        except DatabaseError as e:
            logging.warning(e)
            result = {'response': '信息更改失败'}
            return JsonResponse(result)
        result = {'response': '信息更改完成', 'phone': user.phone, 'address': user.address}
        return JsonResponse(result)
    else:
        result = {'response': '未登陆'}
        return JsonResponse(result)


def update_passwords(request):
    """修改密码"""
    # 判断是否登陆
    if request.session.get('id', ''):
        # 获取用户对象
        user = Users.objects.get(id=request.session['id'])
        # 判断相关选项是否为空
        if request.POST.get('password') and request.POST.get('password_1') and request.POST.get('password_2'):
            # 判断两次密码是否一致
            if request.POST['password_1'] == request.POST['password_2']:
                # 判断旧密码是否正确
                if check_password(request.POST['password'], user.password):
                    new_password = make_password(request.POST['password_1'], None, 'pbkdf2_sha1')
                    # 修改密码
                    user.password = new_password
                    try:
                        user.save()
                    except DatabaseError as e:
                        logging.warning(e)
                        result = {'response': '修改密码失败'}
                        return JsonResponse(result)
                    result = {'response': '修改密码成功'}
                    return JsonResponse(result)
                else:
                    result = {'response': '原密码不正确'}
                    return JsonResponse(result)
            else:
                result = {'response': '新密码不一致'}
                return JsonResponse(result)
        else:
            result = {'response': '选项不能为空'}
            return JsonResponse(result)
    else:
        result = {'response': '未登陆'}
        return JsonResponse(result)
