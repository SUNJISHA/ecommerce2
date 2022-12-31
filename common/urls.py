from django.urls import path
from . import views
app_name='commons'

urlpatterns=[
     path('master',views.common_master,name="master"),
     path('project_home',views.common_home,name="commom_home"),
     path('login',views.common_login,name="login"),
     path('sell_login',views.common_sell_login,name="sell_login"),
     path('cus_reg',views.common_cus_reg,name="cus_reg"),
     path('sell_reg',views.common_sell_reg,name="sell_reg"),
     
     
]