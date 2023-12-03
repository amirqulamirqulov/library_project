from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    description = models.TextField()
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=25, decimal_places=2)
    objects = models.Manager()

    def __str__(self):
        return self.title
