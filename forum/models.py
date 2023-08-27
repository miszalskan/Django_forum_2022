from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
Options = [
            ('Snowboard', 'Snowboard'),
            ('Skiing', 'Skiing'),
            ('Ice skates', 'Ice skates')
        ]


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=Options, default='1')
    is_important = models.BooleanField(default=False)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey('Post', related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']


