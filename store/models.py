from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse     # this will allow us to build an URL


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        """
        - get_absolute_url() will return a URL string that would point to this model's view
        - Notes for reverse():
          1st parameter -> URL we wish to use
          2nd parameter -> whatever item it is we currently want to view
        """
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):

    WHITE = 'wht'
    BLACK = 'blc'
    RED = 'red'
    BLUE = 'blu'

    COLOR_CHOICES = [
        (WHITE, 'White'),
        (BLACK, 'Black'),
        (RED, 'Red'),
        (BLUE, 'Blue'),
    ]

    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default=WHITE)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField(default=0)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        """
        - get_absolute_url() will return a URL string that would point to this model's view
        - Notes for reverse():
          1st parameter -> URL we wish to use
          2nd parameter -> whatever item it is we currently want to view
        """
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title

