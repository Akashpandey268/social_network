from django.urls import path
from .views import user_login, user_signup, obtain_token, user_search, send_friend_request, accept_friend_request, reject_friend_request, list_friends, list_pending_requests

urlpatterns = [
    path('api/auth/login/', user_login, name='user_login'),
    path('api/auth/signup/', user_signup, name='user_signup'),
    path('api/auth/token/', obtain_token, name='token_obtain'),
    path('api/users/search/', user_search, name='user_search'),
    path('api/friends/send-request/', send_friend_request, name='send_friend_request'),
    path('api/friends/accept-request/<int:request_id>/', accept_friend_request, name='accept_friend_request'),
    path('api/friends/reject-request/<int:request_id>/', reject_friend_request, name='reject_friend_request'),
    path('api/friends/list/', list_friends, name='list_friends'),
    path('api/friends/pending-requests/', list_pending_requests, name='list_pending_requests'),
]
