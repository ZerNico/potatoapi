from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('me/upload-image/', views.ManageUserImageView.as_view(),
         name='meimage'),
    path('profile/<pk>/', views.UserProfileDetailView.as_view(),
         name='profiledetail'),
    path('profile/<pk>/upload-image/', views.UserProfileImageView.as_view(),
         name='profileimage'),
]
