from rest_framework import serializers

from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'



class NewsSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = News
        fields = '__all__'



class NewsDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = News
        fields = '__all__'



class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'



