from main import models
from django.contrib.auth.models import User
from rest_framework import serializers, pagination, viewsets,generics
from main import serializers


#vendor
class VendorList(generics.ListCreateAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class=serializers.VendorSerializers
 

class VendorDetail(generics.RetrieveDestroyAPIView):
      queryset=models.Vendor.objects.all()
      serializer_class=serializers.VendorDetailSerializers

#Product
class ProductList(generics.ListCreateAPIView):
    queryset=models.Product.objects.all()
    serializer_class=serializers.ProductListSerializers
    pagination_class=pagination.PageNumberPagination

class ProductDetail(generics.RetrieveDestroyAPIView):
      queryset=models.Product.objects.all()
      serializer_class=serializers.ProductDetailSerializers



#Customer
class CustomerList(generics.ListCreateAPIView):
    queryset=models.Customer.objects.all()
    serializer_class=serializers.CustomerSerializers
  

class CustomerDetail(generics.RetrieveDestroyAPIView):
      queryset=models.Customer.objects.all()
      serializer_class=serializers.CustomerDetailSerializers


#order
class OrderList(generics.ListCreateAPIView):
    queryset=models.Order.objects.all()
    serializer_class=serializers.OrderSerializers
  

class OrderDetail(generics.ListAPIView):
      #queryset=models.OrderItems.objects.all()
      serializer_class=serializers.OrderDetailSerializers

      def get_queryset(self):

        order_id = self.kwargs['pk']
        print(order_id)
        order = models.Order.objects.get(id=order_id)
        order_items = models.OrderItems.objects.filter(order=order)

        return order_items
      

#customer address
class CustomerAddressViewSet(viewsets.ModelViewSet):
     queryset=models.CustomerAddress.objects.all()
     serializer_class=serializers.CustomerAddressSerializers



#Product rating and reviews
class  ProductRatingReviewsViewSet(viewsets.ModelViewSet):
     queryset=models.ProductRatingReviews.objects.all()
     serializer_class=serializers.ProductRatingReviewsSerializers
