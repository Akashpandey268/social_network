# social_network
** Code Files Are In Master Branch **

This project is a social network API built with Django and Django Rest Framework.

## Installation Steps

1. Clone the repository:
   and then
   cd social-network
   
2. Create and activate a virtual environment:
   
   python3 -m venv venv

   source venv/bin/activate

3. Install the dependencies:
   
   pip install -r requirements.txt

4. Apply migrations:
   
   python manage.py migrate

5. Create a superuser:
    
   python manage.py createsuperuser

6. Run the server:
    
   python manage.py runserver



# API Endpoints : 

   POST /api/auth/signup/: User signup with email.
   
   POST /api/auth/login/: User login with email and password.
   
   POST /api/auth/token/: Obtain JWT token.

* User Search
  
   GET /api/users/search/: Search other users by email or name.

* Friendship
  
   POST /api/friends/send-request/: Send friend request to another user.
   
   POST /api/friends/accept-request/<request_id>/: Accept friend request.
   
   POST /api/friends/reject-request/<request_id>/: Reject friend request.
   
   GET /api/friends/list/: List friends of the authenticated user.
   
   GET /api/friends/pending-requests/: List pending friend requests received by the authenticated user.


# Docker

   To containerize the application:
   
   Build and run the containers:
   
   docker-compose up --build
