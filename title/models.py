from django.db import models
import os

# دالة مخصصة لتحديد مسار تحميل الصور
def get_image_upload_path(instance, filename):
    # يمكنك تغيير المسار حسب احتياجاتك
    return os.path.join('images', filename)

class MainTitle(models.Model):
    title = models.CharField(max_length=255)
    description = models.FileField(upload_to='descriptions/')
    image = models.ImageField(upload_to=get_image_upload_path)  # استخدام الدالة المخصصة
    video = models.FileField(upload_to='videos/', null=True, blank=True)

    def __str__(self):
        return self.title