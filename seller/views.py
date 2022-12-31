from django.shortcuts import render
from.models import Seller

# from seller.models import Product
from.models import Product

# Create your views here.

def sel_home(request):
    prof = Seller.objects.get(id=request.session['seller']) 

    return render(request,'seller/seller_home.html',{'seller_prof':prof })

def sel_addproduct(request):
    if request.method == 'POST' :
        pro_name = request.POST['product_name']
        pro_num = request.POST['product_number']
        pro_des = request.POST['description']
        pro_price = request.POST['price']
        pro_stock = request.POST['stock']
        pro_image = request.FILES['pro_images']

        new_product = Product(pro_name = pro_name,
        pro_description = pro_des,
        pro_number = pro_num,
        pro_price = pro_price,
        pro_stock = pro_stock,
        pro_image = pro_image,
        seller_id = request.session['seller']
        )

        new_product.save()



    return render(request,'seller/addproduct.html')

def sel_changepass(request):

    msg =''
    if request.method == 'POST' :

        current_pass = request.POST['curent_pass']
        new_pass = request.POST['new_pass']
        confim_pass = request.POST['confirm_pass']

        seller = Seller.objects.get(id =  request.session['seller'])


        if seller.password == current_pass :

            if new_pass == confim_pass :

                Seller.objects.filter(id =  request.session['seller']).update(password = new_pass)
                msg = 'password change '
            else :
                msg = 'password doesnot match'
        else :
            msg ='incorrect password'
    return render(request,'seller/changepass.html',{'msg':msg})

def sel_profile(request):
    prof = Seller.objects.get(id=request.session['seller']) 

    return render(request,'seller/sell_profile.html',{'seller_prof':prof })

def sel_update_stock(request):
    return render(request,'seller/update_stock.html')

def sel_order_history(request):
    return render(request,'seller/order_history.html')

def sel_edit_profile(request):
    return render(request,'seller/sel_editprofile.html')

def sel_product_catalog(request):
    products = Product.objects.filter(seller_id = request.session['seller'])
    return render(request,'seller/product_catalog.html',{'products':products})

def sel_recent_order(request):
    return render(request,'seller/recent_order.html')