from django.urls import path
from Home.views import *

urlpatterns= [

    path('', IndexView.as_view(),name="index"),
    path('friend-request/', FriendRequestView.as_view(),name="friend_request"),
    path('all-friends/', AllFriendsView.as_view(),name="all_friends"),
    path('all-friends/<int:id>/', AllFriendsView.as_view(),name="all_friends"),
    path('profile-all/', ProfileAllView.as_view(),name="profile-all"),
    path('profile/', ProfileView.as_view(),name="profile"),
    path('profile/<int:id>/', ProfileView.as_view(),name="profile"),
    path('search/', SearchView.as_view(),name="search"),
    path('create-post/', CreatePostView.as_view(),name="create_post"),

]