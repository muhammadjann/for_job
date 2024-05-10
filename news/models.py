from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='images/')
    tags = models.ManyToManyField(Tag)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'News'
        verbose_name = 'News'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})
