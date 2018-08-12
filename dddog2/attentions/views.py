from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.db import DatabaseError
import logging

from attentions.models import Attentions


def test(request):
    """测试通迅"""
    return HttpResponse('this is attentions view test,is ok!')


def attentions_cancels(request):
    """关注与取消"""
    # 获取用户id与关注id
    user_id = request.session.get('id', '')
    attention_id = request.POST.get('uid', '')
    # 判断用户是否登陆
    if user_id:
        # 判断是否传入关注者
        if attention_id:
            # 判断此前是否有过关注
            if Attentions.objects.filter(user_id=user_id, attentions_id=attention_id).exists():
                # 获取关注对象
                attention = Attentions.objects.get(user_id=user_id, attentions_id=attention_id)
                # 判断当前处于关注壮态还是取消关注壮态
                if attention.is_cancel:
                    # 将取消关注变更为关注
                    attention.is_cancel = 0
                    try:
                        attention.save()
                    except DatabaseError as e:
                        logging.warning(e)
                        result = {'respones': '关注异常'}
                        return JsonResponse(result)
                    result = {'respones': '已关注'}
                    return JsonResponse(result)
                else:
                    # 将关注变更为取消关注
                    attention.is_cancel = 1
                    try:
                        attention.save()
                    except DatabaseError as e:
                        logging.warning(e)
                        result = {'respones': '取消关注异常'}
                        return JsonResponse(result)
                    result = {'respones': '已取消关注'}
                    return JsonResponse(result)
            else:
                print(user_id, attention_id)
                # 新建关注对象
                new_attention = Attentions(user_id=user_id, attentions_id=attention_id)
                try:
                    new_attention.save()
                except DatabaseError as e:
                    logging.warning(e)
                    result = {'respones': '关注异常'}
                    return JsonResponse(result)
                result = {'respones': '已关注'}
                return JsonResponse(result)
        else:
            result = {'respones': '请传入关注信息'}
            return JsonResponse(result)

    else:
        result = {'respones': '请先登陆'}
        return JsonResponse(result)


def cancel_attentions(request):
    """取消关注"""
    # 获取用户id与关注id
    user_id = request.session.get('id', '')
    attention_id = request.POST.get('uid', '')
    # 判断用户是否登陆
    if user_id:
        # 判断是否传入关注者
        if attention_id:
            # 获取关注对象
            attention = Attentions.objects.get(user_id=user_id, attentions_id=attention_id)
            # 将关注变更为取消关注
            attention.is_cancel = 1
            try:
                attention.save()
            except DatabaseError as e:
                logging.warning(e)
                result = {'respones': '取消关注异常'}
                return JsonResponse(result)
            result = {'respones': '已取消关注'}
            return JsonResponse(result)


def inquire_attentions(request):
    """查询关注"""
    # 获取用户id
    user_id = request.session.get('id', '')
    # 获取关注用户对象
    user_attentions = Attentions.objects.filter(user_id=user_id, is_cancel=0)
    # 获取用户关注对象信息
    user_attentions_infos = []
    for user_attention in user_attentions:
        user_attentions_infos.append([user_attention.attentions.id, user_attention.attentions.uname])
    result = {'user_attentions_infos': user_attentions_infos}
    return JsonResponse(result)


def inquire_fan(request):
    """查询粉丝"""
    # 获取用户id
    user_id = request.session.get('id', '')
    # 获取粉丝用户对象
    user_fans = Attentions.objects.filter(attentions_id=user_id, is_cancel=0)
    # 获取用户全部粉丝的信息
    user_fans_infos = []
    for user_fan in user_fans:
        user_fans_infos.append([user_fan.user.id, user_fan.user.uname])
    result = {'user_fans_infos': user_fans_infos}
    return JsonResponse(result)
