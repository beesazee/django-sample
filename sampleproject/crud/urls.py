__author__ = 'sibi'

from django.conf.urls import patterns,url
from crud import views

urlpatterns = patterns('',
    url(r'^$',views.employee_list,name='employee_list'),
    url(r'^new$',views.employee_create,name='employee_new'),
    url(r'^edit/(?P<pk>\d+)$',views.employee_update,name='employee_update'),
    url(r'^show/(?P<pk>\d+)$',views.employee_show,name='employee_show'),
    url(r'^delete/(?P<pk>\d+)$',views.employee_delete,name='employee_delete'),
)
