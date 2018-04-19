#Author : mxy940127
# -*- coding:utf-8 -*-
#  @Author   : Eric.Miao
from django.conf.urls import url,include
from .views import distribute_patient, add_admin, admin_login, patient_list

urlpatterns = [
    url(r'^patient/add', distribute_patient),
    url(r'^admin/add', add_admin),
    url(r'^admin/login', admin_login),
    url(r'^patient/list', patient_list)
]