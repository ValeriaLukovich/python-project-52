from django.urls import path

from task_manager.article.views import (
    IndexView,
    UserFormCreateView,
    UserFormUpdateView,
    UserFormDeleteView,
)
from task_manager.views import UserLoginView, UserLogoutView

urlpatterns = [
    path('', IndexView.as_view(), name='users_list'),
    path('create/', UserFormCreateView.as_view(), name='user_create'),
    path('<int:id>/update/', UserFormUpdateView.as_view(), name='user_update'),
    path('<int:id>/delete/', UserFormDeleteView.as_view(), name='user_delete'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout')
]
