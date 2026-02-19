from django import forms

from books.models import Book
from reviews.models import Review


class ReviewFormBasic(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'


class CreateReviewForm(ReviewFormBasic):
    ...

class EditReviewForm(ReviewFormBasic):
    ...

class DeleteReviewForm(ReviewFormBasic):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled=True
            self.fields[field].required = False