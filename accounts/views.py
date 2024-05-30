from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from django.utils import timezone
from django.core.cache import cache
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser, FriendRequest
from .serializers import UserSerializer, FriendRequestSerializer


# User Authentication Endpoints

@api_view(['POST'])
def user_login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def user_signup(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if email and password:
        if CustomUser.objects.filter(email=email).exists():
            return Response({'message': 'Email already in use'}, status=status.HTTP_400_BAD_REQUEST)
        user = CustomUser.objects.create_user(email=email, password=password)
        return Response({'message': 'Signup successful'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)


# User Search Endpoint

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_search(request):
    search_query = request.query_params.get('search_query', '')
    users = CustomUser.objects.filter(email__icontains=search_query) | CustomUser.objects.filter(first_name__icontains=search_query) | CustomUser.objects.filter(last_name__icontains=search_query)
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(users, request)
    serializer = UserSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


# Friendship Endpoints

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_friend_request(request):
    to_user_id = request.data.get('to_user_id')
    if not to_user_id:
        return Response({'message': 'to_user_id is required'}, status=status.HTTP_400_BAD_REQUEST)
    if request.user.sent_requests.filter(to_user_id=to_user_id).exists():
        return Response({'message': 'Friend request already sent to this user'}, status=status.HTTP_400_BAD_REQUEST)
    if request.user == CustomUser.objects.get(pk=to_user_id):
        return Response({'message': 'Cannot send friend request to yourself'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Rate limiting logic
    user_id = request.user.id
    cache_key = f'friend_request_count_{user_id}'
    count = cache.get(cache_key, 0)
    if count >= 3:
        return Response({'message': 'Rate limit exceeded'}, status=status.HTTP_429_TOO_MANY_REQUESTS)
    cache.set(cache_key, count + 1, timeout=60)
    
    FriendRequest.objects.create(from_user=request.user, to_user_id=to_user_id)
    return Response({'message': 'Friend request sent'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def accept_friend_request(request, request_id):
    friend_request = FriendRequest.objects.filter(pk=request_id, to_user=request.user).first()
    if friend_request:
        friend_request.delete()
        friend_request.from_user.friends.add(request.user)
        request.user.friends.add(friend_request.from_user)
        return Response({'message': 'Friend request accepted'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Friend request not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reject_friend_request(request, request_id):
    friend_request = FriendRequest.objects.filter(pk=request_id, to_user=request.user).first()
    if friend_request:
        friend_request.delete()
        return Response({'message': 'Friend request rejected'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Friend request not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_friends(request):
    serializer = UserSerializer(request.user.friends, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_pending_requests(request):
    serializer = FriendRequestSerializer(request.user.received_requests, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Token Endpoint

@api_view(['POST'])
def obtain_token(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
