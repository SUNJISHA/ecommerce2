
from django.urls import path
from . import views
app_name='ecom_admin'

urlpatterns=[
     path('admin_home',views.admin_home,name="ad_home"),

     path('profile_admin',views.admin_profile,name="profile"),

     path('approve_seller',views.admin_approve_seller,name="approve_seller"),

     path('view_customer',views.admin_view_cust,name="view_cust"),

     path('view_seller',views.admin_view_seller,name="view_seller"),
]