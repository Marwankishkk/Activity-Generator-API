from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)


class Activity(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    tags = models.CharField(max_length=255, blank=True)
    difficulty_level = models.CharField(max_length=20, choices=(
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ), blank=True)
