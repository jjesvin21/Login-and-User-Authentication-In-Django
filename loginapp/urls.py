from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from loginapp.views import CreateUser,Hello

urlpatterns = [
    path("api/token/",jwt_views.TokenObtainPairView.as_view()),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view()),
    path('api/newuser/',CreateUser.as_view()),
    path('api/hello/',Hello.as_view())

]

