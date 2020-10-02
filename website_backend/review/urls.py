from django.urls import path
from .views import *

urlpatterns = [
    path('', review_index, name='review_index')
]