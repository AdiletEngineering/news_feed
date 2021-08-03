from rest_framework import serializers

from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'url', 'order_num')


class NewsListSerializer(serializers.ModelSerializer):
    image = ImageSerializer(source='get_logo')
    class Meta:
        model = News
        fields = ('id', 'image', 'title')


class NewsDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = News
        fields = ('id', 'header_title', 'add_date', 'images', 'text')



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')





