from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Video(models.Model):
    video_original = models.FileField()
    video_240 = models.FileField(null=True, blank=True)
    video_360 = models.FileField(null=True, blank=True)
    convert_time = models.PositiveIntegerField(null=True, blank=True)

    def update_video_240(self, filename):
        self.video_240.name = filename
        self.save()

    def update_video_360(self, filename):
        self.video_360.name = filename
        self.save()

    def __str__(self):
        return self.video_original.name


@receiver(post_save, sender=Video)
def video_saved(sender, instance, **kwrags):
    from .tasks import convert_video
    convert_video.delay(instance.id)
