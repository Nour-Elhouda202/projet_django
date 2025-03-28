from django.db import models
from title.models import MainTitle 
from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name
class SubTitle(models.Model):
    main_title = models.ForeignKey(MainTitle, on_delete=models.CASCADE, related_name='subtitles')
    subtitle_title = models.CharField(max_length=255)  
    description = models.FileField(upload_to='descriptions/')  
    images = models.ManyToManyField(Image, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)  

    def __str__(self):
        return self.subtitle_title