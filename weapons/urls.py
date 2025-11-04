from django.urls import path
from . import views

app_name = 'weapons'

urlpatterns = [
    path('', views.WeaponListView.as_view(), name='weapon_list'),
]