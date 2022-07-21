from django.contrib import admin
from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    readonly_fields = (
        'video_240',
        'video_360',
        'convert_time',
    )
