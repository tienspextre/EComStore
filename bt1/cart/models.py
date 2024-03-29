from django.db import models 
from catalog.models import Product 

class CartItem(models.Model): 
 cart_id = models.CharField(max_length=50) 
 date_added = models.DateTimeField(auto_now_add=True) 
 quantity = models.IntegerField(default=1) 
 product = models.ForeignKey('catalog.Product', unique=False) 
 
 class Meta: 
    db_table = 'cart_items' 
    ordering = ['date_added'] 
 
 def total(self): 
    return self.quantity * self.product.price 
 
 def name(self): 
    return self.product.name 
 
 def price(self): 
    return self.product.price
 