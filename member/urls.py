from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'member'

urlpatterns = [
    path('login/',
    auth_views.LoginView.as_view(
        template_name='member/login.html'
    ),
    # django에서 제공하는 로그인 기능, class based view
    
    name='login'
    ),
    path('logout/',
    auth_views.LogoutView.as_view(),
    name='logout'
    ),
    path('signup/', views.signup, name='signup'),
    ]