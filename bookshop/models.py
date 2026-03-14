from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=80)
    description = models.TextField()
    price = models.DecimalField(decimal_places=3, max_digits=10)
    stock_count = models.IntegerField()
    published_date = models.DateField()
    is_available = models.BooleanField(default=True)