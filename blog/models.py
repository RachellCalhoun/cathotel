from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models

class Post(models.Model):
    author= models.ForeignKey('auth.User', null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = tinymce_models.HTMLField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    img = models.ImageField(null=True, blank=True)


    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', null=True, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.text

class Notice(models.Model):
    author= models.ForeignKey('auth.User', null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = tinymce_models.HTMLField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    img = models.ImageField(null=True, blank=True)
    PUBLIC = "Public"
    PRIVATE = "Private"
    PRIVACY = (
        (PUBLIC, "Public"),
        (PRIVATE, "Private"),
        )
    privacy = models.CharField(max_length=15, choices=PRIVACY, default=PUBLIC)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
# Create your models here.
