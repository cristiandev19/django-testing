import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    post_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.post_text

    def was_published_recently(self):
        """
        antes tenia este codigo:
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        pero tenia un bug que si pongo una fecha futura no mostraba un error
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.comment_text

