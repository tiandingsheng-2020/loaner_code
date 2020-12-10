from django.http import HttpResponse,JsonResponse,HttpRequest,HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from loaner_list.models import Loaner
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoanerSerializer
import json
import simplejson
import logging
# 查询所有
def get_index_page(request):
    all_loaner = Loaner.objects.all()
    # 测试Django ORM 的Models API filter函数.过滤
    test2 = Loaner.objects.filter(loaner_status__exact=False)
    for i in test2:
        print(i.loaner_request)
    return render(request,'loaners/index2.html',

                  {
                    'loaner_list' : all_loaner
                  }
                  )


# 不用模版，使用json来做前后端数据的交互.
@csrf_exempt
def reg(request:HttpRequest):
    print(request,'~~~~~~~~')
    try:
        payload=simplejson.loads(request.body)
        name = payload['name']
        age = payload['age']
        print(name,age)
        return HttpResponse("Welcome DS.")

    except Exception as e:
        logging.info(e)
        return HttpResponseBadRequest()

''' 函数式编程'''

@api_view(['GET', 'POST'])
def Loaner_list(request):
    # 获取所有信息或新增后的所有信息
    if request.method == 'GET':
        l = LoanerSerializer(instance=Loaner.objects.all(), many=True)
        return Response(data = l.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        l = LoanerSerializer(data=request.data)
        if l.is_valid():
            l.save()
            return Response(data = l.data, status=status.HTTP_201_CREATED)
        return Response(l.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Loaner_update(request, pk):
    ''' 获取。更新，删除一个信息 '''
    try:
        loaner = Loaner.objects.get(pk=pk)# 此处的pk为每条数据的主键.
    except Loaner.DoesNotExist:
        return Response(data={'msg':'没有找到该信息'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        if request.method == 'GET':
            l = LoanerSerializer(instance=loaner)
            return Response(data=l.data, status=status.HTTP_200_OK)
            # 更新
        elif request.method == 'PUT':
            l = LoanerSerializer(instance=loaner, data=request.data)
            if l.is_valid():
                l.save()
                return Response(l.data, status=status.HTTP_200_OK)
        elif request.method == 'DELETE':
            loaner.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

 # 增加

def add_loaner(request:HttpRequest):
    payload = simplejson.loads(request.body.decode('utf-8'))
    loaner_sn = payload['loaner_sn']
    loaner_request = payload['loaner_request']
    loaner_status = payload['loaner_status']
    loaner = Loaner()
    loaner.loaner_sn = loaner_sn
    loaner.loaner_request = loaner_request
    loaner.loaner_status = loaner_status
    try:
        loaner.save()
        return JsonResponse()
    except Exception as e:
        logging.info(e)
        return HttpResponseBadRequest()


# 查找
def search_loaner(request):
    s_loaner = Loaner.objects.filter(loaner_status__exact=False)
    return HttpResponse(s_loaner)



