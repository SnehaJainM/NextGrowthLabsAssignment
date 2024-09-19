"""
URL configuration for firstapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import home
from home.views import adminn
from home.views import register
from home.views import login_view,registered_apps_view
from home.views import profile,tasks,task_apps,completed_tasks
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    
    path('adminn/',adminn,name='admin-page'),
    path('apps-list/',registered_apps_view,name='apps_list'),
        
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
 
    path('profile/',profile,name='profile'),
    path('tasks/',tasks,name='tasks'),
    path('apps/',task_apps,name='task_apps'),
    path('completed-tasks/',completed_tasks,name='completed_tasks')
]   


