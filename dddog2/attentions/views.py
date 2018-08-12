from django.shortcuts import render,HttpResponse


def test(request):
    """测试通迅"""
    return HttpResponse('this is attentions view test,is ok!')
