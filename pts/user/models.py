from datetime import timezone
from django.db import models

from pts.ptsblog.models import Post

# Create your models here.


class User(models.Model):
    nickaname = models.CharField(max_length=75,
                                 unique=True)
    password = models.CharField()
    email = models.CharField(unique=True)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=140)
    posts = models.ManyToManyField(Post)

    def __str__(self) -> str:
        return self.nickname
