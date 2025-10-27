from django.db import models
from datetime import date
from django.utils import timezone
# Create your models here.


class Poem(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.title


class About(models.Model):
    title = "About Me"
    intro = models.TextField()
    interest = models.TextField()
    bucket_list = models.TextField()

    def save(self, *args, **kwargs):
        if not self.pk and About.objects.exists():
            self.pk = About.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About Me (Singleton)"
