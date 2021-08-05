from rest_framework import serializers

from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('url', 'order_num')


class NewsListSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'header_title', 'text', 'add_date', 'images', 'categories', 'languages')

    def to_representation(self, instance):
        images_serializer = ImageSerializer(instance.images, many=True)
        return {'id': instance.id, 'images': images_serializer.data, 'title': instance.title}

    def create(self, validated_data):

        images = validated_data.pop('images')
        print('images -->> ', images)
        news = News.objects.create(**validated_data)

        for image in images:
            Image.objects.create(url=image['url'],
                                 order_num=image['order_num'],
                                 news=news)
        return news







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
