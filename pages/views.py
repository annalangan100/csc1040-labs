from math import log
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Book, Author
from .forms import *
from rest_framework import viewsets
from .serializers import AuthorSerializer, BookSerializer

# Create your views here.
def home(request):
    username = request.GET.get('username', 'Default')
    return render(request, 'home.html', {'username':username})

def about(request):
    return render(request, 'about.html')


# /profile/1 -> alice 
# /profile/2 -> bob
def profile(request, id):
    users = {
        1:{'username':'alice', 'age':30},
        2:{'username':'bob', 'age':25},
        3:{'username':'charlie', 'age':35}
    }

    user = users.get(id)
    if user is None:
        # a user was not found
        return render(request, 'not_found.html', {'error':f"User with id {id} not found."})
    else:
        return render(request, 'profile.html', {'user':users[id]})
    

def books(request):
    all_books = Book.objects.all() # returns an array of books
    return render(request, 'all_books.html', {'books': all_books})


def book_detail(request, id):
    book = get_object_or_404(Book, id=id) # returns a single book object
    return render(request, 'book_detail.html', {'book': book})

def author_detail(request, id):
    author = get_object_or_404(Author, id=id) # returns a single author object
    return render(request, 'author_detail.html', {'author': author})

@login_required
@user_passes_test(lambda u: u.is_staff)
def add_author(request):
    if request.method=="POST":
        # user has pressed "submit" and is uploading data we need to save
        authorForm = AuthorForm(request.POST)
        if authorForm.is_valid():
            authorForm.save() # save the new author to the database
            return render(request, 'author_added.html', {'author': authorForm.instance})
    else:
        # user is visiting the page for the first time, show them the empty form
        authorForm = AuthorForm()
    return render(request, 'add_author.html', {'form': authorForm})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
