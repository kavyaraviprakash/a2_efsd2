from django.conf.urls import url
from . import views
from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from .views import ChartData

app_name = 'portfolio'

# router = routers.DefaultRouter()
# router.register(r'customers_json', views.CustomerList)

urlpatterns = [

    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('stock_list', views.stock_list, name='stock_list'),
    path('stock/create/', views.stock_new, name='stock_new'),
    path('stock/<int:pk>/edit/', views.stock_edit, name='stock_edit'),
    path('stock/<int:pk>/delete/', views.stock_delete, name='stock_delete'),
    path('investment_list/', views.investment_list, name = 'investment_list'),
    path('investment/<int:pk>/edit/', views.investment_edit, name = 'investment_edit'),
    path('investment/create/', views.investment_new, name='investment_new'),
    path('investment/<int:pk>/delete/', views.investment_delete, name='investment_delete'),
    path('customer/<int:pk>/portfolio/', views.portfolio, name='portfolio'),
    path('customers_json/', views.CustomerList.as_view()),
    path('customer/<int:pk>/portfolio/pdf/', views.generate_pdf_view, name='generate_pdf_view'),
    path('customer/<int:cust_pk>/piechart/', views.pie_chart, name='pie-chart'),
    path('customer/<int:pk>/bar-chart/',ChartData.as_view(), name = 'chartdata'),
]
