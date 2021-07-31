from django.shortcuts import render

# Create your views here.
from rest_framework.pagination import LimitOffsetPagination

from .models import *
from .serializers import *
from rest_framework import generics


class NewsList(generics.ListCreateAPIView):
    serializer_class = NewsSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):

        lang = self.request.query_params.get('lang', 'kg')
        category = self.request.query_params.get('category')
        queryset = News.objects.filter(languages__name=lang)
        if category:
            queryset = News.objects.filter(categories__name=category)
        return queryset



class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer



class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LanguageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer