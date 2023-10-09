from django.urls import path
from books import views

urlpatterns = [
    path('', views.BookHome.as_view(), name='home'),
    path('<int:book_id>/', views.book_id, name="book"),
    path('cats/', views.category, name="category"),
    path('genres/', views.genre, name="genre"),
    path('cats/<slug:cat_slug>/', views.book_category, name="book_cat"),
    path('genres/<slug:genre_slug>/', views.book_genre, name="book_genre"),
    path('add/', views.addbook, name="addbook"),
    path('find/', views.findbook, name="findbook"),
    path('findauthor/', views.findauthor, name="findauthor"),
    path('del/', views.delbook, name="delbook"),
    path('expired/', views.expired, name="expired"),
    path('giveaway/', views.giveaway, name="giveaway"),
    path('addtest/', views.addtest, name="addtest"),
]

