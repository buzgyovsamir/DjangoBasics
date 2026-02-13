from django.db import models
from django.template.defaultfilters import slugify


class Pet(models.Model):
    name = models.CharField(
        max_length=30,
    )
    pet_photo = models.URLField()
    birth_date = models.DateField(
        blank=True,
        null=True
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        null=False,
        editable=False,
    )

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(f"{self.name}-{self.pk}")
        super().save(*args,**kwargs)