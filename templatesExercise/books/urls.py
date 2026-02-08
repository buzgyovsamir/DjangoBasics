from django.urls import path, include

from books.views import landing_page, books_list, book_detail, book_reviews
app_name = 'books'

books_patterns = [
        path('', books_list, name='list'),
        path('<slug:slug>/', book_detail, name='details'),
        path('<slug:slug>/reviews/', book_reviews, name='reviews'),
    ]
urlpatterns =[
    path('', landing_page, name='home'),
    path('books/', include(books_patterns)),
]