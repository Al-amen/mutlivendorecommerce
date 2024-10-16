from django.db import models 

from django.contrib.auth.models import User
#vendor model

class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True)

    def __str__(self):
        return self.user.username
    

# product Catagory

class PoductCategory(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    

    def __str__(self):
        return self.title

# Product
class Product(models.Model):
    category = models.ForeignKey(PoductCategory, on_delete=models.SET_NULL,null=True, related_name="category_product")
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    price = models.FloatField()
    
    def __str__(self):
        return self.title


# customer model
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.PositiveBigIntegerField()

    def __str__(self):
        return self.user.username


# order model
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)

    

# order item model
class OrderItems(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE , related_name="order_items")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title
    
#Customer Address
class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer_address")
    address = models.TextField()
    defualt_address = models.BooleanField(default=True)

    def __str__(self):
        return self.address

#Product rating and reviews
class ProductRatingReviews(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customers_rating")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_ratings")
    rating = models.IntegerField()
    reviews = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rating} - {self.reviews}"
