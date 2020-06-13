from . models import  Category, Image, Video, Event, Testmonial, ImageTestmonial
from .models import *
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        # fields = {'id','username','password','first_name','last_name','phone',}
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class TestmonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testmonial
        fields = '__all__'

class ImageTestmonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTestmonial
        fields = '__all__'
