from django.urls import path
from . import views

app_name = 'unit'

urlpatterns = [
    # post views
    path('search/', views.airman_search, name='airman_search'),
    # path('search/', views.airman_first_name_search(), name='airman_first_name_search'),
    path('<int:year>/<int:month>/<int:day>/<slug:airman>/',
         views.airman_detail,
         name='airman_detail'),
    path('naughty/', views.NaughtyListView.as_view(), name='all_naughty_list'),
    path('profiles/', views.ProfileListView.as_view(), name='all_profile_list'),
    path('ptls/', views.PhysicalTrainingLeaderListView.as_view(), name='all_ptl_list'),
    path('ufpms/', views.UnitFitnessProgramManagerListView.as_view(), name='all_ufpm_list'),
    path('', views.AirmanListView.as_view(), name='airman_list'),
]
