from django.urls import path, include

from photos import views

app_name = 'photos'


urlpatterns = [
    path('', views.add_photo, name='add'),
    path('<int:pk>', include([
        path('', views.details_photo, name='details'),
        path('edit/', views.edit_photo, name='edit')
]))
]