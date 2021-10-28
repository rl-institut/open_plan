from django.urls import path

from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('change_password/', change_password, name='change_password'),
    path('user_info/', user_info, name='user_info'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]
