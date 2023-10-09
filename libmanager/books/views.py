from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.views.generic import ListView, DetailView

from books.models import *
from users.models import BooksUser
from books.forms import *
from books import utils


class BookHome(ListView):
    model = Book
    template_name = "books/index.html"
    context_object_name = "books"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Book.objects.all()

class ShowBook(DetailView):
    model = Book
    template_name = 'books/book.html'
    pk_url_kwarg = 'book_id'
    context_object_name = "book"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Book.objects.all()

    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, id=book_id)
        return render(request, "books/book.html")


def book_id(request: HttpRequest, book_id):
    book = get_object_or_404(Book, id=book_id)
    message = "..."
    if request.method == "POST":
        form = UseridForm(request.POST)
        if form.is_valid():
            gived_book = utils.giveaway_a_book(user_id=form.cleaned_data['uid'], book=book)
            if gived_book:
                message = "SUCCESS!"
        return render(request, "books/book.html", context={"book": book,
               "title": "Страница книги",
                   "form": form, "message": message})
    else:
        form = UseridForm()
        context = {"book": book,
               "title": "Страница книги",
                   "form": form}

    return render(request, "books/book.html", context=context)


def addbook(request: HttpRequest):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddBookForm()
    context = {'form': form,
               'title': 'Добавить книгу',
               "url_name": "addbook",
               "btn_title": "Добавить книгу"
               }
    return render(request, "books/book_form.html", context=context)

def findbook(request):
    if request.method == 'POST':
        form = FindBookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            books = Book.objects.filter(title=title)
            return render(request, "books/search.html", {"title": "Результаты поиска", "books": books})
    else:
        form = FindBookForm()
    return render(request, "books/book_form.html", {"title": "Найти книгу", "form": form, "btn_title": "Найти книгу"})


def findauthor(request):
    if request.method == "POST":
        form = FindAuthorForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            books = Book.objects.filter(author=author)
            return render(request,"books/search.html", {"title": "Результаты поиска", "books": books})
    else:
        form = FindAuthorForm()
        return render(request, "books/book_form.html", {"title": "Найти книгу", "form": form, "btn_title": "Найти книгу"})
def delbook(request):

    return HttpResponse("Delete book from library")

def expired(request):
    return HttpResponse("Shows list of expired books")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def about(request: HttpRequest):
    return HttpResponse("About page")

def category(request):
    cats = Category.objects.all()
    title = "Все категории"
    return render(request, 'books/search.html', context={"title": title, "cats": cats})

def genre(request):
    cats = Genres.objects.all()
    title = "Все жанры"
    return render(request, 'books/search.html', context={"title": title, "cats": cats})

def book_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    books = Book.objects.filter(category=category.id)
    title = " Книги в категории " + category.name
    return render(request, "books/search.html", {"title": title, "books": books})

def book_genre(request, genre_slug):
    genre = get_object_or_404(Genres, slug=genre_slug)
    books = Book.objects.filter(genre=genre.id)
    title = "Книги в жанре " + genre.name
    return render(request, "books/search.html", context={"title": title, "books": books})




#Book(title='123', author='123', year=2002, category='Отечественные', genre='Проза', pub_house='Просвещение', isbn='123', total_amount=123)

def addtest(request: HttpRequest):
    if request.method == 'POST':
        form = AddTestForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления книги')
    else:
        form = AddTestForm()
    return render(request, "books/test_add.html", context={'form': form, 'title': 'Добавить test'})
