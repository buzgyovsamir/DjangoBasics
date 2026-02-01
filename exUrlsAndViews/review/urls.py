from django.urls import path, re_path

from review.views import recent_reviews, review_detail, reviews_by_year

app_name = 'review'
urlpatterns = [
    path('', recent_reviews, name= 'list'),
    path('details/<int:pk>/', review_detail, name='review_detail'),
    re_path(r'^year/(?P<year>20\d{2})/$', reviews_by_year, name='by_year')

]
