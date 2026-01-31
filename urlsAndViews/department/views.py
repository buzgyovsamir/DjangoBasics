from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def int_view(request : HttpRequest, id : int) -> HttpResponse:
    return HttpResponse(f'the id is {id} and the type is {type(id)}', content_type='text/plaint')

def str_view(request : HttpRequest, id : str) -> HttpResponse:
    return HttpResponse(f'the id is {id} and the type is {type(id)}', content_type='text/plaint')


def slug_view(request : HttpRequest, slug : str) -> HttpResponse:
    return HttpResponse(f'the id is {slug} and the type is {type(slug)}', content_type='text/plaint')

def path_view(request : HttpRequest, path : str):
    return HttpResponse(f'the id is {path} and the type is {type(path)}', content_type='text/plaint')

def uuid_view(request : HttpRequest, uuid : str):
    return HttpResponse(f'the id is {uuid} and the type is {type(uuid)}', content_type='text/plaint')

def show_archive(request : HttpRequest, archive_year: int) -> HttpResponse:
    return HttpResponse(f'The requested year is {archive_year}', content_type='text/plain')