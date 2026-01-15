from django.urls import path

from notes import views

urlpatterns = [
    path('', views.hello_notes_view, name= 'hello_notes_view')
]