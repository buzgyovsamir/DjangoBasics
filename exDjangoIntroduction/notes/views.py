from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from notes.models import Note


def hello_notes_view(request : HttpRequest) -> HttpResponse:
    query = request.GET.get('q')
    notes = Note.objects.prefetch_related('category').all()

    if query:
        notes = notes.filter(title__icontains= query)

    context = {
        "notes": notes,
        'query' : query or "",
    }
    return render(request, "index.html", context)
