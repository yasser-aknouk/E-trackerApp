from ast import arg
from django.db import models
from .scraper import get_data

# Create your models here.
class product(models.Model):
    product_name=models.CharField(max_length=200,blank=True)
    url_product=models.URLField()
    current_price=models.FloatField(blank=True)
    old_product_price=models.FloatField(default=0)
    rating=models.CharField(max_length=200,blank=True)
    produc_details=models.CharField(max_length=200,blank=True)
    difference_price=models.FloatField(default=0)
    created=models.DateTimeField(auto_now_add=True)
    Maj=models.DateField(auto_now=True)


    def __str__(self):
        return str(self.product_name)

    class Meta:
         ordering = ('difference_price','-created')
    
    def save(self, *args, **kwargs):
        name, price, rating, details=get_data(self.url_product)
        old_price=self.current_price
        if self.current_price:
            if price != old_price:
                diff = float(price - old_price)
                self.difference_price=round(diff,2)
                self.old_product_price=old_price
               
        else:
            self.difference_price=0
            self.old_product_price=0
        
        
        self.product_name=name
        self.current_price=price
        self.rating=rating
        self.produc_details=details
        
        super().save(*args,**kwargs)
   
          
       
