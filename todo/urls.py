from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.list, name='list'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('signup', views.signup, name='signup'),
    path('todo', views.todo, name='todo'),
    path('todo/<int:num>', views.control, name='control'),
    path('form', views.form, name='form'),
    path('form/<int:num>', views.edit, name='edit'),
]
