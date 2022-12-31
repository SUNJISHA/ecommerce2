from django.shortcuts import render, redirect
from.models import Customer
from.models import Seller
import random
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.

def common_master(request):
    return render(request,'common/commom_master.html')

def common_home(request):
    return render(request,'common/project_home.html')

def common_login(request):
    msg=""
    if request.method == 'POST' :
        user_name = request.POST['cus_name']
        password = request.POST['cus_password']

        try:
            customer = Customer.objects.get(email = user_name, password = password)
            request.session['customer'] = customer.id 
            return redirect('customers:cus_home')
        except Exception as e:
            print(e)
            msg = "User Name or Password Incorrect"
            # data from view to html will be passed in render() as dictionary
    return render(request,'common/login.html',{'message':msg})



def common_sell_login(request):
    msg=""
    if request.method == 'POST':

        user_name = request.POST['user_name']
        password = request.POST['password']

        # when we use get() to fetch data, we must use try except,
        # if the data is not found in the table,exception will be raised

        try:
            seller = Seller.objects.get(username = user_name, password = password)
            request.session['seller'] = seller.id 
            return redirect('sellers:Sel_home')
        except Exception as e:
            print(e)
            msg = "User Name or Password Incorrect"
            # data from view to html will be passed in render() as dictionary
    return render(request,'common/sell_login.html',{'message':msg})

def common_cus_reg(request):
    # by default, form method will be get

    if request.method == 'POST' : #when the submitt button clicked
        c_name = request.POST['fname']    # to get textbox data
        c_email = request.POST['email'] 
        c_address = request.POST['adrress']
        c_phone = request.POST['phonenumber']
        c_gender = request.POST['gender']
        c_password = request.POST['password']

        # in ORM, if we want to insert a data in table,
        # 1. Create an object of model class, here model class is Customer
        new_customer = Customer(customer_name = c_name, email = c_email, address = c_address,
        phone = c_phone, gender = c_gender, password = c_password )

        # call save() method

        new_customer.save()
        
    return render(request,'common/cus_reg.html')



def common_sell_reg(request):
     # by default, form method will be get

    if request.method == 'POST' : #when the submitt button clicked
        s_name = request.POST['fname']    # to get textbox data
        s_email = request.POST['email'] 
        s_address = request.POST['address']
        s_phone = request.POST['phone']
        s_gender = request.POST['gender']
        s_companyname = request.POST['company_name']
        s_account_holder = request.POST['account_holder']
        s_account_num = request.POST['act_num']
        ifsc = request.POST['ifsc']
        branch = request.POST['branch']
        seller_pic = request.FILES['image']

        user_name = random.randint(1111,9999)
        password = 'sel-' + str(user_name) + s_name    # result will be sel-2345-john
    

        # in ORM, if we want to insert a data in table,
        # 1. Create an object of model class, here model class is seller
        new_seller = Seller(seller_name = s_name, 
        seller_email = s_email,
        seller_address = s_address,
        seller_phone = s_phone,
        gender = s_gender,
        company_name = s_companyname,
        account_holder =  s_account_holder,
        account_num = s_account_num,
        ifsc =  ifsc, branch = branch, 
        seller_pic = seller_pic, 
        username = user_name, 
        password = password   )

        # call save() method

        new_seller.save()

        message = 'hai your username is  ' + str(user_name) + 'and your password is  ' + password

        #  sent mail function used to send email through our application
        # 1st argument -> subject
        # 2nd argument -> message
        # 3rd argument -> from email
        # 4th argument -> recipent list, here recipient list should be in an array format
        send_mail('user_name and password',
         message,
         settings.EMAIL_HOST_USER,
         [s_email,]
         )


    return render(request,'common/sell_reg.html')


