from django.urls import path
from .views import get,post,get1,post1,home

urlpatterns = [

    path('', home, name='home'),
    path('get', get, name='get_postal'),
    path('post/', post, name='post_postal'),
    path('get1/', get1, name='get1'),
    path('post1/', post1, name='post_add'),
    
    
]