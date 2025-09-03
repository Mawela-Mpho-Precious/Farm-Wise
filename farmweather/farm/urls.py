from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("", views.home_page, name="homepage"),  # root URL
    path("click/", views.check_box, name="checkbox"),  # checkbox page
    path('home/', login_required(views.home), name='home'),  # another authenticated page
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/signup/', views.signup_view, name='signup'),
    path('accounts/check_auth/', views.check_auth_view, name='check_auth'),
    path('auth/', views.auth_page_view, name='auth_page'),
    path('journal/', views.journal, name='journal'),
    path("chatbot/", views.chat_page, name="chatbot"), 
    path('weather-dashboard/', views.weather_dashboard, name='weather_dashboard'),
]
