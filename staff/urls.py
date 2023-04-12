from . import views
from django.urls import path


# urls for the User functions and members views only.
urlpatterns = [
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('change_password/',
         views.change_password, name='change_password'),
]
