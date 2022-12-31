from django.shortcuts import render,redirect
from seller.models import Product
from customer.models import Customer
from . models import Cart

# Create your views here.


def cus_home(request):
    product = Product.objects.all() # select * from product \

    # product = [
    # {
        # seller : 1,
        # product_name : 'labtop',
        # description : 'dwdw'
        # -------------------
     # }'
     # {
           # seller : 2 
           # product_name : 'labtop',
           # description : 'dwdw'
           # -------------------
      # }
     # ];

    # we pass data from view to html in dictionary format


    return render(request,'customer/cust_home.html',{'product_list': product})

def cus_cart(request):
    product_cart = Cart.objects.filter(customer_id = request.session['customer'])

    return render(request,'customer/cart.html', {'cart_list':product_cart})

def cus_delet_item(request,id) :
    cart_item = Cart.objects.get(product = id, customer = request.session['customer'])
    cart_item.delete()

    return redirect('customers:cus_cart')



def cus_chpass(request):
    msg =''
    if request.method == 'POST' :
        customer = Customer.objects.get(id =  request.session['customer'])

        current_pass = request.POST['curent_pass']
        new_pass = request.POST['new_pass']
        confim_pass = request.POST['confirm_pass']

        if customer.password == current_pass :

            if new_pass == confim_pass :

                customer.password = new_pass
                customer.save()
                msg = 'password change '
            else :
                msg = 'password doesnot match'
        else :
            msg ='incorrect password'

    return render(request,'customer/changepass.html',{'msg':msg})

def cus_prcdtdetails(request,pid):
    msg = ''
    product_data = Product.objects.get(id = pid)  # fetching single data fom table

    if request.method == 'POST' :
        product_id = request.POST['pid']

        item_exist = Cart.objects.filter(product_id = product_id, customer_id = request.session['customer']).exists()
        if not item_exist : # if item_exist == flase
            cart_item = Cart(product_id = product_id, customer_id = request.session['customer'])
            cart_item.save() 
            
          
            return redirect('customers:cus_cart')
        else :
                msg = 'Item Already in cart'
    
    return render(request,'customer/prdct_details.html',{'product' : product_data, 'msg':msg})

def cus_myorder(request):
    return render(request,'customer/myorder.html')

def cus_profile(request):
    return render(request,'customer/cus_profile.html')

def cus_editprofile(request):
    return render(request,'customer/cus_editprof.html')

def logout(request):
    del request.session['customer']
    request.session.flush()
    return redirect('commons:login')
