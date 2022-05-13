from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,  name = 'home'),
    path('login_page',views.login_page,  name = 'login_page'),
    path('Signup',views.signup,  name = 'signup'),
    path('index_two',views.index_two,  name = 'index_two'),
    path('index',views.index,  name = 'index_two'),
    path('loginop',views.loginop,  name = 'login_page'),
    path('user_login',views.user_login,  name = 'login_page'),
    path('admin_login',views.admin_login,  name = 'login_page'),
    path('book',views.book,  name = 'login_page'),
]


