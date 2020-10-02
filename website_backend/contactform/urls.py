from django.urls import path
from .views import *

urlpatterns = [
path('', showform, name='showform'),
    path('add', addcontact, name='addcontact')
]