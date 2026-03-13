from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.


"""
#BASIC AUTHENTICATION
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes=[BasicAuthentication]
    # permission_classes=[AllowAny]
    # permission_classes=[IsAuthenticated]
    permission_classes=[IsAdminUser]
    
    
#SESSION AUTHENTICATION
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes=[SessionAuthentication]
    # permission_classes=[AllowAny]
    # permission_classes=[IsAuthenticated]
    permission_classes=[IsAdminUser]
    """


# TOKEN AUTHENTICATION

# we generate token by four ways
# 1. from admin panel,
# 2. using django manage.py command like :  python manage.py drf_create_token user_name
# 3. by exposing api endpoint like :
# http POST http://127.0.0.1:8000/gettoken/ username="amna" password="amna5464"
# 4. Using Signals
# Create Signals

#after token generation we can use them to manipulate data
# to get data:  http http://127.0.0.1:8000/api/students/ 'Authorization:Token token_key'
# to add data:  http -f POST http://127.0.0.1:8000/api/students/ name=atif email=atif@gmail.com 'Authorization:Token token_key'
# to delete data:  http -f PUT http://127.0.0.1:8000/api/students/1/ 'Authorization:Token token_key'


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


"""
# SIMPLE JWT AUTHENTICATION
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    # permission_classes=[AllowAny]
    permission_classes = [IsAuthenticated]
    # permission_classes=[IsAdminUser]


# GET TOKENS
# http POST http://127.0.0.1:8000/api/token/ username="username" password="password"
# REFRESH TOKEN
# http GET http://127.0.0.1:8000/api/students/ "Authorization: Bearer access_token_here"
# ACCESS TOKEN
# http POST http://127.0.0.1:8000/api/token/refresh/ refresh="your_refresh_token_here"
"""
