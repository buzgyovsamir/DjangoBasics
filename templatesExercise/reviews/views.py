from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from reviews.forms import CreateReviewForm, EditReviewForm, DeleteReviewForm
from reviews.models import Review


def recent_reviews(request: HttpRequest) -> HttpResponse:
    DEFAULT_REVIEWS_COUNT = 5
    reviews_count = int(request.GET.get('count') or DEFAULT_REVIEWS_COUNT)

    reviews = Review.objects.select_related('book')[:reviews_count]

    context = {
        'reviews' : reviews,
        'page_title' : 'Recent reviews'
    }

    return render(request, 'reviews/list.html', context= context)

def review_datils(request: HttpRequest, pk : int) -> HttpResponse:
    review = get_object_or_404(
        Review.objects.select_related('book'),
        pk=pk,
    )

    context = {
        'review':review,
        'page_title': f"{review.author}'s review on {review.book.title}"
    }
    return render(request, 'reviews/detail.html', context= context)

def review_create(request: HttpRequest) -> HttpResponse:
    form = CreateReviewForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('reviews:recent')

    context = {
        'form' : form,
    }

    return render(request, 'reviews/create.html', context= context)

def review_edit(request: HttpRequest, pk: int) -> HttpResponse:
    review = Review.objects.get(pk=pk)
    form = EditReviewForm(request.POST or None, instance=review)

    if request.method == 'POST' and form.is_valid():
        review = form.save(commit=False)
        review.save()
        return redirect('reviews:details')

    context = {
        'review' : review,
        'form' : form,
    }

    return render(request, 'reviews/edit.html', context= context)
def review_delete(request: HttpRequest, pk: int) -> HttpResponse:
    review = Review.objects.get(pk=pk)
    form = DeleteReviewForm(request.POST or None, instance=review)

    if request.method == 'POST' and form.is_valid():
        review.delete()
        return redirect('reviews:recent')

    context = {
        'form' : form,
        'review' : review,
    }

    return render(request,'reviews/delete.html', context= context)