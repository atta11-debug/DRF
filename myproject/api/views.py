from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
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
    
    
    
#SIMPLE JWT AUTHENTICATION
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes=[JWTAuthentication]
    # permission_classes=[AllowAny]
    permission_classes=[IsAuthenticated]
    # permission_classes=[IsAdminUser]
    

#GET TOKENS
# http POST http://127.0.0.1:8000/api/token/ username="username" password="password"
#REFRESH TOKEN
# http GET http://127.0.0.1:8000/api/students/ "Authorization: Bearer access_token_here"
#ACCESS TOKEN
# http POST http://127.0.0.1:8000/api/token/refresh/ refresh="your_refresh_token_here"
    
