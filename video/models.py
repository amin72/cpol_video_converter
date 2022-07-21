from django.db import models

class Video(models.Model):
    video_original = models.FileField()
    video_240 = models.FileField(null=True, blank=True)
    video_360 = models.FileField(null=True, blank=True)
    convert_time = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.video_original.name
