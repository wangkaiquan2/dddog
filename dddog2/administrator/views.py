from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
import logging
from django.db import DatabaseError

from administrator.models import Limits
from users.models import Groups, Users


def test(request):
    """测试通迅"""
    return HttpResponse('this is administrator,is ok')


def add_limits(request):
    """添加权限"""
    # 将从前端获取的权限标识与描述列表生成新的元组
    limits_descriptions = zip(request.POST.getlist('limits'), request.POST.getlist('descriptions'))
    new_limits = []
    x = y = 0
    # 将元组遍历,批量添加权限
    for limit, description in limits_descriptions:
        # 判断每一组权限的标识与描述是否为空
        if limit and description:
            # 判断权限标识是否已经存在,确保标识的唯一性
            if Limits.objects.filter(limit=limit).exists():
                y += 1
            else:
                # 将新生成的权限添加到权限列表内等待保存入数据库
                new_limits.append(Limits(limit=limit, limit_description=description))
                x += 1
        else:
            y += 1
    # 将权限列表内的数据写入数据库
    try:
        Limits.objects.bulk_create(new_limits)
    except DatabaseError as e:
        logging.warning(e)
        result = {'response': '新增权限异常,请重新添加'}
        return HttpResponse(json.dumps(result))
    result = {'response': '新增权限成功' + str(x) + '条,' + '失败' + str(y) + '条'}
    return HttpResponse(json.dumps(result))


def inquire_limits(request):
    """查询所有权限"""
    # 查询所有权限
    limits = Limits.objects.all()
    limits_l = []
    # 将所有权限信息遍历出来
    for limit in limits:
        limits_l.append({
            'lid': limit.id,
            'limit': limit.limit,
            'description': limit.limit_description,
        })
    result = {'response': limits_l}
    return JsonResponse(result)


def update_limits(request):
    """修改权限"""
    # 判断是否传入权限id
    if request.POST.get('lid', ''):
        # 查询权限对象
        limit = Limits.objects.get(id=request.POST['lid'])
        # 修改对应的权限内容
        if request.POST.get('limit', ''):
            # 判断权限标识是否存在
            if Limits.objects.filter(limit=request.POST['limit']).exists():
                result = {'response': '权限标识已存在'}
                return JsonResponse(result)
            else:
                limit.limit = request.POST['limit']
        if request.POST.get('description', ''):
            limit.limit_description = request.POST['description']
        # 将新内容写入数据库内
        try:
            limit.save()
        except DatabaseError as e:
            logging.warning(e)
            result = {'response': '权限修改异常'}
            return HttpResponse(json.dumps(result))
        result = {'response': '权限修改成功'}
        return JsonResponse(result)
    else:
        result = {'response': '请传入正确的参数'}
        return HttpResponse(json.dumps(result))


def delete_limits(request):
    """删除权限"""
    try:
        # 筛选出权限对象并批量删除
        Limits.objects.filter(id__in=request.POST.getlist('lid')).delete()
    except DatabaseError as e:
        logging.warning(e)
        result = {'response': '删除权限异常'}
        return JsonResponse(result)
    result = {'response': '删除权限完成'}
    return JsonResponse(result)


def create_groups(request):
    """创建组"""
    # 判断组选项是否为空
    if request.POST.get('gname', '') and request.POST.get('gmark', ''):
        # 判断组标识是否存在,确保唯一
        if Groups.objects.filter(gname=request.POST['gname']).exists():
            result = {'response': '组标识已存在'}
            return JsonResponse(result)
        else:
            # 创建新组
            new_group = Groups(gname=request.POST['gname'], gmark=request.POST['gmark'])
            try:
                # 将新组写入数据库内
                new_group.save()
            except DatabaseError as e:
                logging.warning(e)
                result = {'response': '创建组异常'}
                return JsonResponse(result)
            result = {'response': '创建组成功'}
            return JsonResponse(result)

    else:
        result = {'response': '组选项不能为空'}
        return JsonResponse(result)


def update_groups(request):
    """修改组"""
    if request.POST.get('gid', ''):
        group = Groups.objects.get(id=request.POST['gid'])
        if request.POST.get('gname', ''):
            group.gname = request.POST['gname']
        if request.POST.get('is_active', ''):
            group.is_active = request.POST['is_active']
        try:
            group.save()
        except DatabaseError as e:
            logging.warning(e)
            result = {'response': '组信息修改失败'}
            return JsonResponse(result)
        result = {'response': '组信息修改成功'}
        return JsonResponse(result)
    else:
        result = {'response': '缺少组相关标识'}
        return JsonResponse(result)


def inquire_groups_infos(request):
    """查询组信息"""
    groups = Groups.objects.all()
    group_infos = []
    for group in groups:
        group_infos.append({
            'gid': group.id,
            'gname': group.gname,
            'gmark': group.gmark,
            'is_active': group.is_active,
            'ctime': group.ctime,
        })
    result = {'response': group_infos}
    return JsonResponse(result)


def inquire_group_users(request):
    """查询组用户"""
    group = Groups.objects.get(id=request.GET['gid'])
    group_users_infos = []
    for guser in group.gusers.all():
        group_users_infos.append({
            'uid':guser.id,
            'uname':guser.uname,
            'is_active':guser.is_active,
            'ctime':guser.ctime,
        })
    result = {'response': group_users_infos}
    return JsonResponse(result)


def inquire_group_limits(request):
    """查询组权限"""
    group = Groups.objects.get(id=request.GET['gid'])
    group_limits_infos = []
    for limit in group.glimits.all():
        group_limits_infos.append({
            'lid':limit.id,
            'limit':limit.limit,
            'limit_description':limit.limit_description,
        })
    result = {'response': group_limits_infos}
    return JsonResponse(result)


def add_group_users(request):
    """添加组用户"""
    pass


def remove_group_users(request):
    """删除组用户"""
    pass


def add_group_limits(request):
    """添加组权限"""
    pass


def remove_group_limits(request):
    """删除组权限"""
    pass