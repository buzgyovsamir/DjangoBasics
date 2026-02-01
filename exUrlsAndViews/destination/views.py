from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from destination.models import Destination


def index(request: HttpRequest) -> HttpResponse:
    """Welcome page for the travel application."""
    return render(request, 'destination/index.html', {'page_title': 'Home'})


def destinations_list(request: HttpRequest) -> HttpResponse:
    """
    Display a list of all active destinations.
    """
    destinations = Destination.objects.filter(is_active=True).order_by('name')

    context = {
        'destinations': destinations,
        'page_title': 'All Destinations'
    }

    return render(request, 'destination/list.html', context)


def destination_detail(request: HttpRequest, slug: str) -> HttpResponse:
    """
    Display detailed information about a specific destination.
    
    Args:
        slug: The slug identifier for the destination
    """
    destination = get_object_or_404(Destination, slug=slug, is_active=True)
    
    # Get related reviews for this destination
    reviews = destination.reviews.filter(is_published=True).order_by('-created_at')[:5]

    context = {
        'destination': destination,
        'page_title': f'{destination.name} Details',
        'reviews': reviews,
    }

    return render(request, 'destination/detail.html', context)


def redirect_home(request: HttpRequest) -> HttpResponse:
    return redirect('destination:list')
