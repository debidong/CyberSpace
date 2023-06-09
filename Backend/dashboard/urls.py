from django.urls import path
from .views import *

# user/dashboard/
urlpatterns = [
    path('info', InfoView.as_view()),
    path('reminder', ReminderView.as_view()),
    path('userList', ListUsersView.as_view()),
    path('userList/friendRequest', FriendRequestView.as_view()),
    path('userList/friendRequest/handle', FriendRequestStatusView.as_view()),
    path('inbox', InboxView.as_view()),
    path('friends', FriendView.as_view())
]