from django .urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('newboard/', views.create_board, name='new_board'),
    path('newlist/<str:id>', views.create_list, name='new_list'),
    path('showboard/<str:id>', views.show_board, name='show_board'),
    path('showlist/<str:id>', views.show_list, name='show_list'),
    path('createCard/<str:id>', views.create_card, name='create_card'),
]