from django.urls import path

from . import views

app_name = 'ota'

urlpatterns = [
    path('builds/', views.BuildView.as_view(), name='build'),
    path('builds/<pk>/', views.BuildDetailView.as_view(), name='builddetail'),
]
