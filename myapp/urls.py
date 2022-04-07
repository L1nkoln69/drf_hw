from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),

    path('post/', PostList.as_view()),
    path('post/<int:pk>/', PostDetail.as_view()),

    path('comment/', CommentList.as_view()),
    path('comment/<int:pk>/', CommentDetail.as_view()),
]
