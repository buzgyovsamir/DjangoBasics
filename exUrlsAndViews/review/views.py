from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from review.models import Review

DEFAULT_REVIEW_COUNT: int = 5
MAX_REVIEW_COUNT: int = 50


def recent_reviews(request: HttpRequest) -> HttpResponse:
    """
    Display a list of recent published reviews.
    
    Query parameter:
        review_count: Number of reviews to display (default: 5, max: 50)
    """
    try:
        review_count = int(request.GET.get('review_count', DEFAULT_REVIEW_COUNT))
        review_count = min(max(review_count, 1), MAX_REVIEW_COUNT)  # Clamp between 1 and MAX
    except (ValueError, TypeError):
        review_count = DEFAULT_REVIEW_COUNT
    
    reviews = Review.objects.filter(is_published=True).order_by('-created_at')[:review_count]

    context = {
        'reviews': reviews,
        'page_title': 'Recent Reviews'
    }

    return render(request, 'review/list.html', context)


def review_detail(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(Review, pk=pk)

    context = {
        'review': review,
        'page_title': f"{review.author}'s review on {review.destination.name}"
    }

    return render(request, 'review/detail.html', context)

def reviews_by_year(request: HttpRequest, year: int) -> HttpResponse:
    """
    Display reviews filtered by year.
    
    Args:
        year: The year to filter reviews by (e.g., 2024)
    """
    reviews = Review.objects.filter(
        is_published=True,
        created_at__year=year
    ).order_by('-created_at')

    context = {
        'page_title': f'Reviews for {year}',
        'reviews': reviews,
    }

    return render(request, 'review/list.html', context)