from django.urls import path
from sandalwood.views import *


urlpatterns=[
    path('king/',king,name='king'),
    path('joker/',joker,name='joker'),
]