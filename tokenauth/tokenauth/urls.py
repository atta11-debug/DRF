from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token
from api.auth import CustomAuthToken

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    # path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("gettoken/",obtain_auth_token)
    path("gettoken/",CustomAuthToken.as_view())
]
