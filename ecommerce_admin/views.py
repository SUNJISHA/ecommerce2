from django.shortcuts import render

# Create your views here.

def admin_home(request):
    return render(request,'ecommerce_admin/admin_home.html')


def admin_profile(request):
    return render(request,'ecommerce_admin/profile.html')

def admin_approve_seller(request):
    return render(request,'ecommerce_admin/approve_seller.html')

def admin_view_cust(request):
    return render(request,'ecommerce_admin/view_cust.html')

def admin_view_seller(request):
    return render(request,'ecommerce_admin/view_seller.html')