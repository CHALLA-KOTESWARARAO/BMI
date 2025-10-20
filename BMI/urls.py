from django.urls import path
from .views import bmi_cal

urlpatterns=[
    path("",bmi_cal,name="bmi_cal")
]