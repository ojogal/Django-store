from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='home'),
  path('home', views.index, name='home'),
  path('signup', views.signup, name='signup'),
  path('product/create', views.create, name='create'),
  path('product/<int:pk>', views.show, name='show'),
  path('product/<int:pk>/update', views.update, name='update'),
  path('product/<int:pk>/delete', views.delete, name='delete'),
]