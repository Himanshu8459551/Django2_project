from django.db import models

# Create your models here.

class Book(models.Model):
  def __str__(self):
    return self.title

  title = models.CharField(max_length=200)
  description = models.TextField(max_length=255)
  price = models.DecimalField(max_digits=5, decimal_places=2)
  image = models.ImageField(default='default.jpeg',upload_to='image/')