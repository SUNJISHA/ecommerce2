
from django.urls import path
from . import views
app_name='sellers'

urlpatterns=[
     
     path('sell_home',views.sel_home,name="Sel_home"),

     path('addproduct',views.sel_addproduct,name="addproduct"),

     path('changepass',views.sel_changepass,name="changepass"),

     path('profile',views.sel_profile,name="sel_profile"),

     path('updatestock',views.sel_update_stock,name="update_stock"),

     path('order_history',views.sel_order_history,name="order_history"),

     path('editprofile',views.sel_edit_profile,name="seller_editprofile"),

     path('productcatalog',views.sel_product_catalog,name="product_catalog"),

     path('recentorder',views.sel_recent_order,name="recent_order"),

]