from django.db import models

class Tasks(models.Model):
    title = models.CharField(
        max_length= 50,
    )
    text = models.TextField()
    is_completed = models.BooleanField()


    def __str__(self):
        return f"{self.title} - {self.text} - {self.is_completed}"