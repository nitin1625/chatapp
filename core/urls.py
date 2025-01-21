from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views 


urlpatterns=[
    path('',views.front_page,name='frontpage'),
    path('signup/',views.signup_page,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',views.logout_view,name='logout'),
]
