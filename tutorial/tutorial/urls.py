
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # Web Apllication Endpoints
    path("students",include("students.urls")),
    # Api Endpoints
    path("api/v1/",include("api.urls")),
]
