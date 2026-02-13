from django.db import models

from photos.models import Photo


class Comment(models.Model):
    text = models.CharField(
        max_length=300,
    )
    date_and_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )
    to_photo = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE
    )

class Like(models.Model):
    to_photo = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE,
    )