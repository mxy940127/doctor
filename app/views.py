from django.shortcuts import render
from django.conf import settings
from .models import Admin, ApiInvoke, Patient
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AdminSerializer, PatientSerializer
from .responseDicts import ADMIN_ACCOUNT_EXISTS, ADMIN_ACCOUNT_ERROR, SUCCESS, SERVER_ERROR, INVOKE_USED_OUT
import numpy
import hashlib
# Create your views here.


@api_view(['POST'])
def add_admin(request):
    try:
        admin = Admin.objects.get(account=request.data.get('account'))
    except Admin.DoesNotExist:
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            api_invoke = ApiInvoke(
                api='patient/add',
                count=60,
                available_count=60,
            )
            api_invoke.save()
            response_data = dict()
            response_data['code'] = 0
            response_data['msg'] = '操作成功'
            response_data['data'] = serializer.data
            return Response(response_data)
        else:
            return Response(ADMIN_ACCOUNT_EXISTS)
    else:
        return Response(ADMIN_ACCOUNT_EXISTS)


@api_view(['POST'])
def admin_login(request):
    try:
        admin = Admin.objects.get(account=request.data.get('account'))
    except Admin.DoesNotExist:
        return Response(ADMIN_ACCOUNT_ERROR)
    password = request.data.get('password')
    secret = hashlib.md5(password.encode('utf-8'))
    if secret.hexdigest() == admin.password:
        request.session.set_expiry(60*60*12)
        request.session['account'] = admin.account
        return Response(SUCCESS)
    else:
        return Response(ADMIN_ACCOUNT_ERROR)


@api_view(['POST'])
def distribute_patient(request):
    temp_plan = True
    try:
        api_invoke = ApiInvoke.objects.get(api__contains='patient/add')
    except ApiInvoke.DoesNotExist:
        return Response(SERVER_ERROR)
    if api_invoke.available_count > 0:
        number = numpy.random.randint(10000)
        if number < 5000:
            temp_plan = True
            patient = Patient(
                name=request.data.get('name'),
                plan=temp_plan
            )
            patient.save()
            return Response(SUCCESS)
        else:
            temp_plan = False
            patient = Patient(
                name=request.data.get('name'),
                plan=temp_plan
            )
            patient.save()
            return Response(SUCCESS)
    else:
        return Response(INVOKE_USED_OUT)


@api_view(['GET'])
def patient_list(request):
    patient_list_true = Patient.objects.filter(plan=True)
    patient_list_false = Patient.objects.filter(plan=False)
    serializer_true = PatientSerializer(patient_list_true, many=True)
    serializer_false = PatientSerializer(patient_list_false, many=True)
    response_data = dict()
    response_data['code'] = 0
    response_data['msg'] = '操作成功'
    response_data['true'] = serializer_true.data
    response_data['false'] = serializer_false.data
    return Response(response_data)

