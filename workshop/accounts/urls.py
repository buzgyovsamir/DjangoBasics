from django.urls import path, include

from accounts import views

app_name = "accounts"

profile_patterns = [
    path('', views.show_profile_details, name='details'),
    path('edit/', views.edit_profile, name='edit'),
    path('delete/', views.delete_profile, name='delete')
]

authentication_patterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login,name='login'),
]

urlpatterns =[
    path('',include(authentication_patterns)),
    path('profile/<int:pk>', include(profile_patterns))
]