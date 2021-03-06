from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Post(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    password = models.PositiveBigIntegerField(blank=True, default=000000)
    title = models.CharField(max_length=40)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-published_date']

class Comment(models.Model):
    postconnect = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=512)
    timestamp = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        ordering = ['-timestamp']