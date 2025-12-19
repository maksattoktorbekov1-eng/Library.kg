from django.db import models

CATEGORY_CHOICES = [
    ('men', 'Мужская'),
    ('women', 'Женская'),
    ('kids', 'Детская'),
]

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
