from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('posts/', views.PostView.as_view(), name='post'),
    path('posts/<pk>/', views.PostDetailView.as_view(), name='postdetail'),
    path('posts/<pk>/upload-image/', views.PostImageView.as_view(),
         name='postimage'),
]
