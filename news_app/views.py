from django.shortcuts import render
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import generics

from .models import *
from .serializers import *



class NewsList(generics.ListCreateAPIView):
    serializer_class = NewsListSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        lang = self.request.query_params.get('lang')
        category = self.request.query_params.getlist('category')
        queryset = News.objects.filter(languages__name=lang)
        if category:
            queryset = queryset.filter(categories__id__in=category)
        return queryset



class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer



class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



