from django.urls import path, include
from Category_Auth import views


urlpatterns =[
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]