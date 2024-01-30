from django.contrib import admin
from django.urls import path,include
from books import views

urlpatterns = [
    path( 'hello/' , views.hello, name="hello"),
    path('book/', views.book, name="book"),
    path('book/detail/<int:id>', views.detail, name="detail"),
    path('book/detail/update/<int:id>', views.update, name="update"),
    path('book/detail/delete/<int:id>', views.delete, name='delete'),
  
    
]