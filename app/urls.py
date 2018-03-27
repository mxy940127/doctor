#Author:mxy940127
# -*- coding:utf-8 -*-
#  @Author   : Eric.Miao


from django.urls import path
from django.conf.urls import url, include
from .views import distribute_patients, get_distribution_list


urlpatterns = [
    url(r'^distribute', distribute_patients),
    url(r'^list', get_distribution_list),
]
