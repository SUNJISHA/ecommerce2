from django.urls import path
from . import views
app_name='customers'

urlpatterns=[
     path('home',views.cus_home,name="cus_home"),

     path('cart',views.cus_cart,name="cus_cart"),
     path('delete/<int:id>',views.cus_delet_item,name="cus_delete"),


     path('changepassword',views.cus_chpass,name="cus_chpass"),

     path('productdetails/<int:pid>',views.cus_prcdtdetails,name="cus_prodetails"),

     path('myorder',views.cus_myorder,name="cus_myorder"),

     path('profile',views.cus_profile,name="cus_profile"),

     path('editprofile',views.cus_editprofile,name="cus_editprofile"),

     path('logout',views.logout,name="cus_logout"),
]