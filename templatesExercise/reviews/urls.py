from django.urls import path, include

from reviews.views import recent_reviews, review_datils, review_edit, review_delete, review_create

app_name = 'reviews'

pk_patterns = [
    path('', review_datils, name='details'),
    path('edit/', review_edit, name='edit'),
    path('delete/', review_delete, name='delete'),
]

reviews_patterns = [
    path('recent/',recent_reviews, name='recent' ),
    path('create/', review_create, name='create'),
    path('<int:pk>/',include(pk_patterns))
]
urlpatterns = [
    path('', include(reviews_patterns))

]