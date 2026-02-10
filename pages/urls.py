from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet, basename='author')
router.register(r'books', views.BookViewSet, basename='book')


urlpatterns = [
    path("", views.home, name="home"), # homepage for 0.0.0.0:8000
    path("about/", views.about, name="about"),
    path("profile/<int:id>/", views.profile, name="profile"), # profile/1, profile/2 
    path("books/", views.books, name="all_books"),
    path("books/<int:id>/", views.book_detail, name="book_detail"),
    path("authors/add/", views.add_author, name="add_author"),
    path("authors/<int:id>/", views.author_detail, name="author_detail"),
    path("register/", views.register, name="register"),
    path("api/", include(router.urls))
]
