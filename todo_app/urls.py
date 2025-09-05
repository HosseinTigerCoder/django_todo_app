from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='home'),
    path('tasks/',views.taskpage,name='tasks'),
    path('delete_task/<int:id>',views.delete_task,name='delete_task'),
    path('finish_task/<int:id>',views.finish_task,name='finish_task'),
    path('register/',views.register,name='register'),
    path('login/',views.login_site,name='login'),
    path('logout/',views.logout_site,name='logout')
]