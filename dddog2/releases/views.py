from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.db import DatabaseError
import logging

from releases.models import States, Services, ServiceOrders


def test(request):
    """测试通迅"""
    return HttpResponse('this is releases test,is ok')


def add_states(request):
    """增加壮态列表"""
    # 获取前端数据
    snames = request.POST.getlist('sname')
    smarks = request.POST.getlist('smark')
    x = y = 0
    # 将前端数据转换成元组
    states_infos = zip(snames, smarks)
    print(snames, smarks,states_infos)
    new_states = []
    # 分别获取每一条前端数据
    for sname, smark in states_infos:
        # 判断前端数据选项是否为空
        if sname and smark:
            # 判断新增壮态标识是否存在,确保唯一
            if States.objects.filter(smark=smark).exists():
                x += 1
            else:
                # 创建新壮态
                new_states.append(States(sname=sname, smark=smark))
                y += 1
        else:
            x += 1
    try:
        # 将所有新壮态写入数据库内
        States.objects.bulk_create(new_states)
    except DatabaseError as e:
        logging.warning(e)
        result = {'response': '新增壮态异常'}
        return JsonResponse(result)
    result = {'response': '新增壮态成功' + str(y) + '条,失败' + str(x) + '条'}
    return JsonResponse(result)


def inquire_states(request):
    """查询壮态列表"""
    # 获取所有的壮态对象
    states = States.objects.all()
    states_infos = []
    # 获取所有壮态的信息
    for state in states:
        states_infos.append([state.id, state.sname, state.smark])
    result = {'response': states_infos}
    return JsonResponse(result)


def update_states(request):
    """修改壮态列表"""
    if request.POST.get('sid',''):
        state = States.objects.get(id=request.POST['sid'])
        if request.POST.get('sname',''):
            state.sname = request.POST['sname']
        try:
            state.save()
        except DatabaseError as e:
            logging.warning(e)
            result = {'response': '修改异常'}
            return JsonResponse(result)
        result = {'response': '修改成功'}
        return JsonResponse(result)
    else:
        result = {'response': '请选择要修改的壮态'}
        return JsonResponse(result)
