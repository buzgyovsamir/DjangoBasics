from django.urls import path, include

from reviews.views import recent_reviews, review_datils

app_name = 'reviews'

reviews_patterns = [
    path('recent/',recent_reviews, name='recent' ),
    path('<int:pk>/', review_datils, name= 'details')
]
urlpatterns = [
    path('', include(reviews_patterns))

]