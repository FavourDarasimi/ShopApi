from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Product, Cart, CartItem, Transaction, Order
from .Serializers.store_serializer import CategorySerializer, ProductSerializer, CartSerializer, CartItemSerializer, \
    TransactionSerializer, OrderSerializer

#Category
class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class UpdateCategoryView(APIView):
    def put(self,request,pk):
        category = Category.objects.get(pk=pk)
        serializer =CategorySerializer(category,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'error': 'Error updating category'}, status=status.HTTP_400_BAD_REQUEST)


class DetailCategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request,pk, *args, **kwargs):
        serializer = CategorySerializer(Category.objects.get(pk=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)



#Product
class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UpdateProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, pk, *args, **kwargs):
        serializer = ProductSerializer(Product.objects.get(pk=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


class DetailProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request,pk, *args, **kwargs):
        serializer = ProductSerializer(Product.objects.get(pk=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)



#Cart
class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class UpdateCartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def post(self, request, pk, *args, **kwargs):
        serializer = CartSerializer(Cart.objects.get(pk=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

class DetailCartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def list(self, request,pk, *args, **kwargs):
        serializer = CartSerializer(Cart.objects.get(pk=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)



#CartItem
class CartItemView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class UpdateCartItemView(APIView):
    def put(self,request,pk):
        cartItem = CartItem.objects.get(pk=pk)
        serializer =CartItemSerializer(cartItem,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'error': 'Error updating category'}, status=status.HTTP_400_BAD_REQUEST)

class DetailCartItemView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def list(self, request,pk, *args, **kwargs):
        serializer = CartItemSerializer(CartItem.objects.get(pk=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteCartItemView(APIView):
    def delete(self,request,pk):
        cartItem = CartItem.objects.get(pk=pk)
        cartItem.delete()
        return Response({'delete':'Item Removed Successfully'},status=status.HTTP_204_NO_CONTENT)



#Transaction
class TransactionView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class UpdateTransactionView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def post(self, request, pk, *args, **kwargs):
        serializer = TransactionSerializer(Transaction.objects.get(pk=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

class DetailTransactionView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def list(self, request,pk, *args, **kwargs):
        serializer = TransactionSerializer(Transaction.objects.get(pk=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)



#Order
class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UpdateOrderView(APIView):
    def put(self,request,pk):
        order = Order.objects.get(pk=pk)
        serializer =OrderSerializer(order,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'error': 'Error updating category'}, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.

class DeleteOrderView(APIView):
    def delete(self,request,pk):
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response({'delete':'Order Deleted Successfully'},status=status.HTTP_204_NO_CONTENT)



class DetailOrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request,pk, *args, **kwargs):
        serializer = OrderSerializer(Order.objects.get(pk=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)
