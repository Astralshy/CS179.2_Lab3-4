from django.shortcuts import render
from django.http import JsonResponse

from .models import User, Product, Cart
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer,ProductSerializer, CartSerializer
from django.http import Http404

class ProductView(APIView):
    def get(self,request,format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductPKView(APIView):
    def get_object(self,pk):
        try:
            return Product.objects.get(pk=pk)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk, format=None):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserView(APIView):
    def get(self,request,format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserPKView(APIView):
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk, format=None):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CartView(APIView):
    def get(self,request,format=None):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)


class CartPKView(APIView):
    def get_object(self,pk):
        try:
            return Cart.objects.get(pk=pk)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        cart = self.get_object(pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cart = Cart.objects.get(pk=pk)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk, format=None):
        cart = Cart.objects.get(pk=pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)