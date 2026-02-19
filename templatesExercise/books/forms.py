from datetime import date
from typing import Any

from django import forms

from books.models import Book, Tag


#
#
# class BookFromBasic(forms.Form):
#     title = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder':"e.g. Done"
#             }
#         )
#     )
#     price = forms.DecimalField(
#         max_digits=6,
#         decimal_places=2,
#         min_value=0,
#         widget=forms.NumberInput(
#             attrs={
#                 'step': '2',
#             }
#         ),
#         label= "Price (USD)"
#     )
#     isbn = forms.CharField(
#         max_length=12,
#         min_length=10,
#     )
#
#     genre = forms.ChoiceField(
#         choices=Book.GenreChoices.choices,
#     )
#
#     publishing_date = forms.DateField(
#         initial=date.today,
#     )
#     description = forms.CharField(
#         widget=forms.Textarea
#     )
#     image_url = forms.URLField()
#
#     publisher =forms.CharField(
#         max_length=100,
#     )

class BookFromBasic(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        exclude = ['slug']
        model = Book

    def __init__(self, *args, **kwargs)-> None:
        super().__init__(*args, **kwargs)
        self.fields['tags'].queryset = Tag.objects.all()

class BookCreateForm(BookFromBasic):
    ...

class BookEditForm(BookFromBasic):
    ...

class BookDeleteForm(BookFromBasic):
    # class Meta(BookFromBasic.Meta):
    #     widgets= {
    #         'title': forms.TextInput(
    #             attrs={'disabled': True}
    #         )
    #     }

    def __init__(self, *args : Any, **kwargs : Any):
        super().__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].disabled = True
            self.fields[name].required = False

class BookSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        label='',
        required=False,
    )