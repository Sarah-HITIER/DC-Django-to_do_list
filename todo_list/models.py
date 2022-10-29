from django.db import models
from django.shortcuts import reverse

# To-Do list
STATUS_CHOICES = (
    (1, "To do"),
    (2, "In progress"),
    (3, "Ended")
)


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=1
    )
    limit_date = models.DateField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return self.title
