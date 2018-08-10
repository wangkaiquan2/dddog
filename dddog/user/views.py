from django.shortcuts import render,HttpResponse
from django.http import JsonResponse


def test(request):
    """测试通迅"""
    return HttpResponse('this is user test,is ok')


