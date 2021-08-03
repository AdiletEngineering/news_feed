from rest_framework import serializers

from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'url', 'order_num')


class NewsListSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = News
        fields = ('id', 'images', 'title')

    # def create(self, validated_data):
    #
    #     images = validated_data.pop('images')
    #     lang = validated_data.pop('')
    #
    #     news = News.objects.create(**validated_data)
    #
    #     for image in images:
    #         Image.objects.create(url=image['url'],
    #                              order_num=image['order_num'], news=news)







class NewsDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = News
        fields = ('id', 'header_title', 'add_date', 'images', 'text')



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'languages')

    def to_representation(self, instance):
        return {'id': instance.id, 'name': instance.name, 'languages': instance.languages.id}
