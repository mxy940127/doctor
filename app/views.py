from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from django.conf import settings
import numpy as np


SUCCESS = {'code': 0, 'msg': '操作成功'}
INTERFACE_COUNT_FULL = {'code': 1, 'msg': '接口使用次数达到上限'}
PARAM_ERROR = {'code':2, 'msg': '参数错误'}


@api_view(['POST'])
def distribute_patients(request):
    if request.data.get('name'):
        name = request.data.get('name')
        if settings.COUNT > 0:
            number = np.random.randint(0, 100)
            if number > 49:
                settings.TREATMENT_GROUP.append(name)
                settings.COUNT = settings.COUNT - 1
                return Response(SUCCESS)
            else:
                settings.MATCHED_GROUP.append(name)
                settings.COUNT = settings.COUNT - 1
                return Response(SUCCESS)
        else:
            return Response(INTERFACE_COUNT_FULL)
    else:
        return Response(PARAM_ERROR)


@api_view(['GET'])
def get_distribution_list(request):
    SUCCESS['treatment'] = settings.TREATMENT_GROUP
    SUCCESS['matched'] = settings.MATCHED_GROUP
    return Response(SUCCESS)

