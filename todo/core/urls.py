from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about/', views.about, name= 'about'),
    path('logout/', views.logout_user, name= 'logout'),
    path('login/', views.login_user, name= 'login'),
    path('register/', views.register_user, name= 'register'),
    path('detail/<int:pk>', views.todo_detail, name= 'detail'),
    path('delete/<int:pk>', views.delete_todo, name= 'delete'),
    path('add/', views.add_todo, name= 'add'),
    path('update/<int:pk>', views.update_todo, name= 'update'),
]
