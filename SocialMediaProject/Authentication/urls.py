from django.urls import path
from Authentication.views import *


urlpatterns = [

    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(),name="logout"),



]