from django .urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('newboard/', views.create_board, name='new_board'),
    path('showboard/<str:id>', views.show_board, name='show_board'),
    path('newlist/', views.create_list, name='new_list'),
    path('showlist/<str:id>', views.show_list, name='show_list'),
    path('deletelist/<str:id>', views.delete_list, name='delete_list'),
    path('createcard/', views.create_card, name='create_card'),
    path('deletecard/<str:id>', views.delete_card, name='delete_card'),
    path('showcard/<str:id>', views.show_card, name='show_card'),
]