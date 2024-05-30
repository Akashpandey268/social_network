"""
URL configuration for social_network project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/auth/', include('dj_rest_auth.urls')),
#     path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
#     path('api/', include('accounts.urls')),
# ]
from django.urls import path
from accounts.views import user_login, user_signup, obtain_token, user_search, send_friend_request, accept_friend_request, reject_friend_request, list_friends, list_pending_requests

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



