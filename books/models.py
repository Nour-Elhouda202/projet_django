from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    publish_date = models.CharField(max_length=50, blank=True)
    language = models.CharField(max_length=50, default='fr')
    download_link = models.URLField(blank=True)
    source = models.CharField(max_length=100)
    cover_image = models.URLField(blank=True)
    pages = models.IntegerField(null=True, blank=True)
    isbn = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']