from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ImageTestmonial, Category, Image, Video, Event, Testmonial
from rest_framework import generics
from .serializers import ImageTestmonialSerializer, CategorySerializer, TestmonialSerializer, EventSerializer, ImageSerializer, VideoSerializer
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, permissions
def home(request):
    return JsonResponse({'foo':'bar'})
class CategoryList(APIView):

    def get(self, request):
        Category1 = Category.objects.all()
        serializer = CategorySerializer(Category1,many=True)
        permissions_classes = [AllowAny]
        return Response(serializer.data)
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ImageList(generics.ListAPIView):
    pagination_class = StandardResultsSetPagination
    serializer_class = ImageSerializer
    permissions_classes = [AllowAny]
    def get_queryset(self):
        queryset = Image.objects.all()
        # print(self.request.query_params.get('categoryid'))
        categoryfilter = self.request.query_params.get('categoryid', None)
        if categoryfilter is not None:
            queryset = queryset.filter(category_id=categoryfilter)
        return queryset
class VideoList(generics.ListAPIView):
    pagination_class = StandardResultsSetPagination
    serializer_class = VideoSerializer
    permissions_classes = [AllowAny]
    def get_queryset(self):
        queryset = Video.objects.all()
        # print(self.request.query_params.get('categoryid'))
        categoryfilter = self.request.query_params.get('categoryid', None)
        if categoryfilter is not None:
            queryset = queryset.filter(category_id=categoryfilter)
        return queryset

class EventList(generics.ListAPIView):
    pagination_class = StandardResultsSetPagination
    serializer_class = EventSerializer
    permissions_classes = [AllowAny]
    def get_queryset(self):
        queryset = Event.objects.all()
        # print(self.request.query_params.get('categoryid'))
        eventfilter = self.request.query_params.get('eventid', None)
        if eventfilter is not None:
            queryset = queryset.filter(organiser_id=eventfilter)
        return queryset


class TestmonialList(generics.ListAPIView):
    pagination_class = StandardResultsSetPagination
    serializer_class = TestmonialSerializer
    permissions_classes = [AllowAny]
    def get_queryset(self):
        queryset = Testmonial.objects.all()
        # print(self.request.query_params.get('categoryid'))
        testmonialfilter = self.request.query_params.get('oragniserid', None)
        if testmonialfilter is not None:
            queryset = queryset.filter(organiser_id=testmonialfilter)
        return queryset

class ImageTestmonialList(generics.ListAPIView):
    pagination_class = StandardResultsSetPagination
    serializer_class = ImageTestmonialSerializer
    permissions_classes = [AllowAny]
    def get_queryset(self):
        queryset = ImageTestmonial.objects.all()
        # print(self.request.query_params.get('categoryid'))
        Testmonialfilter = self.request.query_params.get('testmonialid', None)
        if Testmonialfilter is not None:
            queryset = queryset.filter(testmonial_id=Testmonialfilter)
        return queryset
