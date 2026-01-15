from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from tasks.models import Tasks


# def index(request: HttpRequest) -> HttpResponse:
#     all_tasks = Tasks.objects.all()
#
#     template = [
#         "<h1>All tasks<h1/>",
#         *[f"<h3>{t.title} - {t.is_completed}</h3>" for t in all_tasks]
#     ]
#
#     return HttpResponse(
#         "\n".join(template),
#     )

def index1(request: HttpRequest) -> HttpResponse:
    context = {
        "tasks": Tasks.objects.all()
    }

    return render(request, "index.html", context)