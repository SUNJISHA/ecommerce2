from django.db import models

# Create your models here.


class Customer(models.Model) :
    customer_name = models.CharField(max_length = 20 )
    email = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    phone = models.BigIntegerField()
    gender = models.CharField(max_length = 20)
    password = models.CharField(max_length = 30)

class Seller(models.Model) :
    seller_name = models.CharField(max_length = 20)
    seller_email = models.CharField(max_length = 50)
    seller_address = models.CharField(max_length = 100)
    seller_phone = models.BigIntegerField()
    gender = models.CharField(max_length = 20)
    company_name = models.CharField(max_length = 30)
    account_holder = models.CharField(max_length = 20)
    account_num = models.BigIntegerField()
    ifsc = models.BigIntegerField() 
    branch = models.CharField(max_length = 30)
    seller_pic = models.ImageField(upload_to='seller')
    username = models.CharField(max_length = 20, default="")
    password = models.CharField(max_length = 20, default="")
   
    
    

    
