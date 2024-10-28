from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import CreateUserApiView, UserListApiView, GetCurUserApiView

urlpatterns =[
    path('login/', TokenObtainPairView.as_view()),
    path('register/', CreateUserApiView.as_view()),
    path('list/', UserListApiView.as_view()),
    path('current/', GetCurUserApiView.as_view())
]