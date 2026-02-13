from django.urls import path, include

from pets import views

app_name = 'pets'

urlpatterns = [
    path('add/', views.add_page, name='add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.details, name='details'),
        path('edit/', views.edit_page, name='edit'),
        path('delete/', views.delete_page, name='delete'),

]))
]