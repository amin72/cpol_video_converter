import os
import subprocess
from celery import shared_task
from video.models import Video


def convert_video_util(video_path, scale):
    """Convert video file to provided scale"""

    path, filename = os.path.split(video_path)
    filename, ext = os.path.splitext(filename)
    
    scale_option = f'scale=-1:{scale}'
    new_filename = f'{filename}_{scale}{ext}'
    output_file = f'{path}/{new_filename}'

    command_list = [
        'ffmpeg',
        '-i',
        video_path,
        '-vf',
        scale_option,
        '-c:v',
        'libx264',
        '-c:a',
        'copy',
        output_file,
    ]

    result = subprocess.call(command_list)
    if result == 0:
        return new_filename

    return None


@shared_task(name="convert video")
def convert_video(video_id):
    """Celery task to convert videos"""

    video = Video.objects.get(id=video_id)
    video_path = video.video_original.path

    # convert video file to scale 240
    new_filename = convert_video_util(video_path, 240)
    if new_filename:
        print('\nVideo converted to scale 240 successfully\n')
        video.update_video_240(new_filename)
    else:
        print('\nVideo convertion to scale 240 failed\n')

    # convert video file to scale 360
    new_filename = convert_video_util(video_path, 360)
    if new_filename:
        print('\nVideo converted to scale 360 successfully\n')
        video.update_video_360(new_filename)
    else:
        print('\nVideo convertion to scale 360 failed\n')
