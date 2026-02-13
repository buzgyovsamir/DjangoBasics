from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def add_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'pets/pet-add-page.html')

def delete_page(request: HttpRequest, username:str, slug:str) -> HttpResponse:
    return render(request, 'pets/pet-delete-page.html')

def details(request: HttpRequest, username:str, slug:str) -> HttpResponse:
    return render(request, 'pets/pet-details-page.html')

def edit_page(request: HttpRequest, username:str, slug:str) -> HttpResponse:
    return render(request, 'pets/pet-edit-page.html')