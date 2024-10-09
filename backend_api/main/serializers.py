from rest_framework import serializers
from main import models


class VendorSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['id','user','address']
    def __init__(self,*args, **kwargs):
        super(VendorSerializers,self).__init__(*args, **kwargs)
       # self.Meta.depth = 1

class VendorDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['id','user','address']
    def __init__(self,*args, **kwargs):
        super(VendorDetailSerializers,self).__init__(*args, **kwargs)
        #self.Meta.depth = 1
     
class ProductListSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id','vendor','category','title','detail', 'price']
    def __init__(self,*args, **kwargs):
        super(ProductListSerializers,self).__init__(*args, **kwargs)
       # self.Meta.depth = 1

class ProductDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id','vendor','category','title','detail', 'price']
    def __init__(self,*args, **kwargs):
        super(ProductDetailSerializers,self).__init__(*args, **kwargs)
       # self.Meta.depth = 1


#Customer 
class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['id','user','mobile']
    def __init__(self,*args, **kwargs):
        super(CustomerSerializers,self).__init__(*args, **kwargs)
       # self.Meta.depth = 1

class CustomerDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['id','user','mobile']
    def __init__(self,*args, **kwargs):
        super(CustomerDetailSerializers,self).__init__(*args, **kwargs)
        #self.Meta.depth = 1


#order 
class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ['id','customer','order_time']
    def __init__(self,*args, **kwargs):
        super(OrderSerializers,self).__init__(*args, **kwargs)
       # self.Meta.depth = 1

class OrderDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItems
        fields = ['id','order','product']
    def __init__(self,*args, **kwargs):
        super(OrderDetailSerializers,self).__init__(*args, **kwargs)
        #self.Meta.depth = 1


#customer address
class CustomerAddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerAddress
        fields = ['id','customer','address']
    def __init__(self,*args, **kwargs):
        super(CustomerAddressSerializers,self).__init__(*args, **kwargs)
        #self.Meta.depth = 1


class CustomerAddressDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerAddress
        fields = ['id','customer','address']
    def __init__(self,*args, **kwargs):
        super(CustomerAddressDetailSerializers,self).__init__(*args, **kwargs)
        #self.Meta.depth = 