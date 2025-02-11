from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

class Article(models.Model):
    STATUS_CHOICES = (
        ('drf', 'Draft'),
        ('Pub', 'Published')
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    summery = models.TextField(null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default='drf', max_length=10)

    def save(self, *args, **kwargs):
        from src.tasks import summarize_article
        is_new = self.pk is None
        try:
            old_article = Article.objects.get(pk=self.pk)
            description_updated = old_article.description != self.description
        except Article.DoesNotExist:
            description_updated = True
        super().save(*args, **kwargs)
        if is_new or description_updated:
            summarize_article.delay(self.pk)

    def __str__(self):
        return self.title


class Knowledge(models.Model):
    STATUS_CHOICES = (
        ('drf', 'Draft'),
        ('Pub', 'Published')
    )
    title = models.CharField(max_length=255, verbose_name='title')
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, default='drf', max_length=10)
    article = models.ManyToManyField(Article, related_name='knowledge')

    def __str__(self):
        return self.title
