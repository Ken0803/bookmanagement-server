from django.urls import path
from myapp import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/create/', views.create_book, name='create_book'),
    path('book/update/<int:book_id>/', views.update_book, name='update_book'),
    path('book/delete/<int:book_id>/', views.delete_book, name='delete_book'),
]
