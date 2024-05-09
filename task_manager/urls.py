"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from task_manager.views import (
    HomePageView,
    UserLoginView,
    UserLogoutView,
)

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', HomePageView.as_view(), name='start_page'),
    path('users/', include('task_manager.article.urls'), name='users_list'),
    path('statuses/', include('task_manager.statuses.urls'), name='statuses_list'),
    path('tasks/', include('task_manager.tasks.urls'), name='tasks_list'),
    path('labels/', include('task_manager.labels.urls'), name='labels_list'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
