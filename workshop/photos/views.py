from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def add_photo(request: HttpRequest) -> HttpResponse:
    return render(request, 'photos/photo-add-page.html')

def details_photo(request: HttpRequest, pk,int) -> HttpResponse:
    return render(request, 'photos/photo-details-page.html')

def edit_photo(request: HttpRequest, pk:int) -> HttpResponse:
    return render(request, 'photos/photo-edit-page.html')
