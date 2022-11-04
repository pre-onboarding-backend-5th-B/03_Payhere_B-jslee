from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

from .views import SignupView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    re_path(r'^jwt-auth/', obtain_jwt_token),
    re_path(r'^jwt-verify/', verify_jwt_token),
    re_path(r'^jwt-refresh/', refresh_jwt_token),
]
