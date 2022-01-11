from django.urls import path
from .views import *

urlpatterns = [
    path('data/<int:pk>', TelemetricModelDetail.as_view()),
    path('postdata', TelemetricPost.as_view()),
    path('getalldata', TelemetricDetail.as_view()),
]