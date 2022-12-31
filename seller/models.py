from django.db import models
from common.models import Seller

# Create your models here.

class Product(models.Model) :
    seller = models.ForeignKey(Seller,on_delete = models.CASCADE)
    pro_name = models.CharField(max_length = 20)
    pro_description = models.CharField(max_length = 100)
    pro_number = models.BigIntegerField()
    pro_price = models.FloatField()
    pro_stock = models.IntegerField()
    pro_image = models.ImageField(upload_to='product/')
