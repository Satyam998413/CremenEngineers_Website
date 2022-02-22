import django
from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField(timezone.now())
    desc2=models.CharField(max_length=300)
    category= models.CharField(max_length=50, default="")
    sub_category= models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    image= models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name
   
   