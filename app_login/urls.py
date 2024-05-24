
from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboards/', views.dashboards, name='dashboards'),
    path('text_summary', views.text_summary, name="text_summary"),
    path('summary.html', views.summary, name='summary'),
    path('admin/', admin.site.urls),
]