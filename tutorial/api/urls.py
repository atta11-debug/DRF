from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

router = DefaultRouter()
router.register("employees", views.EmployeeViewset, basename="employee")

urlpatterns = [
    # path("api/token/", TokenObtainPairView.as_view()),
    # path("api/token/refresh/", TokenRefreshView.as_view()),
    
    path("students/", views.studentsView),
    path("students/<int:pk>/", views.studentDetailView),
    # path("employees/",views.Employees.as_view()),
    # path("employees/<int:pk>/",views.EmployeeDetails.as_view())
    path("", include(router.urls)),
    path("blogs/", views.BlogsView.as_view()),
    path("blogs/<int:pk>/", views.BlogDetailsView.as_view()),
    path("comments/", views.CommentsView.as_view()),
    path("comments/<int:pk>/", views.CommentDetailsView.as_view()),
]
