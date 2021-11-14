from django.urls import path
from .views import signup, logout
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('signup/', signup, name='account-signup'),
    path('login/', obtain_auth_token),
    path('logout',logout,name='account-logout')

]