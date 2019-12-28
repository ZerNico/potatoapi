from django.urls import path

from . import views

app_name = 'ota'

urlpatterns = [
    path('builds/', views.BuildView.as_view(), name='build'),
    path('builds/md5/<md5>/', views.BuildDetailHashView.as_view(),
         name='builddetailhash'),
    path('builds/<pk>/', views.BuildDetailView.as_view(), name='builddetail'),
    path('notes/', views.NoteView.as_view(), name='note'),
    path('notes/<device>/', views.NoteDetailView.as_view(), name='notedetail'),
]
