from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'pace'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^login/', views.LoginUserView.as_view(), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='pace/logout.html'), name='logout'),
    url(r'^dashboard/', views.DashboardView.as_view(), name='dashboard'),
    url(r'^sign_up/', views.SignUpView.as_view(), name='sign_up'),
    url(r'^session_list/', views.SessionListView.as_view(), name='session_list'),


]
