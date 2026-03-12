from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

#for viewsets, to set default routers we have to write these lines
router=DefaultRouter()
router.register("students",StudentViewSet)

urlpatterns = [
    #we have to include this in url patterns for default router to work
    path('',include(router.urls)),
    
    #write this url for session authentication
    # path('auth/',include("rest_framework.urls")),
]
