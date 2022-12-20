from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, Tovarlar, Korzina, Zakaz, Video

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created_at',)



class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'data')




class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class TovarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tovarlar
        fields = ('id', 'name', 'about', 'cost', 'type',)


class KorzinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Korzina
        fields = ('id', 'username', 'tovarnomi', 'tovarnarxi', 'tovarsoni',)



class ZakazSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zakaz
        fields = ('id', 'username', 'tovarnomi', 'tovarnarxi', 'tovarsoni',)