from django.db.models import Avg, Q
from django.forms import modelform_factory
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from books.forms import BookFromBasic, BookCreateForm, BookEditForm, BookDeleteForm, BookSearchForm
from books.models import Book


def landing_page(request: HttpRequest) -> HttpResponse:
    total_books = Book.objects.count()
    latest_book = Book.objects.order_by('-publishing_date').first()

    context = {
        'total_books' : total_books,
        'latest_book' : latest_book,
        'page_title': 'Home'
    }

    return render(request, 'books/landing_page.html', context=context)


def books_list(request : HttpRequest) -> HttpResponse:
    search_form = BookSearchForm(request.GET or None)

    list_books = Book.objects.annotate(
        avg_rating= Avg('reviews__rating')
    ).order_by('title')

    if request.GET:
        if search_form.is_valid():
            search_value = search_form.cleaned_data['query']
            list_books = Book.objects.filter(
                Q(title__icontains=search_value)
                |
                Q(description__icontains=search_value)
            )

    context = {
        'books' : list_books,
        'page_title' : 'Dashboard',
        'search_form' : search_form,
    }

    return render(request, 'books/list.html', context= context)

def book_detail(request: HttpRequest, slug : str) -> HttpResponse:
    book = get_object_or_404(
        Book.objects.annotate(
            avg_rating=Avg('reviews__rating'),
        ), slug = slug

    )

    context = {
        'book': book,
        'page_title':f'{book.title} details'
    }

    return render(request, 'books/detail.html', context=context)


def book_reviews(request: HttpRequest, slug: str) -> HttpResponse:
    book = get_object_or_404(Book, slug=slug)
    reviews = book.reviews.all()

    context = {
        'book': book,
        'reviews': reviews,
        'page_title': f'Reviews for {book.title}',
    }
    return render(request, 'books/reviews_list.html', context=context)

def book_create(request:HttpRequest) -> HttpResponse:
    form = BookCreateForm(request.POST or None)
    # BookForm = modelform_factory(
    #     Book,
    #     exclude=['slug']
    # )
    # form = BookForm(request.POST or None)


    if request.method == 'POST' and form.is_valid():
        # Book.objects.create(
        #     **form.cleaned_data,
        #     # title=form.cleaned_data['title'],
        #     # price=form.cleaned_data['price'],
        #     # isbn=form.cleaned_data['isbn'],
        #     # genre=form.cleaned_data['genre'],
        #     # publishing_date=form.cleaned_data['publishing_date'],         harder way
        #     # description=form.cleaned_data['description'],
        #     # image_url=form.cleaned_data['image_url'],                       For model form we just use the save() method
        #     # publisher = form.cleaned_data['publisher']
        # )
        book = form.save(commit=False)
        book.save()
        if 'tags' in form.cleaned_data:
            book.tag_set.set(form.cleaned_data['tags'])
        return redirect('books:home')

    context = {
        'form': form,
    }

    return render(request, 'books/create.html', context)


def book_edit(request: HttpRequest, pk:int) -> HttpResponse:
    book =Book.objects.get(pk=pk)
    form = BookEditForm(request.POST or None, instance=book)

    if request.method == 'POST' and form.is_valid():
        book = form.save(commit=False)
        book.save()
        if 'tags' in form.cleaned_data:
            book.tag_set.set(form.cleaned_data['tags'])
        return redirect('books:home')

    context = {
        'book' : book,
        'form' : form,
    }

    return render(request, 'books/edit.html', context= context)

def book_delete(request: HttpRequest,pk :int) -> HttpResponse:
    book = Book.objects.get(pk=pk)
    form = BookDeleteForm(request.POST or None, instance=book)

    if request.method == 'POST' and form.is_valid():
        book.delete()
        return redirect('books:home')

    context = {
        'book' : book,
        'form': form
    }

    return render(request, 'books/delete.html', context=context)


