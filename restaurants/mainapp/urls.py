from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('post/<slug:slug>/', ShowPost.as_view(), name='post'),
    path('del_post/', DelPost.as_view(), name='del_post'),
    path('post/<slug:slug>/update', PutPost.as_view(), name='update'),
    path('post/<slug:slug>/delete', DelPost.as_view(), name='delete'),
    path('search/', SearchResult.as_view(), name='search'),

]
