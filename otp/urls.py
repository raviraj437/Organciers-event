from django.urls import path
from .views import getPhoneNumberRegistered

urlpatterns =[
    path("<phone>/", getPhoneNumberRegistered.as_view(), name="OTP Gen"),
]