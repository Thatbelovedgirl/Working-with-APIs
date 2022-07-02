from django.shortcuts import render
import rest_framework.generics
from rest_framework import generics
from Links.serializers import LinkSerializer
from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView, UpdateAPIView, DestroyAPIView
from Links import serializers
from .models import Link

# Create your views here.
class PostListApi(generics.ListAPIView):
    queryset=Link.objects.filter(active=True)
    serializer_class=LinkSerializer

class PostCreateApi(generics.CreateAPIView):
    queryset=Link.objects.filter(active=True)
    serializer_class=LinkSerializer

class PostDetailApi(generics.RetrieveAPIView):
    queryset=Link.objects.filter(active=True)
    serializer_class=LinkSerializer

class PostUpdateApi(generics.UpdateAPIView):
    queryset=Link.objects.filter(active=True)
    serializer_class=LinkSerializer

class PostDeleteApi(generics.DestroyAPIView):
    queryset=Link.objects.filter(active=True)
    serializer_class=LinkSerializer




