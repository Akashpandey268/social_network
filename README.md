# social_network


This project is a simple social network API built with Django and Django Rest Framework.

## Installation Steps

1. Clone the repository:
2. 
   git clone https://github.com/Akashpandey268/social-network.git
   
   cd social-network
   
3. Create and activate a virtual environment:
4. 
python3 -m venv venv

source venv/bin/activate

5. Install the dependencies:
6. 
pip install -r requirements.txt

7. Apply migrations:
8. 
python manage.py migrate

9. Create a superuser:
10. 
python manage.py createsuperuser

11. Run the server:
12. 
python manage.py runserver



# API Endpoints : 

POST /api/auth/signup/: User signup with email.

POST /api/auth/login/: User login with email and password.

POST /api/auth/token/: Obtain JWT token.

* User Search
* 
GET /api/users/search/: Search other users by email or name.

* Friendship
* 
POST /api/friends/send-request/: Send friend request to another user.

POST /api/friends/accept-request/<request_id>/: Accept friend request.

POST /api/friends/reject-request/<request_id>/: Reject friend request.

GET /api/friends/list/: List friends of the authenticated user.

GET /api/friends/pending-requests/: List pending friend requests received by the authenticated user.


# Docker

To containerize the application:

Build and run the containers:

docker-compose up --build
