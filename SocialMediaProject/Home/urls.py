from django.urls import path
from Home.views import *

urlpatterns= [

    path('', IndexView.as_view(),name="index"),
    path('massage/', MassageView.as_view(),name="massage"),
    path('notification/', NotificationView.as_view(),name="notification"),
    path('profile-all/', ProfileAllView.as_view(),name="profile-all"),
    path('profile/', ProfileView.as_view(),name="profile"),
    path('search/', SearchView.as_view(),name="search"),

]