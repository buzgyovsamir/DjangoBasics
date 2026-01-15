from django.db import models

from notes.choices import PriorityChoices


class Note(models.Model):
    title = models.CharField(
        max_length=30
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(choices=PriorityChoices.choices, default=PriorityChoices.LOW)
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        related_name="notes",
        blank=True,
        null=True,
    )


    def __str__(self):
        return self.title