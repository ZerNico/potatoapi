from django.urls import path

from . import views

app_name = 'ota'

urlpatterns = [
    path('builds/', views.BuildView.as_view(), name='build'),
    path('builds/<pk>/', views.BuildDetailView.as_view(), name='builddetail'),
    path('downloads/__private__/<device>/<dish>/weeklies/<filename>',
         views.mirror_weekly_redirect, name='mirrorweeklyredirect'),
    path('downloads/__private__/<device>/<dish>/<filename>', views.mirror_redirect,
         name='mirrorredirect'),
    path('downloads/<device>/<dish>/weeklies/<filename>', views.sf_weekly_redirect,
         name='sfweeklyredirect'),
    path('downloads/<device>/<dish>/<filename>', views.sf_redirect,
         name='sfredirect'),

]
