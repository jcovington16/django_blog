from django.db import models
from datetime import datetime

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100)
    date = models.DateField(default=datetime.now)
    text = models.TextField()
