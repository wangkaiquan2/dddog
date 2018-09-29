from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, FileResponse
from django.db import DatabaseError
import logging
import datetime

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
    print(snames, smarks, states_infos)
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
    if request.POST.get('sid', ''):
        state = States.objects.get(id=request.POST['sid'])
        if request.POST.get('sname', ''):
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


def create_service(request):
    """发布服务"""
    # 获取前端信息
    user = request.session.get('id', '')
    service_number = 20180812001
    role = 2
    method = request.POST.get('method', '')
    title = request.POST.get('title', '')
    details = request.POST.get('details', '')
    appoint_time = request.POST.get('appoint_time', '')
    remark = request.POST.get('remark', '')
    area = request.POST.get('area', '')
    price = request.POST.get('price', '')
    unit = request.POST.get('unit', '')
    # 创建新的服务记录
    new_service = Services(user=user, service_number=service_number, role=int(role), method=int(method),
                           title=title, details=details, appoint_time=appoint_time, remark=remark, area=area,
                           price=float(price), unit=int(unit))
    try:
        new_service.save()
    except DatabaseError as e:
        logging.warning(e)
        result = {'response': '发布服务失败'}
        return JsonResponse(result)
    result = {'response': '发布服务成功'}
    return JsonResponse(result)


def create_demand(request):
    """发布需求"""
    # 获取前端信息
    user = request.session.get('id', '')
    service_number = 20180812001
    role = 1
    method = request.POST.get('method', '')
    title = request.POST.get('title', '')
    details = request.POST.get('details', '')
    appoint_time = request.POST.get('appoint_time', '')
    remark = request.POST.get('remark', '')
    area = request.POST.get('area', '')
    price = request.POST.get('price', '')
    unit = request.POST.get('unit', '')
    # 创建新的需求记录
    new_service = Services(user=user, service_number=service_number, role=int(role), method=int(method),
                           title=title, details=details, appoint_time=appoint_time, remark=remark, area=area,
                           price=float(price), unit=int(unit))
    try:
        new_service.save()
    except DatabaseError as e:
        logging.warning(e)
        result = {'response': '发布需求失败'}
        return JsonResponse(result)
    result = {'response': '发布需求成功'}
    return JsonResponse(result)


def upload_files(request):
    """上传图片"""
    if request.method == 'GET':
        return render(request, 'upload_files.html')
    else:
        # 获取上传文件的数据
        image = request.FILES['image']
        print(image)
        print(image.name)
        # 获取上传文件的名字并生成新的名字
        name = str(datetime.datetime.today()) + image.name
        print(name)
        # 生成文件保存路径
        path = 'static/upload/' + name
        print(path)
        # 打开文件
        with open(path, 'wb') as f:
            # 判断文件是否大于2.5
            if image.multiple_chunks():
                print('>2.5')
                # 大于2.5时采用chunks方法保存文件
                for chunk in image.chunks():
                    f.write(chunk)
            else:
                print('<2.5')
                # 小于2.5时采用read方法保存文件
                f.write(image.read())
                print(image.read())
        return JsonResponse({'image.name': image.name, 'path': path})


def download(request):
    """"""
    return render(request, 'download.html')


def download_files(request):
    """下载文件"""
    path = 'static/upload/01_one.jpg'

    # 读取文件数据
    def read_files(path, chunk_size=512):
        with open(path, 'rb') as f:
            while True:
                file = f.read(chunk_size)
                if file:
                    yield file
                else:
                    break

    # 将打开文件响应给前端
    response = FileResponse(read_files(path))
    # 设置请求头
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format('01_one.jpg')
    return response


def upload_excel(request):
    """上传excel文件"""
    pass
